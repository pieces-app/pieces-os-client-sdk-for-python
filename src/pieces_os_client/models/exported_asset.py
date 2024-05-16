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



from pydantic import BaseModel, Field, StrictStr
from pieces_os_client.models.file_format import FileFormat
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp

class ExportedAsset(BaseModel):
    """
    This is a model for a minimum exported version of an asset.  # noqa: E501
    """
    name: StrictStr = Field(..., description="this is the title of the asset ")
    description: StrictStr = Field(..., description="this is the description of the asset")
    created: GroupedTimestamp = Field(...)
    raw: FileFormat = Field(...)
    __properties = ["name", "description", "created", "raw"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ExportedAsset:
        """Create an instance of ExportedAsset from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of raw
        if self.raw:
            _dict['raw'] = self.raw.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExportedAsset:
        """Create an instance of ExportedAsset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExportedAsset.parse_obj(obj)

        _obj = ExportedAsset.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "created": GroupedTimestamp.from_dict(obj.get("created")) if obj.get("created") is not None else None,
            "raw": FileFormat.from_dict(obj.get("raw")) if obj.get("raw") is not None else None
        })
        return _obj


