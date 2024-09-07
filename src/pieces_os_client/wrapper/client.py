from pieces_os_client import (
    ApiClient,
    Configuration,
    ConversationApi,
    ConversationMessageApi,
    ConversationMessagesApi,
    ConversationsApi,
    QGPTApi,
    UserApi,
    FormatApi,
    ConnectorApi,
    SeededConnectorConnection,
    SeededTrackedApplication,
    AssetApi,
    AssetsApi,
    FragmentMetadata,
    ModelsApi,
    AnnotationApi,
    LinkifyApi,
    WellKnownApi,
    OSApi,
    AllocationsApi,
    SearchApi,
    __version__
)
import socket
from typing import Optional,Dict
import platform
import atexit
import subprocess
from urllib.parse import urlparse

from .copilot import Copilot
from .basic_identifier import BasicAsset,BasicUser
from .streamed_identifiers import AssetSnapshot
from .websockets import *


def _check_startup(func):
    def wrapper(self,*args, **kwargs):
        if not self._is_started_runned: 
            if self.is_pos_running():
                self._startup()
            else:
                raise ValueError("PiecesClient is not started successfully\nPerhaps Pieces OS is not running")
        return func(*args, **kwargs)
    return wrapper

class PiecesClient:
    def __init__(self, host:str="", seeded_connector: Optional[SeededConnectorConnection] = None,**kwargs):
        if not host:
            host = "http://localhost:5323" if 'Linux' in platform.platform() else "http://localhost:1000"

        self.host = host
        self._is_started_runned = False
        self.local_os = platform.system().upper() if platform.system().upper() in ["WINDOWS","LINUX","DARWIN"] else "WEB"
        self.local_os = "MACOS" if self.local_os == "DARWIN" else self.local_os
        self._seeded_connector = seeded_connector or SeededConnectorConnection(
            application=SeededTrackedApplication(
                name = "OPEN_SOURCE",
                platform = self.local_os,
                version = __version__)) 
        self._connect_websockets = kwargs.get("connect_wesockets",True)
        self._user = BasicUser(self)   
        self._copilot = Copilot(self)

        if self.is_pos_running():
            self._startup()


    def _startup(self):
        self.tracked_application = self.connector_api.connect(seeded_connector_connection=self._seeded_connector).application

        if self._connect_websockets:
            self.conversation_ws = ConversationWS(self)
            self.assets_ws = AssetsIdentifiersWS(self)
            self.user_websocket = AuthWS(self,self.user.on_user_callback)
            # Start all initilized websockets
            BaseWebsocket.start_all()
        
        self.models = None
        self.model_name = "GPT-3.5-turbo Chat Model"
        self._is_started_runned = True


    @_check_startup
    @property
    def user(self):
        return self._user

    @_check_startup
    @property
    def copilot(self):
        return self._copilot

    @property
    def host(self) -> str:
        return self._host

    @host.setter
    def host(self,host):
        if not host.startswith("http"):
            raise TypeError("Invalid host url\n Host should start with http or https")

        parsed_url = urlparse(host)
        self.hostname = parsed_url.hostname
        self.port = parsed_url.port

        self._host = host
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
        self.models_api = ModelsApi(self.api_client)
        self.annotation_api = AnnotationApi(self.api_client)
        self.well_known_api = WellKnownApi(self.api_client)
        self.os_api = OSApi(self.api_client)
        self.allocations_api = AllocationsApi(self.api_client)
        self.linkfy_api = LinkifyApi(self.api_client)
        self.search_api = SearchApi(self.api_client)

        # Websocket urls
        ws_base_url:str = host.replace('http','ws')
        self.ASSETS_IDENTIFIERS_WS_URL = ws_base_url + "/assets/stream/identifiers"
        self.AUTH_WS_URL = ws_base_url + "/user/stream"
        self.ASK_STREAM_WS_URL = ws_base_url + "/qgpt/stream"
        self.CONVERSATION_WS_URL = ws_base_url + "/conversations/stream/identifiers"
        self.HEALTH_WS_URL = ws_base_url + "/.well-known/stream/health"

    @_check_startup
    def assets(self):
        self.ensure_initialization()
        return [BasicAsset(id) for id in AssetSnapshot.identifiers_snapshot.keys()]

    @_check_startup
    def asset(self,asset_id):
        self.ensure_initialization()
        return BasicAsset(asset_id)

    @_check_startup
    @staticmethod
    def create_asset(content:str,metadata:Optional[FragmentMetadata]=None):
        return BasicAsset.create(content,metadata)

    @_check_startup
    def get_models(self) -> Dict[str, str]:
        if self.models:
            return self.models
        api_response = self.models_api.models_snapshot()
        models = {model.name: model.id for model in api_response.iterable if model.cloud or model.downloaded} # getting the models that are available in the cloud or is downloaded
        self.models = models
        return models

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
        return list(self.get_models().keys())

    def ensure_initialization(self):
        """
            Waits for all the assets/conversations and all the started websockets to open
        """
        BaseWebsocket.wait_all()

    def close(self):
        """
            Use this when you exit the app
        """
        BaseWebsocket.close_all()

    @_check_startup
    @property
    def version(self) -> str:
        """
            Returns Pieces OS Version
        """
        return self.well_known_api.get_well_known_version()
    
    @_check_startup  
    @property
    def health(self) -> str:
        """
            Returns True Pieces OS health is ok else False
        """
        return self.well_known_api.get_well_known_health()

    def open_pieces_os(self) -> bool:
        """
            Open Pieces OS

            Returns (bool): true if Pieces OS runned successfully else false 
        """
        if self.local_os == "WINDOWS":
            subprocess.run(["start", "pieces://launch"], shell=True)
        elif self.local_os == "MACOS":
            subprocess.run(["open","pieces://launch"])
        elif self.local_os == "LINUX":
            subprocess.run(["xdg-open","pieces://launch"])
        return self.is_pos_running(timeout=8) # Wait maxium 8 sec

    def is_pos_running(self,timeout=1) -> bool:
        """
            Checks if Pieces OS is running or not
        """
        try:
            # Create a socket object
            with socket.create_connection((self.hostname + "/.well-known/health",self.port), timeout=timeout):
                return True
        except (socket.timeout, socket.error):
            return False


# Register the function to be called on exit
atexit.register(BaseWebsocket.close_all)

