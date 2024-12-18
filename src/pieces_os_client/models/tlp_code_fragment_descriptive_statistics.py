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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema

class TLPCodeFragmentDescriptiveStatistics(BaseModel):
    """
    Model for ML big query Data collection.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    user: StrictStr = Field(...)
    os: StrictStr = Field(...)
    language: StrictStr = Field(...)
    length: Union[StrictFloat, StrictInt] = Field(...)
    ast: StrictStr = Field(...)
    timestamp: StrictStr = Field(...)
    asset: StrictStr = Field(...)
    context: StrictStr = Field(default=..., description="this is the application in which this was created from.")
    snippet: StrictStr = Field(default=..., description="this is the value of the snippet")
    probability: StrictStr = Field(...)
    __properties = ["schema", "user", "os", "language", "length", "ast", "timestamp", "asset", "context", "snippet", "probability"]

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
    def from_json(cls, json_str: str) -> TLPCodeFragmentDescriptiveStatistics:
        """Create an instance of TLPCodeFragmentDescriptiveStatistics from a JSON string"""
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
    def from_dict(cls, obj: dict) -> TLPCodeFragmentDescriptiveStatistics:
        """Create an instance of TLPCodeFragmentDescriptiveStatistics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TLPCodeFragmentDescriptiveStatistics.parse_obj(obj)

        _obj = TLPCodeFragmentDescriptiveStatistics.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "user": obj.get("user"),
            "os": obj.get("os"),
            "language": obj.get("language"),
            "length": obj.get("length"),
            "ast": obj.get("ast"),
            "timestamp": obj.get("timestamp"),
            "asset": obj.get("asset"),
            "context": obj.get("context"),
            "snippet": obj.get("snippet"),
            "probability": obj.get("probability")
        })
        return _obj


