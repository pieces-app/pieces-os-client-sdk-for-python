from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import TYPE_CHECKING, Callable, Optional,Dict, Union
import platform
import atexit
import subprocess
import urllib.request
import urllib.error
import time
import socket

from pieces_os_client import __version__

from pieces_os_client.api_client import ApiClient
from pieces_os_client.configuration import Configuration

from pieces_os_client.api.conversation_api import ConversationApi
from pieces_os_client.api.conversation_message_api import ConversationMessageApi
from pieces_os_client.api.conversation_messages_api import ConversationMessagesApi
from pieces_os_client.api.conversations_api import ConversationsApi
from pieces_os_client.api.qgpt_api import QGPTApi
from pieces_os_client.api.user_api import UserApi
from pieces_os_client.api.format_api import FormatApi
from pieces_os_client.api.connector_api import ConnectorApi
from pieces_os_client.api.os_api import OSApi
from pieces_os_client.api.allocations_api import AllocationsApi
from pieces_os_client.api.search_api import SearchApi
from pieces_os_client.api.asset_api import AssetApi
from pieces_os_client.api.well_known_api import WellKnownApi
from pieces_os_client.api.assets_api import AssetsApi
from pieces_os_client.api.models_api import ModelsApi
from pieces_os_client.api.annotations_api import AnnotationsApi
from pieces_os_client.api.annotation_api import AnnotationApi
from pieces_os_client.api.linkify_api import LinkifyApi
from pieces_os_client.api.tags_api import TagsApi
from pieces_os_client.api.tag_api import TagApi
from pieces_os_client.api.website_api import WebsiteApi
from pieces_os_client.api.websites_api import WebsitesApi
from pieces_os_client.api.anchors_api import AnchorsApi
from pieces_os_client.api.anchor_api import AnchorApi
from pieces_os_client.api.range_api import RangeApi
from pieces_os_client.api.ranges_api import RangesApi
from pieces_os_client.api.model_api import ModelApi
from pieces_os_client.api.workstream_pattern_engine_api import WorkstreamPatternEngineApi

from pieces_os_client.models.seeded_connector_connection import SeededConnectorConnection
from pieces_os_client.models.seeded_tracked_application import SeededTrackedApplication
from pieces_os_client.wrapper.installation import DownloadModel, PosInstaller


from .copilot import Copilot
from .basic_identifier import BasicAsset,BasicUser
from .streamed_identifiers import AssetSnapshot
from .websockets import (
    ConversationWS,
    HealthWS,
    AssetsIdentifiersWS,
    AuthWS,
    BaseWebsocket,
    LTMVisionWS,
    RangesIdentifiersWS,
    AnchorsIdentifiersWS
)

if TYPE_CHECKING:
    from pieces_os_client.models.fragment_metadata import FragmentMetadata
    from pieces_os_client.models.model import Model

