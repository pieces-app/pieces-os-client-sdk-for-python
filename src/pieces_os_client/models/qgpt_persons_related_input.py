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
from pieces_os_client.models.qgpt_conversation import QGPTConversation
from pieces_os_client.models.seed import Seed

class QGPTPersonsRelatedInput(BaseModel):
    """
    This is used for /qgpt/persons/related.  will accept a seed, or conversation all optionally.   # noqa: E501
    """
    application: Optional[StrictStr] = Field(default=None, description="optional application id")
    conversation: Optional[QGPTConversation] = None
    model: Optional[StrictStr] = Field(default=None, description="optional model id")
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    seed: Optional[Seed] = None
    __properties = ["application", "conversation", "model", "schema", "seed"]

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
    def from_json(cls, json_str: str) -> QGPTPersonsRelatedInput:
        """Create an instance of QGPTPersonsRelatedInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of conversation
        if self.conversation:
            _dict['conversation'] = self.conversation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of seed
        if self.seed:
            _dict['seed'] = self.seed.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QGPTPersonsRelatedInput:
        """Create an instance of QGPTPersonsRelatedInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QGPTPersonsRelatedInput.parse_obj(obj)

        _obj = QGPTPersonsRelatedInput.parse_obj({
            "application": obj.get("application"),
            "conversation": QGPTConversation.from_dict(obj.get("conversation")) if obj.get("conversation") is not None else None,
            "model": obj.get("model"),
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "seed": Seed.from_dict(obj.get("seed")) if obj.get("seed") is not None else None
        })
        return _obj


