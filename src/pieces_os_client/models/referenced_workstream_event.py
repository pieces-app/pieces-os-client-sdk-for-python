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
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema

class ReferencedWorkstreamEvent(BaseModel):
    """
    This is a minimal representation of a WorkstreamEvent event.  # noqa: E501
    """
    id: StrictStr = Field(...)
    reference: Optional[FlattenedWorkstreamEvent] = None
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    __properties = ["id", "reference", "schema"]

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
    def from_json(cls, json_str: str) -> ReferencedWorkstreamEvent:
        """Create an instance of ReferencedWorkstreamEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of reference
        if self.reference:
            _dict['reference'] = self.reference.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReferencedWorkstreamEvent:
        """Create an instance of ReferencedWorkstreamEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReferencedWorkstreamEvent.parse_obj(obj)

        _obj = ReferencedWorkstreamEvent.parse_obj({
            "id": obj.get("id"),
            "reference": FlattenedWorkstreamEvent.from_dict(obj.get("reference")) if obj.get("reference") is not None else None,
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None
        })
        return _obj

from pieces_os_client.models.flattened_workstream_event import FlattenedWorkstreamEvent
ReferencedWorkstreamEvent.update_forward_refs()

