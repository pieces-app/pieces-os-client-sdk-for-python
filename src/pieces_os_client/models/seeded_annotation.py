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
from pieces_os_client.models.annotation_type_enum import AnnotationTypeEnum
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.mechanism_enum import MechanismEnum

class SeededAnnotation(BaseModel):
    """
    This is the percursor to a fully referenced Annotation.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    mechanism: Optional[MechanismEnum] = None
    asset: Optional[StrictStr] = None
    person: Optional[StrictStr] = None
    type: AnnotationTypeEnum = Field(...)
    text: StrictStr = Field(default=..., description="This is the text of the annotation.")
    model: Optional[StrictStr] = None
    pseudo: Optional[StrictBool] = None
    favorited: Optional[StrictBool] = None
    anchor: Optional[StrictStr] = None
    conversation: Optional[StrictStr] = None
    workstream_summary: Optional[StrictStr] = None
    messages: Optional[FlattenedConversationMessages] = None
    assets: Optional[FlattenedAssets] = None
    persons: Optional[FlattenedPersons] = None
    anchors: Optional[FlattenedAnchors] = None
    conversations: Optional[FlattenedConversations] = None
    websites: Optional[FlattenedWebsites] = None
    tags: Optional[FlattenedTags] = None
    summaries: Optional[FlattenedWorkstreamSummaries] = None
    workstream_events: Optional[FlattenedWorkstreamEvents] = None
    __properties = ["schema", "mechanism", "asset", "person", "type", "text", "model", "pseudo", "favorited", "anchor", "conversation", "workstream_summary", "messages", "assets", "persons", "anchors", "conversations", "websites", "tags", "summaries", "workstream_events"]

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
    def from_json(cls, json_str: str) -> SeededAnnotation:
        """Create an instance of SeededAnnotation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of messages
        if self.messages:
            _dict['messages'] = self.messages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of persons
        if self.persons:
            _dict['persons'] = self.persons.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anchors
        if self.anchors:
            _dict['anchors'] = self.anchors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversations
        if self.conversations:
            _dict['conversations'] = self.conversations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of websites
        if self.websites:
            _dict['websites'] = self.websites.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summaries
        if self.summaries:
            _dict['summaries'] = self.summaries.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workstream_events
        if self.workstream_events:
            _dict['workstream_events'] = self.workstream_events.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededAnnotation:
        """Create an instance of SeededAnnotation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededAnnotation.parse_obj(obj)

        _obj = SeededAnnotation.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "mechanism": obj.get("mechanism"),
            "asset": obj.get("asset"),
            "person": obj.get("person"),
            "type": obj.get("type"),
            "text": obj.get("text"),
            "model": obj.get("model"),
            "pseudo": obj.get("pseudo"),
            "favorited": obj.get("favorited"),
            "anchor": obj.get("anchor"),
            "conversation": obj.get("conversation"),
            "workstream_summary": obj.get("workstream_summary"),
            "messages": FlattenedConversationMessages.from_dict(obj.get("messages")) if obj.get("messages") is not None else None,
            "assets": FlattenedAssets.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "persons": FlattenedPersons.from_dict(obj.get("persons")) if obj.get("persons") is not None else None,
            "anchors": FlattenedAnchors.from_dict(obj.get("anchors")) if obj.get("anchors") is not None else None,
            "conversations": FlattenedConversations.from_dict(obj.get("conversations")) if obj.get("conversations") is not None else None,
            "websites": FlattenedWebsites.from_dict(obj.get("websites")) if obj.get("websites") is not None else None,
            "tags": FlattenedTags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None,
            "summaries": FlattenedWorkstreamSummaries.from_dict(obj.get("summaries")) if obj.get("summaries") is not None else None,
            "workstream_events": FlattenedWorkstreamEvents.from_dict(obj.get("workstream_events")) if obj.get("workstream_events") is not None else None
        })
        return _obj

from pieces_os_client.models.flattened_anchors import FlattenedAnchors
from pieces_os_client.models.flattened_assets import FlattenedAssets
from pieces_os_client.models.flattened_conversation_messages import FlattenedConversationMessages
from pieces_os_client.models.flattened_conversations import FlattenedConversations
from pieces_os_client.models.flattened_persons import FlattenedPersons
from pieces_os_client.models.flattened_tags import FlattenedTags
from pieces_os_client.models.flattened_websites import FlattenedWebsites
from pieces_os_client.models.flattened_workstream_events import FlattenedWorkstreamEvents
from pieces_os_client.models.flattened_workstream_summaries import FlattenedWorkstreamSummaries
SeededAnnotation.update_forward_refs()

