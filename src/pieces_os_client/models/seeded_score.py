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
from pydantic import BaseModel, Field, StrictBool
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema

class SeededScore(BaseModel):
    """
    This is the low level seeded score and will let us know what exactly we want to increment on our material.  Note: ONLY include one of these, as we will only increment one of the following.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    reuse: Optional[StrictBool] = None
    update: Optional[StrictBool] = None
    reference: Optional[StrictBool] = None
    priority: Optional[StrictBool] = None
    searched: Optional[StrictBool] = None
    __properties = ["schema", "reuse", "update", "reference", "priority", "searched"]

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
    def from_json(cls, json_str: str) -> SeededScore:
        """Create an instance of SeededScore from a JSON string"""
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
    def from_dict(cls, obj: dict) -> SeededScore:
        """Create an instance of SeededScore from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededScore.parse_obj(obj)

        _obj = SeededScore.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "reuse": obj.get("reuse"),
            "update": obj.get("update"),
            "reference": obj.get("reference"),
            "priority": obj.get("priority"),
            "searched": obj.get("searched")
        })
        return _obj


