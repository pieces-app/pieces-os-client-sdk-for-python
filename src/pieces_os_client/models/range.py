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
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.flattened_conversations import FlattenedConversations
from pieces_os_client.models.flattened_workstream_summaries import FlattenedWorkstreamSummaries
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.score import Score

class Range(BaseModel):
    """
    This is an identified Range, this is ONLY needed when using plural rangedTimestamps, in order to ensure granularity(add/modify/delete)  # noqa: E501
    """
    between: Optional[StrictBool] = None
    conversations: Optional[FlattenedConversations] = None
    created: GroupedTimestamp = Field(...)
    var_from: Optional[GroupedTimestamp] = Field(default=None, alias="from")
    id: StrictStr = Field(...)
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    score: Optional[Score] = None
    summaries: Optional[FlattenedWorkstreamSummaries] = None
    to: Optional[GroupedTimestamp] = None
    updated: GroupedTimestamp = Field(...)
    __properties = ["between", "conversations", "created", "from", "id", "schema", "score", "summaries", "to", "updated"]

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
    def from_json(cls, json_str: str) -> Range:
        """Create an instance of Range from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of conversations
        if self.conversations:
            _dict['conversations'] = self.conversations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_from
        if self.var_from:
            _dict['from'] = self.var_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of score
        if self.score:
            _dict['score'] = self.score.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summaries
        if self.summaries:
            _dict['summaries'] = self.summaries.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to
        if self.to:
            _dict['to'] = self.to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Range:
        """Create an instance of Range from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Range.parse_obj(obj)

        _obj = Range.parse_obj({
            "between": obj.get("between"),
            "conversations": FlattenedConversations.from_dict(obj.get("conversations")) if obj.get("conversations") is not None else None,
            "created": GroupedTimestamp.from_dict(obj.get("created")) if obj.get("created") is not None else None,
            "var_from": GroupedTimestamp.from_dict(obj.get("from")) if obj.get("from") is not None else None,
            "id": obj.get("id"),
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "score": Score.from_dict(obj.get("score")) if obj.get("score") is not None else None,
            "summaries": FlattenedWorkstreamSummaries.from_dict(obj.get("summaries")) if obj.get("summaries") is not None else None,
            "to": GroupedTimestamp.from_dict(obj.get("to")) if obj.get("to") is not None else None,
            "updated": GroupedTimestamp.from_dict(obj.get("updated")) if obj.get("updated") is not None else None
        })
        return _obj


