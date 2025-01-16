from typing import Optional, List, TYPE_CHECKING

from ..streamed_identifiers import ConversationsSnapshot
from .basic import Basic

from pieces_os_client.models.conversation import Conversation
from pieces_os_client.models.annotation_type_enum import AnnotationTypeEnum


if TYPE_CHECKING:
    from . import BasicMessage,BasicAnnotation,BasicWebsite, BasicAnchor, BasicAsset, BasicRange

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

    def messages(self) -> List["BasicMessage"]:
        """
        Retrieves the messages in the conversation.

        Returns:
            A list of BasicMessage instances representing the messages in the conversation.
        """
        from .message import BasicMessage
        out = []
        for message_id, index in (self.conversation.messages.indices or {}).items():
            if index == -1:  # Deleted message
                continue
            out.append(BasicMessage(ConversationsSnapshot.pieces_client,message_id))
        return out


    @property
    def annotations(self) -> List["BasicAnnotation"]:
        """
        Gets the annotations of the conversation.

        Returns:
            The BasicAnnotation of the conversation, or None if not available.
        """
        from . import BasicAnnotation
        return self._from_indices(
            getattr(self.conversation.annotations, "indices", {}),
            lambda id:BasicAnnotation.from_id(ConversationsSnapshot.pieces_client,id)
        )

    @property
    def summary(self)-> Optional[str]:
        annotations = self.annotations
        if not annotations:
            return
        d = None
        for annotation in annotations:
            if annotation.type == AnnotationTypeEnum.SUMMARY:
                d = annotation
        
        return d.raw_content if d else None


    def delete(self):
        """
        Deletes the conversation.
        """
        ConversationsSnapshot.pieces_client.conversations_api.conversations_delete_specific_conversation(self.id)

    @property
    def websites(self) -> List["BasicWebsite"]:
        from . import BasicWebsite
        return self._from_indices(
            getattr(self.conversation.websites,"indices",{}),
            lambda id:BasicWebsite.from_id(ConversationsSnapshot.pieces_client,id)
        )
    
    def associate_asset(self, asset: "BasicAsset"):
        """
        Associates an asset with the conversation.

        Args:
            asset: The asset to associate.
        """
        ConversationsSnapshot.pieces_client.conversation_api.conversation_associate_asset(self.id, asset.id)

    def disassociate_asset(self, asset: "BasicAsset"):
        """
        Disassociates an asset from the conversation.

        Args:
            asset: The asset to disassociate.
        """
        ConversationsSnapshot.pieces_client.conversation_api.conversation_disassociate_asset(self.id, asset.id)

    def associate_message(self, message: "BasicMessage"):
        """
        Associates a message with the conversation.

        Args:
            message: The message to associate.
        """
        ConversationsSnapshot.pieces_client.conversation_api.conversation_grounding_messages_associate_message(self.id, message.id)

    def disassociate_message(self, message: "BasicMessage"):
        """
        Disassociates a message from the conversation.

        Args:
            message: The message to disassociate.
        """
        ConversationsSnapshot.pieces_client.conversation_api.conversation_grounding_messages_disassociate_message(self.id, message.id)

    def associate_anchor(self, anchor: "BasicAnchor"):
        """
        Associates an anchor with the conversation.

        Args:
            anchor: The anchor to associate.
        """
        ConversationsSnapshot.pieces_client.conversation_api.conversation_associate_anchor(self.id, anchor.id)

    def disassociate_anchor(self, anchor: "BasicAnchor"):
        """
        Disassociates an anchor from the conversation.

        Args:
            anchor: The anchor to disassociate.
        """
        ConversationsSnapshot.pieces_client.conversation_api.conversation_disassociate_anchor(self.id, anchor.id)
    
    @property
    def is_ltm_enabled(self) -> bool:
        """
        Checks if LTM is enabled for this conversation.

        Returns:
            True if LTM is enabled, False otherwise.
        """
        temporal = self.conversation.grounding.temporal
        if temporal and temporal.workstreams and temporal.workstreams.indices:
            for idx in temporal.workstreams.indices:
                k,v = idx.items()
                if v == 1:
                    return True
        return False

    def disassociate_range(self, range: "BasicRange"):
        """
        Disassociates a range from the conversation.

        Args:
            range: The range to disassociate.
        """
        ConversationsSnapshot.pieces_client.conversation_api.conversation_disassociate_grounding_temporal_range_workstream(self.id, range.id)

    def associate_range(self, range: "BasicRange"):
        """
        Associates a range with the conversation.

        Args:
            range: The range to associate.
        """
        ConversationsSnapshot.pieces_client.conversation_api.conversation_associate_grounding_temporal_range_workstream(self.id, range.id)

    @property
    def ranges(self) -> List["BasicRange"]:
        from . import BasicRange
        temporal = self.conversation.grounding.temporal if self.conversation.grounding else None
        if not temporal or not temporal.workstreams or not temporal.workstreams.indices:
            return []
        return self._from_indices(
            temporal.workstreams.indices,
            lambda id:BasicRange(id)
        )

    @staticmethod
    def _edit_conversation(conversation):
        """
        Edits the conversation.

        Args:
            conversation: The conversation to edit.
        """
        ConversationsSnapshot.pieces_client.conversation_api.conversation_update(False, conversation)


