import datetime
from typing import TYPE_CHECKING, Optional

from pieces_os_client.models.anonymous_temporal_range import AnonymousTemporalRange
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.os_permissions import OSPermissions
from pieces_os_client.models.os_processing_permissions import OSProcessingPermissions
from pieces_os_client.models.workstream_pattern_engine_status import WorkstreamPatternEngineStatus
from pieces_os_client.models.workstream_pattern_engine_vision_status import WorkstreamPatternEngineVisionStatus
from pieces_os_client.wrapper.basic_identifier.range import BasicRange
from .streamed_identifiers.conversations_snapshot import ConversationsSnapshot


if TYPE_CHECKING:
    from .context import Context
    from pieces_os_client.models.workstream_pattern_engine_vision_calibration import WorkstreamPatternEngineVisionCalibration


QR_CODE_BASE_64 = """data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyBAMAAADsEZWCAAAAKlBMVEUAAAD///+pqan7+/v+/v4QEBDu7u5WVlazs7NOTk5xcXEtLS3g4OCOjo5qPpGPAAAA0klEQVQ4y2NgGIZghZKSxgIgHaQEAV1wmUZBQcEGIB0iCAEScBlFY2NDBSAdJmwMBkIIGUNBiIwIWIswhTJI9pigyADdJgJyGzNIhyOyDMg/N8vLy4uAftERQZYBgYlA5QZAmkkYXaYQaFcqdhlDQUcqypi44JIBug27zJS0tLTToaGhHBgyrEDRPUDZZEF0GRAIE0QPUbiMiIuLIw4Z3HrIkxFBSSHIMo4oqQpJRkR2enl5NTYZYUmsqRgkI04PGWBKxC4DyiXYZZiAKbGbYZgCALuBN/D7PkRzAAAAAElFTkSuQmCC"""
QRCCODE_HIEGHT = 50
QRCCODE_WIDTH = 50

class LongTermMemory:
    ltm_status: Optional[WorkstreamPatternEngineStatus] = None

    def __init__(self, context: "Context"):
        self.context = context
        self.pieces_client = self.context.pieces_client
    
    @property
    def is_enabled(self) -> bool:
        """Checks if the LTM is enabled

        Returns:
            bool: Whether the LTM is enabled
        """
        if self.ltm_status:
            return self.ltm_status.vision.activation is not None if self.ltm_status.vision is not None else False # checking the activation status
        return False
    
    def enable(self, show_message = False):
        """
            This will activate the long term memory (LTM)
            It blocks the main thread until the LTM is enabled and all permissions are enabled
            use PiecesClient.pool to run it in spearate thread

            Args:
                show_message (bool, optional): Defaults to False.
                it show_message is True it will ask the user to enable the permissions if it is not
            Raises:
                PermissionError: If LTM if Permission is not enabled
        """
        if self.is_enabled:
            return

        perms = self.pieces_client.os_api.os_permissions()
        missing_permissions = []
        
        if not perms.processing.vision:
            missing_permissions.append("vision")
        
        if not perms.processing.accessibility:
            missing_permissions.append("accessibility")
        
        if missing_permissions and show_message:
            out = self.pieces_client.os_api.os_permissions_request(
                os_permissions=OSPermissions(
                    processing=OSProcessingPermissions(
                        **{perm: True for perm in missing_permissions}
                    )
                )
            )
            missing_permissions.clear()
            if not out.processing.vision:
                missing_permissions.append("vision")
            if not out.processing.accessibility:
                missing_permissions.append("accessibility")

        if missing_permissions:
            raise PermissionError(f"{', '.join(missing_permissions).capitalize()} is not enabled")

        state = WorkstreamPatternEngineStatus(
            vision=WorkstreamPatternEngineVisionStatus(
                activation=AnonymousTemporalRange(
                    continuous=True
                )
            )
        )
        self.pieces_client.work_stream_pattern_engine_api.workstream_pattern_engine_processors_vision_activate(state)
    
    def pause(self, until: Optional[datetime.datetime] = None):
        """
        This will pause the long term memory (LTM)

        Args:
            until (Optional[datetime.datetime], optional): Until when the LTM will be paused. Defaults to None (Until tunned back on).
        """
        if until:
            workstream_pattern_engine_status=WorkstreamPatternEngineStatus(
                vision=WorkstreamPatternEngineVisionStatus(
                    deactivation = AnonymousTemporalRange(
                        to = GroupedTimestamp(
                            value = until,
                        )
                    ),
                )
            )
        else:
            workstream_pattern_engine_status=WorkstreamPatternEngineStatus(
                vision=WorkstreamPatternEngineVisionStatus(
                    deactivation = AnonymousTemporalRange(
                        continuous=True
                    ),
                )
            )
        self.pieces_client.work_stream_pattern_engine_api.workstream_pattern_engine_processors_vision_deactivate(workstream_pattern_engine_status)

    def get_qrcode(self) -> str:
        """
        This will return the qrcode that needs to be placed on the corner of the Copilot window to avoid multiple capture context capture

        If you want to download the image it self you can run the following script

        ```python
        image_data = base64.b64decode(ltm.get_qrcode())
        output_file_path = "qrcode.png"
        with open(output_file_path, "wb") as file:
            file.write(image_data)
        ```

        Returns:
            str: The qrcode png image base64
        """
        return QR_CODE_BASE_64

    def capture(self) -> "WorkstreamPatternEngineVisionCalibration":
        """
        This will capture the qrcode that you got from `get_qrcode` for the LTM engine to ignore the window to avoid multiple context captures
        that will enhance the LTM quality

        Returns:
            WorkstreamPatternEngineVisionCalibration: The Captured window details
        """
        return self.pieces_client.work_stream_pattern_engine_api.workstream_pattern_engine_processors_vision_calibration_capture()


    def chat_enable_ltm(self):
        """
        This will enable the chat LTM
        """
        chat = self.context.copilot.chat
        if not chat:
            chat = self.context.copilot.create_chat("New Conversation")
        chat.associate_range(BasicRange.create())
        conv = self.pieces_client.conversation_api.conversation_get_specific_conversation(chat.id) # Update the local cache
        ConversationsSnapshot.identifiers_snapshot[conv.id] = conv

    def chat_disable_ltm(self):
        """
        This will disable the chat LTM
        """
        chat = self.context.copilot.chat
        if not chat:
            return
        for range in chat.ranges:
            range.disassociate_chat(chat)

    @property
    def is_chat_ltm_enabled(self) -> bool:
        """
        This will check if the chat LTM is enabled

        Returns:
            bool: True if the chat LTM is enabled
        """
        if not self.context.copilot.chat:
            return False
        return len(self.context.copilot.chat.ranges) > 0