class PiecesClient:
    def __init__(self, seeded_connector: Optional[SeededConnectorConnection] = None,**kwargs):
        self._port = ""
        self.is_pos_stream_running = False
        self._reconnect_on_host_change = kwargs.get("reconnect_on_host_change", True)
        self.models:Dict[str, str] = {} # Maps model_name to the model_id
        self.models_object: list[Model] = []
        self._is_started_runned = False
        self.local_os = platform.system().upper() if platform.system().upper() in ["WINDOWS","LINUX","DARWIN"] else "WEB"
        self.local_os = "MACOS" if self.local_os == "DARWIN" else self.local_os
        self._seeded_connector = seeded_connector or SeededConnectorConnection(
            application=SeededTrackedApplication(
                name = "OPEN_SOURCE",
                platform = self.local_os,
                version = __version__)) 
        self._connect_websockets = kwargs.get("connect_websockets",True)
        self.user = BasicUser(self)   
        self.copilot = Copilot(self)
        self._startup()


    def _startup(self) -> bool:
        if self._is_started_runned:
            return True

        if not self.is_pieces_running(): # Check if PiecesOS is running or not
            return False

        self._is_started_runned = True
        self.host # Make sure no issues in porting scanning and caching the port
        self._tracked_application = self.connector_api.connect(seeded_connector_connection=self._seeded_connector).application
        self.api_client.set_default_header("application",self._tracked_application.id)

        if self._connect_websockets:
            self.conversation_ws = ConversationWS(self)
            self.assets_ws = AssetsIdentifiersWS(self)
            self.user_websocket = AuthWS(self,self.user.on_user_callback)
            self.health_ws = HealthWS(self,lambda x : None)
            self.anchor_ws = AnchorsIdentifiersWS(self)
            self.ltm_vision_ws = LTMVisionWS(self,lambda x : None)
            self.range_ws = RangesIdentifiersWS(self)
            # Start all initilized websockets
            BaseWebsocket.start_all()
        
        self.model_name = "GPT-3.5-turbo Chat Model"
        return True

    @property
    def port(self) -> Union[str,None]:
        if not self._port: # check also if the HealthStream is running
            self.port = self._port_scanning()
        return self._port

    @port.setter
    def port(self, p: Union[str,None]):
        if p != self._port and p is not None:
            self.connect_apis("http://127.0.0.1:" + p)
        self._port = p

    @property
    def host(self) -> str:
        if not self.port:
            return "http://127.0.0.1:39300"
        return "http://127.0.0.1:" + self.port

    @staticmethod
    def _port_scanning() -> str:
        def check_port(port: int) -> Optional[str]:
            try:
                # 1) Quick socket check
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.05)  # Short timeout for local checks
                    if sock.connect_ex(('127.0.0.1', port)) != 0:
                        return None  # If non-zero, the socket isn't open

                # 2) If socket is open, send a single HEAD request
                url = f"http://127.0.0.1:{port}/.well-known/health"
                request = urllib.request.Request(url, method='HEAD')
                with urllib.request.urlopen(request, timeout=0.1) as response:
                    if response.status == 200:
                        return str(port)
            except Exception:
                pass
            return None

        # Scan ports 39300 to 39334 in parallel
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = [executor.submit(check_port, p) for p in range(39300, 39334)]
            for future in as_completed(futures):
                result = future.result()
                if result is not None:
                    return result

        # If no port was found, raise an error
        raise ValueError("PiecesOS is not running")


    @property
    def tracked_application(self):
        self._check_startup()
        return self._tracked_application


    def connect_apis(self,host:str):
        if not host.startswith("http"):
            raise TypeError("Invalid host url\n Host should start with http or https")
        
        self.api_client = ApiClient(Configuration(host))
        self.conversation_message_api = ConversationMessageApi(self.api_client)
        self.conversation_messages_api = ConversationMessagesApi(self.api_client)
        self.conversations_api = ConversationsApi(self.api_client)
        self.conversation_api = ConversationApi(self.api_client)
        self.qgpt_api = QGPTApi(self.api_client)
        self.user_api = UserApi(self.api_client)
        self.assets_api = AssetsApi(self.api_client)
        self.asset_api = AssetApi(self.api_client)
        self.format_api = FormatApi(self.api_client)
        self.connector_api = ConnectorApi(self.api_client)
        self.model_api = ModelApi(self.api_client)
        self.models_api = ModelsApi(self.api_client)
        self.annotation_api = AnnotationApi(self.api_client)
        self.annotations_api = AnnotationsApi(self.api_client)
        self.well_known_api = WellKnownApi(self.api_client)
        self.os_api = OSApi(self.api_client)
        self.allocations_api = AllocationsApi(self.api_client)
        self.linkfy_api = LinkifyApi(self.api_client)
        self.search_api = SearchApi(self.api_client)
        self.tag_api = TagApi(self.api_client)
        self.tags_api = TagsApi(self.api_client)
        self.website_api = WebsiteApi(self.api_client)
        self.websites_api = WebsitesApi(self.api_client)
        self.anchors_api = AnchorsApi(self.api_client)
        self.anchor_api = AnchorApi(self.api_client)
        self.work_stream_pattern_engine_api = WorkstreamPatternEngineApi(self.api_client)
        self.range_api = RangeApi(self.api_client)
        self.ranges_api = RangesApi(self.api_client)

        # Websocket urls
        ws_base_url:str = host.replace('http','ws')
        self.ASSETS_IDENTIFIERS_WS_URL = ws_base_url + "/assets/stream/identifiers"
        self.AUTH_WS_URL = ws_base_url + "/user/stream"
        self.ASK_STREAM_WS_URL = ws_base_url + "/qgpt/stream"
        self.CONVERSATION_WS_URL = ws_base_url + "/conversations/stream/identifiers"
        self.HEALTH_WS_URL = ws_base_url + "/.well-known/stream/health"
        self.ANCHORS_IDENTIFIERS_WS_URL = ws_base_url + "/anchors/stream/identifiers"
        self.LTM_VISION_WS_URL = ws_base_url + "/workstream_pattern_engine/processors/vision/status/stream"
        self.RANGES_IDENTIFIERS_WS_URL = ws_base_url + "/ranges/stream/identifiers"
        if self._reconnect_on_host_change:
            BaseWebsocket.reconnect_all()

    def assets(self):
        """
            Retruns all the assets after the caching process is done
        """
        self.ensure_initialization()
        return [BasicAsset(id) for id in AssetSnapshot.identifiers_snapshot.keys()]

    def asset(self,asset_id):
        self.ensure_initialization()
        return BasicAsset(asset_id)

    @staticmethod
    def create_asset(content:str, metadata:Optional["FragmentMetadata"]=None):
        """
            Create an asset
        """
        return BasicAsset.create(content,metadata)


    def get_models(self) -> Dict[str, str]:
        """
            Returns a dict of the {model_name: model_id}
        """
        if not self.models:
            self.models_object = self.models_api.models_snapshot().iterable
            self.models = {model.name: model.id for model in self.models_object if model.cloud or model.downloaded} # getting the models that are available in the cloud or is downloaded
        return self.models

    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self,model):
        models = self.get_models()
        if model not in models:
            raise ValueError(f"Not a vaild model name, the available models are {', '.join(models.keys())}")
        self._model_name = model
        self.model_id = models[model]

    @property
    def available_models_names(self) -> list:
        """
            Returns all available models names
        """
        return list(self.get_models().keys())

    def ensure_initialization(self):
        """
            Waits for all the assets/conversations and all the started websockets to open
        """
        self._check_startup()
    
    @staticmethod
    def wait_for_cache():
        BaseWebsocket.wait_all()

    @classmethod
    def close(cls):
        """
            Use this when you exit the app
        """ 
        BaseWebsocket.close_all()
        if hasattr(atexit, 'unregister'):
            atexit.unregister(cls.close)

    @property
    def version(self) -> str:
        """
            Returns Pieces OS Version
        """
        self.ensure_initialization()
        return self.well_known_api.get_well_known_version()
 
    @property
    def health(self) -> str:
        """
            Calls the well known health api
            /.well-known/health [GET]
        """
        self.ensure_initialization()
        return self.well_known_api.get_well_known_health()


    def open_pieces_os(self) -> bool:
        """
            Open Pieces OS

            Returns (bool): true if Pieces OS runned successfully else false 
        """
        if self.is_pieces_running(): return True
        if self.local_os == "WINDOWS":
            subprocess.run(["start", "pieces://launch"], shell=True)
        elif self.local_os == "MACOS":
            subprocess.run(["open","pieces://launch"])
        elif self.local_os == "LINUX":
            subprocess.run(["xdg-open","pieces://launch"])
        return self.is_pieces_running(maxium_retries=8)


    def is_pieces_running(self,maxium_retries=1) -> bool:
        """
            Checks if Pieces OS is running or not

            Returns (bool): true if Pieces OS is running 
        """
        for _ in range(maxium_retries):
            try:
                request = urllib.request.Request(self.host + "/.well-known/health")
                with urllib.request.urlopen(request, timeout=0.1) as response:
                    return response.status == 200
            except:
                if maxium_retries != 1:
                    time.sleep(0.5)
        return False

    def _check_startup(self):
        if not self._startup():
            raise ValueError("PiecesClient is not started successfully\nPerhaps Pieces OS is not running")


    def __str__(self) -> str:
        return f"<PiecesClient host={self.host}, pieces_os_status={'Running' if self.is_pieces_running() else 'Not running'}>"


    def __repr__(self) -> str:
        return f"<PiecesClient(host={self.host})>"


    def pool(self,api_call,args):
        """
            call the api async without stopping the main thread
            Create thread pool on first request
            avoids instantiating unused threadpool for blocking clients.
            return the ThreadPool created
        """
        return self.api_client.pool.apply_async(api_call, args)

    def pieces_os_installer(self, callback: Callable[[DownloadModel], None]) -> PosInstaller:
        """
        Installs Pieces OS using the provided callback for download progress updates.

        Args:
            callback (Callable[[DownloadModel], None]): A callback function to receive download progress updates.

        Returns:
            PosInstaller: An instance of PosInstaller handling the installation process.
        """
        return PosInstaller(callback, self._seeded_connector.application.name)

# Register the function to be called on exit
atexit.register(PiecesClient.close)

