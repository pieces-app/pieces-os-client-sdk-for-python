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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from pieces_os_client.models.detected_external_application import DetectedExternalApplication
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema

class DetectedExternalApplications(BaseModel):
    """
    This is used as the returnable for the /applications/external && /applications/external/related endpoints.  This will return an iterable of Deteched Application a detected Application is an application that is currently installed on your machine.  the /applications/external/related endpoint, will return a subset of the applications returned mainly applications that we detect are Pieces Applications that you have yet to install + names of applications where Pieces is coming soon.  # noqa: E501
    """
    iterable: conlist(DetectedExternalApplication) = Field(...)
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    __properties = ["iterable", "schema"]

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
    def from_json(cls, json_str: str) -> DetectedExternalApplications:
        """Create an instance of DetectedExternalApplications from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in iterable (list)
        _items = []
        if self.iterable:
            for _item in self.iterable:
                if _item:
                    _items.append(_item.to_dict())
            _dict['iterable'] = _items
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DetectedExternalApplications:
        """Create an instance of DetectedExternalApplications from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DetectedExternalApplications.parse_obj(obj)

        _obj = DetectedExternalApplications.parse_obj({
            "iterable": [DetectedExternalApplication.from_dict(_item) for _item in obj.get("iterable")] if obj.get("iterable") is not None else None,
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None
        })
        return _obj


