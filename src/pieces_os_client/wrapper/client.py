from pieces_os_client import (
    ApiClient,
    Application,
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
    AnnotationApi
)
from typing import Optional,Dict
import platform
import atexit

from .copilot import Copilot
from .basic_identifier import BasicAsset
from .streamed_identifiers import AssetSnapshot
from .websockets import *

class PiecesClient:
    def __init__(self, host:str="",config: dict={}, seeded_connector: Optional[SeededConnectorConnection] = None):
        if host:
            self.host = host
        else:
            self.host = "http://localhost:5323" if 'Linux' in platform.platform() else "http://localhost:1000"

        connect_websockets= True
        if "connect_websockets" in config:
            connect_websockets = config["connect_websockets"]
            del config["connect_websockets"]

        self.config = Configuration(**config)

        self.api_client = ApiClient(self.config)

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

        # Websocket urls
        if 'http' not in self.host:
            raise TypeError("Invalid host url\n Host should start with http or https")
        ws_base_url:str = self.host.replace('http','ws')
        
        self.ASSETS_IDENTIFIERS_WS_URL = ws_base_url + "/assets/stream/identifiers"
        self.AUTH_WS_URL = ws_base_url + "/user/stream"
        self.ASK_STREAM_WS_URL = ws_base_url + "/qgpt/stream"
        self.CONVERSATION_WS_URL = ws_base_url + "/conversations/stream/identifiers"
        self.HEALTH_WS_URL = ws_base_url + "/.well-known/stream/health"

        local_os = platform.system().upper() if platform.system().upper() in ["WINDOWS","LINUX","DARWIN"] else "WEB"
        local_os = "MACOS" if local_os == "DARWIN" else local_os
        seeded_connector = seeded_connector or SeededConnectorConnection(
            application=SeededTrackedApplication(
                name = "OPEN_SOURCE",
                platform = local_os,
                version = "0.0.1"))

        self.tracked_application = self.connector_api.connect(seeded_connector_connection=seeded_connector).application

        if connect_websockets:
            self.conversation_ws = ConversationWS(self)
            self.assets_ws = AssetsIdentifiersWS(self)

            # Start all initilized websockets
            BaseWebsocket.start_all()
        
        self.models = None
        self.model_name = "GPT-3.5-turbo Chat Model"


    def assets(self):
        self.ensure_initialization()
        return [BasicAsset(id) for id in AssetSnapshot.identifiers_snapshot.keys()]

    def asset(self,asset_id):
        self.ensure_initialization()
        return BasicAsset(asset_id)

    @staticmethod
    def create_asset(content:str,metadata:Optional[FragmentMetadata]=None):
        return BasicAsset.create(content,metadata)

    def get_user_profile_picture(self) -> Optional[str]:
        try:
            user_res = self.user_api.user_snapshot()
            return user_res.user.picture or None
        except Exception as error:
            print(f'Error getting user profile picture: {error}')
            return None

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

    @property
    def copilot(self):
        return Copilot(self)

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

# Register the function to be called on exit
atexit.register(BaseWebsocket.close_all)

