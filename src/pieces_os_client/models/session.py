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
from pydantic import BaseModel, Field, StrictStr
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp

class Session(BaseModel):
    """
    This is a specific model that will let us know at what time this user was using the application.  # noqa: E501
    """
    closed: Optional[GroupedTimestamp] = None
    id: StrictStr = Field(default=..., description="The UUID of the current Session")
    opened: GroupedTimestamp = Field(...)
    __properties = ["closed", "id", "opened"]

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
    def from_json(cls, json_str: str) -> Session:
        """Create an instance of Session from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of closed
        if self.closed:
            _dict['closed'] = self.closed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of opened
        if self.opened:
            _dict['opened'] = self.opened.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Session:
        """Create an instance of Session from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Session.parse_obj(obj)

        _obj = Session.parse_obj({
            "closed": GroupedTimestamp.from_dict(obj.get("closed")) if obj.get("closed") is not None else None,
            "id": obj.get("id"),
            "opened": GroupedTimestamp.from_dict(obj.get("opened")) if obj.get("opened") is not None else None
        })
        return _obj


