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
from pieces_os_client.models.assets import Assets
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema

class ReuseSuggestion(BaseModel):
    """
    This is the ReuseSuggestion. Mainly creating an additional model here because I imagine that we will want to add some additional data to this in the future (potentially with more numerical data that is emitted from the ML Models)  **Note: suggested is required here because we will want to say if we suggested to take this action of reuse or not.  ** Thoughts here. We could potentially return Assets: which would be an iterable of assets in most relavent order for the user to reuse if they want.  # noqa: E501
    """
    assets: Assets = Field(...)
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    suggested: StrictBool = Field(default=..., description="This is a boolean, that will say if you should or should not take action.")
    __properties = ["assets", "schema", "suggested"]

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
    def from_json(cls, json_str: str) -> ReuseSuggestion:
        """Create an instance of ReuseSuggestion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReuseSuggestion:
        """Create an instance of ReuseSuggestion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReuseSuggestion.parse_obj(obj)

        _obj = ReuseSuggestion.parse_obj({
            "assets": Assets.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "suggested": obj.get("suggested")
        })
        return _obj


