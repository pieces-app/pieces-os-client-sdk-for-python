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
from pieces_os_client.models.seeded_score import SeededScore

class SeededScoreIncrement(BaseModel):
    """
    This is the body for a respective scores increment,  This will enable us to know what material we want to increment, all of which are optional, if it is defined we will attempt to increment the material.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    asset: Optional[SeededScore] = None
    assets: Optional[SeededScore] = None
    website: Optional[SeededScore] = None
    websites: Optional[SeededScore] = None
    anchor: Optional[SeededScore] = None
    anchors: Optional[SeededScore] = None
    anchor_point: Optional[SeededScore] = Field(default=None, alias="anchorPoint")
    anchor_points: Optional[SeededScore] = Field(default=None, alias="anchorPoints")
    annotation: Optional[SeededScore] = None
    annotations: Optional[SeededScore] = None
    conversation: Optional[SeededScore] = None
    conversations: Optional[SeededScore] = None
    conversation_message: Optional[SeededScore] = Field(default=None, alias="conversationMessage")
    conversation_messages: Optional[SeededScore] = Field(default=None, alias="conversationMessages")
    share: Optional[SeededScore] = None
    shares: Optional[SeededScore] = None
    sensitive: Optional[SeededScore] = None
    sensitives: Optional[SeededScore] = None
    hint: Optional[SeededScore] = None
    hints: Optional[SeededScore] = None
    person: Optional[SeededScore] = None
    persons: Optional[SeededScore] = None
    tag: Optional[SeededScore] = None
    tags: Optional[SeededScore] = None
    workstream_summary: Optional[SeededScore] = None
    workstream_summaries: Optional[SeededScore] = None
    workstream_events: Optional[SeededScore] = None
    workstream_event: Optional[SeededScore] = None
    ranges: Optional[SeededScore] = None
    range: Optional[SeededScore] = None
    workstream_pattern_engine_sources: Optional[SeededScore] = None
    workstream_pattern_engine_source: Optional[SeededScore] = None
    models: Optional[SeededScore] = None
    model: Optional[SeededScore] = None
    __properties = ["schema", "asset", "assets", "website", "websites", "anchor", "anchors", "anchorPoint", "anchorPoints", "annotation", "annotations", "conversation", "conversations", "conversationMessage", "conversationMessages", "share", "shares", "sensitive", "sensitives", "hint", "hints", "person", "persons", "tag", "tags", "workstream_summary", "workstream_summaries", "workstream_events", "workstream_event", "ranges", "range", "workstream_pattern_engine_sources", "workstream_pattern_engine_source", "models", "model"]

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
    def from_json(cls, json_str: str) -> SeededScoreIncrement:
        """Create an instance of SeededScoreIncrement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of website
        if self.website:
            _dict['website'] = self.website.to_dict()
        # override the default output from pydantic by calling `to_dict()` of websites
        if self.websites:
            _dict['websites'] = self.websites.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anchor
        if self.anchor:
            _dict['anchor'] = self.anchor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anchors
        if self.anchors:
            _dict['anchors'] = self.anchors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anchor_point
        if self.anchor_point:
            _dict['anchorPoint'] = self.anchor_point.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anchor_points
        if self.anchor_points:
            _dict['anchorPoints'] = self.anchor_points.to_dict()
        # override the default output from pydantic by calling `to_dict()` of annotation
        if self.annotation:
            _dict['annotation'] = self.annotation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of annotations
        if self.annotations:
            _dict['annotations'] = self.annotations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversation
        if self.conversation:
            _dict['conversation'] = self.conversation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversations
        if self.conversations:
            _dict['conversations'] = self.conversations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversation_message
        if self.conversation_message:
            _dict['conversationMessage'] = self.conversation_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversation_messages
        if self.conversation_messages:
            _dict['conversationMessages'] = self.conversation_messages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of share
        if self.share:
            _dict['share'] = self.share.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shares
        if self.shares:
            _dict['shares'] = self.shares.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sensitive
        if self.sensitive:
            _dict['sensitive'] = self.sensitive.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sensitives
        if self.sensitives:
            _dict['sensitives'] = self.sensitives.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hint
        if self.hint:
            _dict['hint'] = self.hint.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hints
        if self.hints:
            _dict['hints'] = self.hints.to_dict()
        # override the default output from pydantic by calling `to_dict()` of person
        if self.person:
            _dict['person'] = self.person.to_dict()
        # override the default output from pydantic by calling `to_dict()` of persons
        if self.persons:
            _dict['persons'] = self.persons.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tag
        if self.tag:
            _dict['tag'] = self.tag.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workstream_summary
        if self.workstream_summary:
            _dict['workstream_summary'] = self.workstream_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workstream_summaries
        if self.workstream_summaries:
            _dict['workstream_summaries'] = self.workstream_summaries.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workstream_events
        if self.workstream_events:
            _dict['workstream_events'] = self.workstream_events.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workstream_event
        if self.workstream_event:
            _dict['workstream_event'] = self.workstream_event.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ranges
        if self.ranges:
            _dict['ranges'] = self.ranges.to_dict()
        # override the default output from pydantic by calling `to_dict()` of range
        if self.range:
            _dict['range'] = self.range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workstream_pattern_engine_sources
        if self.workstream_pattern_engine_sources:
            _dict['workstream_pattern_engine_sources'] = self.workstream_pattern_engine_sources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workstream_pattern_engine_source
        if self.workstream_pattern_engine_source:
            _dict['workstream_pattern_engine_source'] = self.workstream_pattern_engine_source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of models
        if self.models:
            _dict['models'] = self.models.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededScoreIncrement:
        """Create an instance of SeededScoreIncrement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededScoreIncrement.parse_obj(obj)

        _obj = SeededScoreIncrement.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "asset": SeededScore.from_dict(obj.get("asset")) if obj.get("asset") is not None else None,
            "assets": SeededScore.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "website": SeededScore.from_dict(obj.get("website")) if obj.get("website") is not None else None,
            "websites": SeededScore.from_dict(obj.get("websites")) if obj.get("websites") is not None else None,
            "anchor": SeededScore.from_dict(obj.get("anchor")) if obj.get("anchor") is not None else None,
            "anchors": SeededScore.from_dict(obj.get("anchors")) if obj.get("anchors") is not None else None,
            "anchor_point": SeededScore.from_dict(obj.get("anchorPoint")) if obj.get("anchorPoint") is not None else None,
            "anchor_points": SeededScore.from_dict(obj.get("anchorPoints")) if obj.get("anchorPoints") is not None else None,
            "annotation": SeededScore.from_dict(obj.get("annotation")) if obj.get("annotation") is not None else None,
            "annotations": SeededScore.from_dict(obj.get("annotations")) if obj.get("annotations") is not None else None,
            "conversation": SeededScore.from_dict(obj.get("conversation")) if obj.get("conversation") is not None else None,
            "conversations": SeededScore.from_dict(obj.get("conversations")) if obj.get("conversations") is not None else None,
            "conversation_message": SeededScore.from_dict(obj.get("conversationMessage")) if obj.get("conversationMessage") is not None else None,
            "conversation_messages": SeededScore.from_dict(obj.get("conversationMessages")) if obj.get("conversationMessages") is not None else None,
            "share": SeededScore.from_dict(obj.get("share")) if obj.get("share") is not None else None,
            "shares": SeededScore.from_dict(obj.get("shares")) if obj.get("shares") is not None else None,
            "sensitive": SeededScore.from_dict(obj.get("sensitive")) if obj.get("sensitive") is not None else None,
            "sensitives": SeededScore.from_dict(obj.get("sensitives")) if obj.get("sensitives") is not None else None,
            "hint": SeededScore.from_dict(obj.get("hint")) if obj.get("hint") is not None else None,
            "hints": SeededScore.from_dict(obj.get("hints")) if obj.get("hints") is not None else None,
            "person": SeededScore.from_dict(obj.get("person")) if obj.get("person") is not None else None,
            "persons": SeededScore.from_dict(obj.get("persons")) if obj.get("persons") is not None else None,
            "tag": SeededScore.from_dict(obj.get("tag")) if obj.get("tag") is not None else None,
            "tags": SeededScore.from_dict(obj.get("tags")) if obj.get("tags") is not None else None,
            "workstream_summary": SeededScore.from_dict(obj.get("workstream_summary")) if obj.get("workstream_summary") is not None else None,
            "workstream_summaries": SeededScore.from_dict(obj.get("workstream_summaries")) if obj.get("workstream_summaries") is not None else None,
            "workstream_events": SeededScore.from_dict(obj.get("workstream_events")) if obj.get("workstream_events") is not None else None,
            "workstream_event": SeededScore.from_dict(obj.get("workstream_event")) if obj.get("workstream_event") is not None else None,
            "ranges": SeededScore.from_dict(obj.get("ranges")) if obj.get("ranges") is not None else None,
            "range": SeededScore.from_dict(obj.get("range")) if obj.get("range") is not None else None,
            "workstream_pattern_engine_sources": SeededScore.from_dict(obj.get("workstream_pattern_engine_sources")) if obj.get("workstream_pattern_engine_sources") is not None else None,
            "workstream_pattern_engine_source": SeededScore.from_dict(obj.get("workstream_pattern_engine_source")) if obj.get("workstream_pattern_engine_source") is not None else None,
            "models": SeededScore.from_dict(obj.get("models")) if obj.get("models") is not None else None,
            "model": SeededScore.from_dict(obj.get("model")) if obj.get("model") is not None else None
        })
        return _obj


