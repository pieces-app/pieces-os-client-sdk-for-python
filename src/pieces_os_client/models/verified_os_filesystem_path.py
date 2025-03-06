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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.byte_descriptor import ByteDescriptor
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from typing import Optional, Set
from typing_extensions import Self

class VerifiedOSFilesystemPath(BaseModel):
    """
    This will return is the given path was verified/ or it was invalid.  and if it is valid if it is a file/folder  note: file/directory are both null.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    path: StrictStr
    file: Optional[StrictBool] = None
    directory: Optional[StrictBool] = None
    verified: StrictBool = Field(description="This means if the path(file/folder) exists on the machine.")
    denied: Optional[StrictBool] = Field(default=None, description="This means that attempting to access the file was not aloud(ie no permission)")
    bytes: Optional[ByteDescriptor] = None
    __properties: ClassVar[List[str]] = ["schema", "path", "file", "directory", "verified", "denied", "bytes"]

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
        """Create an instance of VerifiedOSFilesystemPath from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VerifiedOSFilesystemPath from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "path": obj.get("path"),
            "file": obj.get("file"),
            "directory": obj.get("directory"),
            "verified": obj.get("verified"),
            "denied": obj.get("denied"),
            "bytes": ByteDescriptor.from_dict(obj["bytes"]) if obj.get("bytes") is not None else None
        })
        return _obj


