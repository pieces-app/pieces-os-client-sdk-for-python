# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.model_download_progress_status_enum import ModelDownloadProgressStatusEnum
from pieces_os_client.models.os_file_streaming_read_progress import OSFileStreamingReadProgress
from pieces_os_client.models.transferable_bytes import TransferableBytes
from typing import Optional, Set
from typing_extensions import Self

class OSFileStreamingRead(BaseModel):
    """
    This is a model to return stream progress for a file read.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    status: ModelDownloadProgressStatusEnum
    percentage: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Optionally if the download is in progress you will receive a download percent(from 0-100).")
    path: StrictStr
    id: StrictStr = Field(description="This is a generated UUID that represents this current stream in progress(can be used to cancel this in the future)")
    bytes: Optional[TransferableBytes] = None
    progress: Optional[OSFileStreamingReadProgress] = None
    __properties: ClassVar[List[str]] = ["schema", "status", "percentage", "path", "id", "bytes", "progress"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OSFileStreamingRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bytes
        if self.bytes:
            _dict['bytes'] = self.bytes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of progress
        if self.progress:
            _dict['progress'] = self.progress.to_dict()
        # set to None if percentage (nullable) is None
        # and model_fields_set contains the field
        if self.percentage is None and "percentage" in self.model_fields_set:
            _dict['percentage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OSFileStreamingRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "status": obj.get("status"),
            "percentage": obj.get("percentage"),
            "path": obj.get("path"),
            "id": obj.get("id"),
            "bytes": TransferableBytes.from_dict(obj["bytes"]) if obj.get("bytes") is not None else None,
            "progress": OSFileStreamingReadProgress.from_dict(obj["progress"]) if obj.get("progress") is not None else None
        })
        return _obj


