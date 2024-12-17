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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from pieces_os_client.models.anchor_type_enum import AnchorTypeEnum
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.platform_enum import PlatformEnum

class SeededAnchorPoint(BaseModel):
    """
    SeededAnchorPoint
    """
    anchor: StrictStr = Field(default=..., description="Cannot create an AnchorPoint w/o a Anchor.")
    fullpath: StrictStr = Field(...)
    platform: Optional[PlatformEnum] = None
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    type: AnchorTypeEnum = Field(...)
    watch: Optional[StrictBool] = None
    __properties = ["anchor", "fullpath", "platform", "schema", "type", "watch"]

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
    def from_json(cls, json_str: str) -> SeededAnchorPoint:
        """Create an instance of SeededAnchorPoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededAnchorPoint:
        """Create an instance of SeededAnchorPoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededAnchorPoint.parse_obj(obj)

        _obj = SeededAnchorPoint.parse_obj({
            "anchor": obj.get("anchor"),
            "fullpath": obj.get("fullpath"),
            "platform": obj.get("platform"),
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "type": obj.get("type"),
            "watch": obj.get("watch")
        })
        return _obj


