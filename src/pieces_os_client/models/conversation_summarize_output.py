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
from pydantic import BaseModel, Field
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.referenced_annotation import ReferencedAnnotation
from pieces_os_client.models.referenced_conversation import ReferencedConversation

class ConversationSummarizeOutput(BaseModel):
    """
    This is the output model for \"/conversation/{conversation}/summarize  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    conversation: ReferencedConversation = Field(...)
    annotation: ReferencedAnnotation = Field(...)
    __properties = ["schema", "conversation", "annotation"]

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
    def from_json(cls, json_str: str) -> ConversationSummarizeOutput:
        """Create an instance of ConversationSummarizeOutput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of conversation
        if self.conversation:
            _dict['conversation'] = self.conversation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of annotation
        if self.annotation:
            _dict['annotation'] = self.annotation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConversationSummarizeOutput:
        """Create an instance of ConversationSummarizeOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConversationSummarizeOutput.parse_obj(obj)

        _obj = ConversationSummarizeOutput.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "conversation": ReferencedConversation.from_dict(obj.get("conversation")) if obj.get("conversation") is not None else None,
            "annotation": ReferencedAnnotation.from_dict(obj.get("annotation")) if obj.get("annotation") is not None else None
        })
        return _obj


