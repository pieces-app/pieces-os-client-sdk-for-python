import datetime
from typing import TYPE_CHECKING, Optional

from pieces_os_client.models.anonymous_temporal_range import AnonymousTemporalRange
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.os_permissions import OSPermissions
from pieces_os_client.models.os_processing_permissions import OSProcessingPermissions
from pieces_os_client.models.workstream_pattern_engine_status import WorkstreamPatternEngineStatus
from pieces_os_client.models.workstream_pattern_engine_vision_status import WorkstreamPatternEngineVisionStatus


if TYPE_CHECKING:
    from .context import Context
    from pieces_os_client.models.workstream_pattern_engine_vision_calibration import WorkstreamPatternEngineVisionCalibration


QR_CODE_BASE_64 = """data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAAEsCAIAAAD2HxkiAAAMP2lDQ1BJQ0MgUHJvZmlsZQAASImVVwdYU8kWnluSkJDQAghICb0JIjWAlBBaAOndRkgChBJjIKjY0UUF1y4WsKGrIoqdZkfsLIoN+2JBQVkXC3blTQrouq98b75v7vz3nzP/OXPuzL13AFA/yRWLc1ENAPJEBZLYkABGckoqg9QNMEACVOAIvLi8fDErOjoCwDLY/r28uwkQWXvNQab1z/7/WjT5gnweAEg0xOn8fF4exIcAwCt5YkkBAEQZbz6lQCzDsAJtCQwQ4oUynKnAlTKcrsD75DbxsWyIWwBQoXK5kkwA1K5AnlHIy4Qaan0QO4n4QhEA6gyIffPyJvEhToPYBtqIIZbpM9N/0Mn8m2b6kCaXmzmEFXORF5VAYb44lzvt/0zH/y55udJBH1awUrMkobGyOcO83cqZFC7DVIh7RemRURBrQfxByJfbQ4xSsqShCQp71JCXz4Y5A7oQO/G5geEQG0IcLMqNjFDy6RnCYA7EcIWgU4UFnHiI9SBeKMgPilPabJZMilX6QusyJGyWkj/Plcj9ynw9kOYksJT6r7MEHKU+plaUFZ8EMQVii0JhYiTEahA75ufEhSttRhdlsSMHbSTSWFn8FhDHCkQhAQp9rDBDEhyrtC/Nyx+cL7Y5S8iJVOIDBVnxoYr8YC08rjx+OBfsikDEShjUEeQnRwzOhS8IDFLMHesWiBLilDofxAUBsYqxOEWcG620x80EuSEy3gxi1/zCOOVYPLEALkiFPp4hLoiOV8SJF2Vzw6IV8eDLQARgg0DAAFJY08EkkA2Ebb31vfBO0RMMuEACMoEAOCiZwRFJ8h4RvMaBIvAnRAKQPzQuQN4rAIWQ/zrEKq4OIEPeWygfkQOeQpwHwkEuvJfKR4mGvCWCJ5AR/sM7F1YejDcXVln/v+cH2e8MCzIRSkY66JGhPmhJDCIGEkOJwURb3AD3xb3xCHj1h9UZZ+Keg/P4bk94SmgnPCLcIHQSbk8UFkt+inIM6IT6wcpcpP+YC9wKarrhAbgPVIfKuC5uABxwV+iHhftBz26QZSvjlmWF8ZP232bww9NQ2pGdyCh5GNmfbPPzSDU7NbchFVmuf8yPItb0oXyzh3p+9s/+Ift82Ib/bIktxA5i57BT2AXsKFYPGNgJrAFrxY7J8NDqeiJfXYPeYuXx5EAd4T/8DT5ZWSbznWqcepy+KPoKBFNl72jAniSeJhFmZhUwWPCLIGBwRDzHEQxnJ2dXAGTfF8Xr602M/LuB6LZ+5+b9AYDPiYGBgSPfubATAOz3gNu/8Ttnw4SfDlUAzjfypJJCBYfLLgT4llCHO00fGANzYAPn4wzcgTfwB0EgDESBeJACJsDos+A6l4ApYAaYC0pAGVgGVoP1YBPYCnaCPeAAqAdHwSlwFlwCV8ANcBeuni7wAvSBd+AzgiAkhIbQEX3EBLFE7BFnhIn4IkFIBBKLpCBpSCYiQqTIDGQeUoasQNYjW5BqZD/SiJxCLiDtyG3kIdKDvEY+oRhKRbVRI9QKHYkyURYajsaj49FMdDJahM5Hl6Br0Sp0N1qHnkIvoTfQTvQF2o8BTBXTxUwxB4yJsbEoLBXLwCTYLKwUK8eqsFqsCT7na1gn1ot9xIk4HWfgDnAFh+IJOA+fjM/CF+Pr8Z14Hd6CX8Mf4n34NwKNYEiwJ3gROIRkQiZhCqGEUE7YTjhMOAP3UhfhHZFI1CVaEz3gXkwhZhOnExcTNxD3Ek8S24mPif0kEkmfZE/yIUWRuKQCUglpHWk36QTpKqmL9EFFVcVExVklWCVVRaRSrFKuskvluMpVlWcqn8kaZEuyFzmKzCdPIy8lbyM3kS+Tu8ifKZoUa4oPJZ6STZlLWUuppZyh3KO8UVVVNVP1VI1RFarOUV2ruk/1vOpD1Y9ULaodlU0dR5VSl1B3UE9Sb1Pf0Gg0K5o/LZVWQFtCq6adpj2gfVCjqzmqcdT4arPVKtTq1K6qvVQnq1uqs9QnqBepl6sfVL+s3qtB1rDSYGtwNWZpVGg0anRo9GvSNUdpRmnmaS7W3KV5QbNbi6RlpRWkxdear7VV67TWYzpGN6ez6Tz6PPo2+hl6lzZR21qbo52tXaa9R7tNu09HS8dVJ1Fnqk6FzjGdTl1M10qXo5uru1T3gO5N3U/DjIaxhgmGLRpWO+zqsPd6w/X89QR6pXp79W7ofdJn6Afp5+gv16/Xv2+AG9gZxBhMMdhocMagd7j2cO/hvOGlww8Mv2OIGtoZxhpON9xq2GrYb2RsFGIkNlpndNqo11jX2N8423iV8XHjHhO6ia+J0GSVyQmT5wwdBouRy1jLaGH0mRqahppKTbeYtpl+NrM2SzArNttrdt+cYs40zzBfZd5s3mdhYjHGYoZFjcUdS7Il0zLLco3lOcv3VtZWSVYLrOqtuq31rDnWRdY11vdsaDZ+NpNtqmyu2xJtmbY5thtsr9ihdm52WXYVdpftUXt3e6H9Bvv2EYQRniNEI6pGdDhQHVgOhQ41Dg8ddR0jHIsd6x1fjrQYmTpy+chzI785uTnlOm1zujtKa1TYqOJRTaNeO9s585wrnK+70FyCXWa7NLi8crV3FbhudL3lRncb47bArdntq7uHu8S91r3Hw8IjzaPSo4OpzYxmLmae9yR4BnjO9jzq+dHL3avA64DXX94O3jneu7y7R1uPFozeNvqxj5kP12eLT6cvwzfNd7Nvp5+pH9evyu+Rv7k/33+7/zOWLSubtZv1MsApQBJwOOA924s9k30yEAsMCSwNbAvSCkoIWh/0INgsODO4JrgvxC1kesjJUEJoeOjy0A6OEYfHqeb0hXmEzQxrCaeGx4WvD38UYRchiWgag44JG7NyzL1Iy0hRZH0UiOJErYy6H20dPTn6SAwxJjqmIuZp7KjYGbHn4uhxE+N2xb2LD4hfGn83wSZBmtCcqJ44LrE68X1SYNKKpM7kkckzky+lGKQIUxpSSamJqdtT+8cGjV09tmuc27iScTfHW4+fOv7CBIMJuROOTVSfyJ14MI2QlpS2K+0LN4pbxe1P56RXpvfx2Lw1vBd8f/4qfo/AR7BC8CzDJ2NFRnemT+bKzJ4sv6zyrF4hW7he+Co7NHtT9vucqJwdOQO5Sbl781Ty0vIaRVqiHFHLJONJUye1i+3FJeLOyV6TV0/uk4RLtucj+ePzGwq04Y98q9RG+ov0YaFvYUXhhymJUw5O1Zwqmto6zW7aomnPioKLfpuOT+dNb55hOmPujIczWTO3zEJmpc9qnm0+e/7srjkhc3bOpczNmft7sVPxiuK385LmNc03mj9n/uNfQn6pKVErkZR0LPBesGkhvlC4sG2Ry6J1i76V8ksvljmVlZd9WcxbfPHXUb+u/XVgScaStqXuSzcuIy4TLbu53G/5zhWaK4pWPF45ZmXdKsaq0lVvV09cfaHctXzTGsoa6ZrOtRFrG9ZZrFu27sv6rPU3KgIq9lYaVi6qfL+Bv+HqRv+NtZuMNpVt+rRZuPnWlpAtdVVWVeVbiVsLtz7dlrjt3G/M36q3G2wv2/51h2hH587YnS3VHtXVuwx3La1Ba6Q1PbvH7b6yJ3BPQ61D7Za9unvL9oF90n3P96ftv3kg/EDzQebB2kOWhyoP0w+X1iF10+r66rPqOxtSGtobwxqbm7ybDh9xPLLjqOnRimM6x5Yepxyff3zgRNGJ/pPik72nMk89bp7YfPd08unrLTEtbWfCz5w/G3z29DnWuRPnfc4fveB1ofEi82L9JfdLda1urYd/d/v9cJt7W91lj8sNVzyvNLWPbj9+1e/qqWuB185e51y/dCPyRvvNhJu3OsZ1dN7i3+q+nXv71Z3CO5/vzrlHuFd6X+N++QPDB1V/2P6xt9O989jDwIetj+Ie3X3Me/ziSf6TL13zn9Kelj8zeVbd7dx9tCe458rzsc+7XohffO4t+VPzz8qXNi8P/eX/V2tfcl/XK8mrgdeL3+i/2fHW9W1zf3T/g3d57z6/L/2g/2HnR+bHc5+SPj37POUL6cvar7Zfm76Ff7s3kDcwIOZKuPJfAQxWNCMDgNc7AKClAECH5zPKWMX5T14QxZlVjsB/woozory4A1AL/99jeuHfTQcA+7bB4xfUVx8HQDQNgHhPgLq4DNXBs5r8XCkrRHgO2Bz9NT0vHfybojhz/hD3zy2QqbqCn9t/AT0wfIq1amAYAAAAOGVYSWZNTQAqAAAACAABh2kABAAAAAEAAAAaAAAAAAACoAIABAAAAAEAAAEsoAMABAAAAAEAAAEsAAAAAPuooN0AAAehSURBVHgB7dVRbgVFEANAFnH/Kz84QkswyN2ufK8m7nKs/PGHHwIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgkCzwZYb7/X6Bwb4vkSvTKrC+fyJlNvhnJpZUBHoEjLCna5eGChhhaDFi9QgYYU/XLg0VMMLQYsTqETDCnq5dGipghKHFiNUjYIQ9Xbs0VMAIQ4sRq0fACHu6dmmogBGGFiNWj4AR9nTt0lABIwwtRqweASPs6dqloQJGGFqMWD0CRtjTtUtDBYwwtBixegSMsKdrl4YKGGFoMWL1CBhhT9cuDRUwwtBixOoRMMKerl0aKmCEocWI1SNghD1duzRUwAhDixGrR8AIe7p2aaiAEYYWI1aPgBH2dO3SUAEjDC1GrB4BI+zp2qWhAkYYWoxYPQJG2NO1S0MFjDC0GLF6BIywp2uXhgoYYWgxYvUIGGFP1y4NFTDC0GLE6hEwwp6uXRoqYIShxYjVI2CEPV27NFTACEOLEatHwAh7unZpqIARhhYjVo+AEfZ07dJQASMMLUasHgEj7OnapaECRhhajFg9AkbY07VLQwWMMLQYsXoEvp5T//2lv9/v3z/yn7/wfYklspoX7T/h3MqXBJ4IGOETVo8SmAsY4dzKlwSeCBjhE1aPEpgLGOHcypcEnggY4RNWjxKYCxjh3MqXBJ4IGOETVo8SmAsY4dzKlwSeCBjhE1aPEpgLGOHcypcEnggY4RNWjxKYCxjh3MqXBJ4IGOETVo8SmAsY4dzKlwSeCBjhE1aPEpgLGOHcypcEnggY4RNWjxKYCxjh3MqXBJ4IGOETVo8SmAsY4dzKlwSeCBjhE1aPEpgLGOHcypcEnggY4RNWjxKYCxjh3MqXBJ4IGOETVo8SmAsY4dzKlwSeCBjhE1aPEpgLGOHcypcEnggY4RNWjxKYCxjh3MqXBJ4IGOETVo8SmAsY4dzKlwSeCBjhE1aPEpgLGOHcypcEnggY4RNWjxKYCxjh3MqXBJ4IGOETVo8SmAsY4dzKlwSeCBjhE1aPEpgLGOHcypcEnggY4RNWjxKYCxjh3MqXBJ4IGOETVo8SmAsY4dzKlwSeCBjhE1aPEpgLGOHcypcEnggY4RNWjxKYCxjh3MqXBJ4IfE9e9ej/KPD7/f7H37b7V31f4h+8/4S7/6qkPyBghAdKdMJuASPc3Z/0BwSM8ECJTtgtYIS7+5P+gIARHijRCbsFjHB3f9IfEDDCAyU6YbeAEe7uT/oDAkZ4oEQn7BYwwt39SX9AwAgPlOiE3QJGuLs/6Q8IGOGBEp2wW8AId/cn/QEBIzxQohN2Cxjh7v6kPyBghAdKdMJuASPc3Z/0BwSM8ECJTtgtYIS7+5P+gIARHijRCbsFjHB3f9IfEDDCAyU6YbeAEe7uT/oDAkZ4oEQn7BYwwt39SX9AwAgPlOiE3QJGuLs/6Q8IGOGBEp2wW8AId/cn/QEBIzxQohN2Cxjh7v6kPyBghAdKdMJuASPc3Z/0BwSM8ECJTtgtYIS7+5P+gIARHijRCbsFjHB3f9IfEDDCAyU6YbeAEe7uT/oDAkZ4oEQn7BYwwt39SX9AwAgPlOiE3QJGuLs/6Q8IGOGBEp2wW8AId/cn/QEBIzxQohN2Cxjh7v6kPyDw14EbnBAo8H1fYKrMSP4TZvYiVZGAERaV7dRMASPM7EWqIgEjLCrbqZkCRpjZi1RFAkZYVLZTMwWMMLMXqYoEjLCobKdmChhhZi9SFQkYYVHZTs0UMMLMXqQqEjDCorKdmilghJm9SFUkYIRFZTs1U8AIM3uRqkjACIvKdmqmgBFm9iJVkYARFpXt1EwBI8zsRaoiASMsKtupmQJGmNmLVEUCRlhUtlMzBYwwsxepigSMsKhsp2YKGGFmL1IVCRhhUdlOzRQwwsxepCoSMMKisp2aKWCEmb1IVSRghEVlOzVTwAgze5GqSMAIi8p2aqaAEWb2IlWRgBEWle3UTAEjzOxFqiIBIywq26mZAkaY2YtURQJGWFS2UzMFjDCzF6mKBIywqGynZgoYYWYvUhUJGGFR2U7NFDDCzF6kKhIwwqKynZopYISZvUhVJGCERWU7NVPACDN7kapIwAiLynZqpoARZvYiFQECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIEAgROBvl1wQkxmaZi0AAAAASUVORK5CYII="""

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
        workstream_pattern_engine_status = None
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
