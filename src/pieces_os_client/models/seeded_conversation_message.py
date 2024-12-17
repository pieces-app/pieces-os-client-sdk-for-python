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
from pieces_os_client.models.conversation_message_sentiment_enum import ConversationMessageSentimentEnum
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.fragment_format import FragmentFormat
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.model import Model
from pieces_os_client.models.qgpt_conversation_message_role_enum import QGPTConversationMessageRoleEnum
from pieces_os_client.models.referenced_conversation import ReferencedConversation

class SeededConversationMessage(BaseModel):
    """
    This is a seeded version of a ConversationMessage.  conversation is optional, this is because it can be used within the SeededConversation, however if this is passed into the /messages/create w/o a conversation uuid then we will throw an error.  # noqa: E501
    """
    conversation: Optional[ReferencedConversation] = None
    created: Optional[GroupedTimestamp] = None
    fragment: FragmentFormat = Field(...)
    model: Optional[Model] = None
    role: QGPTConversationMessageRoleEnum = Field(...)
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    sentiment: Optional[ConversationMessageSentimentEnum] = None
    __properties = ["conversation", "created", "fragment", "model", "role", "schema", "sentiment"]

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
    def from_json(cls, json_str: str) -> SeededConversationMessage:
        """Create an instance of SeededConversationMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fragment
        if self.fragment:
            _dict['fragment'] = self.fragment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededConversationMessage:
        """Create an instance of SeededConversationMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededConversationMessage.parse_obj(obj)

        _obj = SeededConversationMessage.parse_obj({
            "conversation": ReferencedConversation.from_dict(obj.get("conversation")) if obj.get("conversation") is not None else None,
            "created": GroupedTimestamp.from_dict(obj.get("created")) if obj.get("created") is not None else None,
            "fragment": FragmentFormat.from_dict(obj.get("fragment")) if obj.get("fragment") is not None else None,
            "model": Model.from_dict(obj.get("model")) if obj.get("model") is not None else None,
            "role": obj.get("role"),
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "sentiment": obj.get("sentiment")
        })
        return _obj


