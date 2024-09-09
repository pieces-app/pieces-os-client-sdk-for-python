from typing import TYPE_CHECKING, List, Optional, Generator
from pieces_os_client import (SeededConversation,
    QGPTStreamInput,
    RelevantQGPTSeeds,
    QGPTQuestionInput,
    QGPTStreamOutput,
    QGPTStreamEnum,
    QGPTQuestionOutput)
from pieces_os_client.models.qgpt_prompt_pipeline import QGPTPromptPipeline

from .context import Context
from .basic_identifier.chat import BasicChat
from .streamed_identifiers.conversations_snapshot import ConversationsSnapshot
from .websockets import AskStreamWS
import queue


if TYPE_CHECKING:
    from .client import PiecesClient


class Copilot:
    """
    A class to interact with the Pieces Copilot SDK for managing conversations and streaming QGPT responses.
    """

    def __init__(self, pieces_client: "PiecesClient"):
        """
        Initializes the Copilot instance.

        Args:
            pieces_client: The client instance to interact with the Pieces API.
        """
        self.pieces_client = pieces_client
        self._on_message_queue = queue.Queue()
        self.ask_stream_ws = AskStreamWS(self.pieces_client, self._on_message_queue.put)
        self.context = Context(pieces_client)
        self._chat = None
        self._chat_id = None

    def stream_question(self,
            query: str,
            pipeline: Optional[QGPTPromptPipeline] = None
            ) -> Generator[QGPTStreamOutput, None, None]:
        """
        Asks a question to the QGPT model and streams the responses.
        by default it will create a new conversation and always use it in the ask.
        You can always change the conversation in copilot.chat = BasicChat(chat_id="YOU ID GOES HERE")

        Args:
            query (str): The question to ask.
            pipeline (Optional[QGPTPromptPipeline]): the pipeline to use.

        Yields:
            QGPTStreamOutput: The streamed output from the QGPT model.
        """
        self.pieces_client._check_startup()
        relevant = self.context._relevance_api(query) if self.context._check_relevant_existance else RelevantQGPTSeeds(iterable=[])
        self.ask_stream_ws.send_message(
            QGPTStreamInput(
                question=QGPTQuestionInput(
                    relevant=relevant,
                    query=query,
                    application=self.pieces_client.tracked_application.id,
                    model=self.pieces_client.model_id,
                    pipeline=pipeline
                ),
                conversation=self._chat_id,
            )
        )
        return self._return_on_message()

    def _return_on_message(self):
        while True:
            message: QGPTStreamOutput = self._on_message_queue.get()
            if message.status != QGPTStreamEnum.IN_MINUS_PROGRESS:  # Loop only while in progress
                yield message
                self.chat = BasicChat(message.conversation)  # Save the conversation
                break
            yield message


    def question(self,
        query:str, 
        relevant_qgpt_seeds: RelevantQGPTSeeds = RelevantQGPTSeeds(iterable=[]),
        pipeline:Optional[QGPTPromptPipeline]=None
        ) -> QGPTQuestionOutput:
        """
        Asks a question to the QGPT model and return the responses,
        Note: the question is not a part of any conversation.

        Args:
            query (str): The question to ask.
            relevant_qgpt_seeds (RelevantQGPTSeeds): Context to the model .
            pipeline (Optional[QGPTPromptPipeline]): the pipeline to use.

        returns:
            QGPTQuestionOutput: The streamed output from the QGPT model.
        """
        self.pieces_client._check_startup()
        gpt_input = QGPTQuestionInput(
            query = query,
            model = self.pieces_client.model_id,
            application = self.pieces_client.tracked_application.id,
            pipeline=pipeline,
            relevant = relevant_qgpt_seeds
        )

        return self.pieces_client.qgpt_api.question(gpt_input)

    def chats(self) -> List[BasicChat]:
        """
        Retrieves a list of all chat identifiers.

        Returns:
            list[BasicChat]: A list of BasicChat instances representing the chat identifiers.
        """
        self.pieces_client.ensure_initialization()
        return [BasicChat(id) for id in ConversationsSnapshot.identifiers_snapshot]

    @property
    def chat(self) -> Optional[BasicChat]:
        """
        Gets the current conversation being used in the copilot.

        Returns:
            Optional[BasicChat]: The current chat instance or None if no chat is set.
        """
        return self._chat

    @chat.setter
    def chat(self, chat: Optional[BasicChat]):
        """
        Sets the current conversation to be used in the copilot.

        Args:
            chat (Optional[BasicChat]): The chat instance to set.
            use chat = None if you want to create a new conversation on asking
        """
        self._chat = chat
        self.context.clear() # clear the context on changing the conversation
        self._chat_id = chat.id if chat else None


    def create_chat(self, name:Optional[str]=None):
        """
            Creates a New Chat and change the current Copilot chat state to the new generated one
        """
        new_conversation = self.pieces_client.conversations_api.conversations_create_specific_conversation(
            seeded_conversation={
                'name': name,
                'type': 'COPILOT',
            }
        )

        ConversationsSnapshot.identifiers_snapshot[new_conversation.id] = new_conversation # Make sure to update the cache
        self.chat = BasicChat(new_conversation.id)

        return self.chat

