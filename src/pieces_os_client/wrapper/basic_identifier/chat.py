from pieces_os_client import Conversation,Annotations
from ..streamed_identifiers import ConversationsSnapshot
from typing import Optional, List
from .basic import Basic
from .message import BasicMessage

class BasicChat(Basic):
    """
    A class to represent a basic chat, initialized with a conversation ID.
    """
    @property
    def conversation(self) -> Conversation:
        conversation = ConversationsSnapshot.identifiers_snapshot.get(self._id)
        if not conversation:
            raise ValueError("Conversation not found")
        return conversation

    @property
    def id(self) -> str:
        """
        Gets the ID of the conversation.

        Returns:
            The ID of the conversation.
        """
        return self.conversation.id

    @property
    def name(self) -> str:
        """
        Gets the name of the conversation.

        Returns:
            The name of the conversation, or "New Conversation" if the name is not set.
        """
        return self.conversation.name if self.conversation.name else "New Conversation"

    @name.setter
    def name(self, name):
        """
        Sets the name of the conversation.

        Args:
            name: The new name of the conversation.
        """
        self.conversation.name = name
        self._edit_conversation(self.conversation)

    def messages(self) -> List[BasicMessage]:
        """
        Retrieves the messages in the conversation.

        Returns:
            A list of BasicMessage instances representing the messages in the conversation.
        """
        out = []
        for message_id, index in (self.conversation.messages.indices or {}).items():
            if index == -1:  # Deleted message
                continue
            out.append(BasicMessage(ConversationsSnapshot.pieces_client,message_id))
        return out


    @property
    def annotations(self) -> Optional[Annotations]:
        """
        Gets the annotations of the conversation.

        Returns:
            The annotations of the conversation, or None if not available.
        """
        return getattr(self.conversation.annotations, "iterable", None)

    def delete(self):
        """
        Deletes the conversation.
        """
        ConversationsSnapshot.pieces_client.conversations_api.conversations_delete_specific_conversation(self.id)

    @staticmethod
    def _edit_conversation(conversation):
        """
        Edits the conversation.

        Args:
            conversation: The conversation to edit.
        """
        ConversationsSnapshot.pieces_client.conversation_api.conversation_update(False, conversation)


