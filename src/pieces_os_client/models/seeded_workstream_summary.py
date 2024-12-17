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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from pieces_os_client.models.applications import Applications
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.flattened_anchors import FlattenedAnchors
from pieces_os_client.models.flattened_assets import FlattenedAssets
from pieces_os_client.models.flattened_conversations import FlattenedConversations
from pieces_os_client.models.flattened_persons import FlattenedPersons
from pieces_os_client.models.flattened_ranges import FlattenedRanges
from pieces_os_client.models.flattened_websites import FlattenedWebsites
from pieces_os_client.models.flattened_workstream_events import FlattenedWorkstreamEvents
from pieces_os_client.models.model import Model
from pieces_os_client.models.seeded_annotation import SeededAnnotation

class SeededWorkstreamSummary(BaseModel):
    """
    This is a seeded version of a WorkstreamSummary  # noqa: E501
    """
    anchors: Optional[FlattenedAnchors] = None
    annotations: Optional[conlist(SeededAnnotation)] = None
    applications: Optional[Applications] = None
    assets: Optional[FlattenedAssets] = None
    conversations: Optional[FlattenedConversations] = None
    events: Optional[FlattenedWorkstreamEvents] = None
    model: Model = Field(...)
    name: StrictStr = Field(...)
    persons: Optional[FlattenedPersons] = None
    ranges: Optional[FlattenedRanges] = None
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    websites: Optional[FlattenedWebsites] = None
    __properties = ["anchors", "annotations", "applications", "assets", "conversations", "events", "model", "name", "persons", "ranges", "schema", "websites"]

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
    def from_json(cls, json_str: str) -> SeededWorkstreamSummary:
        """Create an instance of SeededWorkstreamSummary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of anchors
        if self.anchors:
            _dict['anchors'] = self.anchors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in annotations (list)
        _items = []
        if self.annotations:
            for _item in self.annotations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['annotations'] = _items
        # override the default output from pydantic by calling `to_dict()` of applications
        if self.applications:
            _dict['applications'] = self.applications.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversations
        if self.conversations:
            _dict['conversations'] = self.conversations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of events
        if self.events:
            _dict['events'] = self.events.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of persons
        if self.persons:
            _dict['persons'] = self.persons.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ranges
        if self.ranges:
            _dict['ranges'] = self.ranges.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of websites
        if self.websites:
            _dict['websites'] = self.websites.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededWorkstreamSummary:
        """Create an instance of SeededWorkstreamSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededWorkstreamSummary.parse_obj(obj)

        _obj = SeededWorkstreamSummary.parse_obj({
            "anchors": FlattenedAnchors.from_dict(obj.get("anchors")) if obj.get("anchors") is not None else None,
            "annotations": [SeededAnnotation.from_dict(_item) for _item in obj.get("annotations")] if obj.get("annotations") is not None else None,
            "applications": Applications.from_dict(obj.get("applications")) if obj.get("applications") is not None else None,
            "assets": FlattenedAssets.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "conversations": FlattenedConversations.from_dict(obj.get("conversations")) if obj.get("conversations") is not None else None,
            "events": FlattenedWorkstreamEvents.from_dict(obj.get("events")) if obj.get("events") is not None else None,
            "model": Model.from_dict(obj.get("model")) if obj.get("model") is not None else None,
            "name": obj.get("name"),
            "persons": FlattenedPersons.from_dict(obj.get("persons")) if obj.get("persons") is not None else None,
            "ranges": FlattenedRanges.from_dict(obj.get("ranges")) if obj.get("ranges") is not None else None,
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "websites": FlattenedWebsites.from_dict(obj.get("websites")) if obj.get("websites") is not None else None
        })
        return _obj


