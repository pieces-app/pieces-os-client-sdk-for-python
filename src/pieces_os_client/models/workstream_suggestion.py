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
from pieces_os_client.models.flattened_anchors import FlattenedAnchors
from pieces_os_client.models.flattened_annotations import FlattenedAnnotations
from pieces_os_client.models.flattened_assets import FlattenedAssets
from pieces_os_client.models.flattened_conversation_messages import FlattenedConversationMessages
from pieces_os_client.models.flattened_conversations import FlattenedConversations
from pieces_os_client.models.flattened_hints import FlattenedHints
from pieces_os_client.models.flattened_identified_workstream_pattern_engine_sources import FlattenedIdentifiedWorkstreamPatternEngineSources
from pieces_os_client.models.flattened_persons import FlattenedPersons
from pieces_os_client.models.flattened_sensitives import FlattenedSensitives
from pieces_os_client.models.flattened_tags import FlattenedTags
from pieces_os_client.models.flattened_websites import FlattenedWebsites
from pieces_os_client.models.flattened_workstream_summaries import FlattenedWorkstreamSummaries
from pieces_os_client.models.referenced_anchor import ReferencedAnchor
from pieces_os_client.models.referenced_annotation import ReferencedAnnotation
from pieces_os_client.models.referenced_asset import ReferencedAsset
from pieces_os_client.models.referenced_conversation import ReferencedConversation
from pieces_os_client.models.referenced_conversation_message import ReferencedConversationMessage
from pieces_os_client.models.referenced_hint import ReferencedHint
from pieces_os_client.models.referenced_identified_workstream_pattern_engine_source import ReferencedIdentifiedWorkstreamPatternEngineSource
from pieces_os_client.models.referenced_person import ReferencedPerson
from pieces_os_client.models.referenced_sensitive import ReferencedSensitive
from pieces_os_client.models.referenced_tag import ReferencedTag
from pieces_os_client.models.referenced_website import ReferencedWebsite
from pieces_os_client.models.referenced_workstream_summary import ReferencedWorkstreamSummary
from pieces_os_client.models.seed import Seed
from pieces_os_client.models.seeds import Seeds

class WorkstreamSuggestion(BaseModel):
    """
    This is an individual material that is apart of the workstream feed. might want to also consider plural uuids ie top websites/tags/and others..  related: this is an optional field that will only be calculated for first degree relationships.          ie. an anchor may have related.iterable.first.persons that are not associated but related.          via the workstream patturn engine.  current: if current is defined then this is the current viewed object  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    summary: Optional[ReferencedWorkstreamSummary] = None
    asset: Optional[ReferencedAsset] = None
    tag: Optional[ReferencedTag] = None
    website: Optional[ReferencedWebsite] = None
    anchor: Optional[ReferencedAnchor] = None
    conversation: Optional[ReferencedConversation] = None
    person: Optional[ReferencedPerson] = None
    seed: Optional[Seed] = None
    seeds: Optional[Seeds] = None
    summaries: Optional[FlattenedWorkstreamSummaries] = None
    assets: Optional[FlattenedAssets] = None
    tags: Optional[FlattenedTags] = None
    websites: Optional[FlattenedWebsites] = None
    anchors: Optional[FlattenedAnchors] = None
    conversations: Optional[FlattenedConversations] = None
    persons: Optional[FlattenedPersons] = None
    related: Optional[WorkstreamSuggestions] = None
    current: Optional[WorkstreamSuggestion] = None
    annotation: Optional[ReferencedAnnotation] = None
    annotations: Optional[FlattenedAnnotations] = None
    conversation_message: Optional[ReferencedConversationMessage] = Field(default=None, alias="conversationMessage")
    conversation_messages: Optional[FlattenedConversationMessages] = Field(default=None, alias="conversationMessages")
    hint: Optional[ReferencedHint] = None
    hints: Optional[FlattenedHints] = None
    sensitive: Optional[ReferencedSensitive] = None
    sensitives: Optional[FlattenedSensitives] = None
    source: Optional[ReferencedIdentifiedWorkstreamPatternEngineSource] = None
    sources: Optional[FlattenedIdentifiedWorkstreamPatternEngineSources] = None
    __properties = ["schema", "summary", "asset", "tag", "website", "anchor", "conversation", "person", "seed", "seeds", "summaries", "assets", "tags", "websites", "anchors", "conversations", "persons", "related", "current", "annotation", "annotations", "conversationMessage", "conversationMessages", "hint", "hints", "sensitive", "sensitives", "source", "sources"]

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
    def from_json(cls, json_str: str) -> WorkstreamSuggestion:
        """Create an instance of WorkstreamSuggestion from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tag
        if self.tag:
            _dict['tag'] = self.tag.to_dict()
        # override the default output from pydantic by calling `to_dict()` of website
        if self.website:
            _dict['website'] = self.website.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anchor
        if self.anchor:
            _dict['anchor'] = self.anchor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversation
        if self.conversation:
            _dict['conversation'] = self.conversation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of person
        if self.person:
            _dict['person'] = self.person.to_dict()
        # override the default output from pydantic by calling `to_dict()` of seed
        if self.seed:
            _dict['seed'] = self.seed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of seeds
        if self.seeds:
            _dict['seeds'] = self.seeds.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summaries
        if self.summaries:
            _dict['summaries'] = self.summaries.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of websites
        if self.websites:
            _dict['websites'] = self.websites.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anchors
        if self.anchors:
            _dict['anchors'] = self.anchors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversations
        if self.conversations:
            _dict['conversations'] = self.conversations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of persons
        if self.persons:
            _dict['persons'] = self.persons.to_dict()
        # override the default output from pydantic by calling `to_dict()` of related
        if self.related:
            _dict['related'] = self.related.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current
        if self.current:
            _dict['current'] = self.current.to_dict()
        # override the default output from pydantic by calling `to_dict()` of annotation
        if self.annotation:
            _dict['annotation'] = self.annotation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of annotations
        if self.annotations:
            _dict['annotations'] = self.annotations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversation_message
        if self.conversation_message:
            _dict['conversationMessage'] = self.conversation_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversation_messages
        if self.conversation_messages:
            _dict['conversationMessages'] = self.conversation_messages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hint
        if self.hint:
            _dict['hint'] = self.hint.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hints
        if self.hints:
            _dict['hints'] = self.hints.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sensitive
        if self.sensitive:
            _dict['sensitive'] = self.sensitive.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sensitives
        if self.sensitives:
            _dict['sensitives'] = self.sensitives.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sources
        if self.sources:
            _dict['sources'] = self.sources.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WorkstreamSuggestion:
        """Create an instance of WorkstreamSuggestion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WorkstreamSuggestion.parse_obj(obj)

        _obj = WorkstreamSuggestion.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "summary": ReferencedWorkstreamSummary.from_dict(obj.get("summary")) if obj.get("summary") is not None else None,
            "asset": ReferencedAsset.from_dict(obj.get("asset")) if obj.get("asset") is not None else None,
            "tag": ReferencedTag.from_dict(obj.get("tag")) if obj.get("tag") is not None else None,
            "website": ReferencedWebsite.from_dict(obj.get("website")) if obj.get("website") is not None else None,
            "anchor": ReferencedAnchor.from_dict(obj.get("anchor")) if obj.get("anchor") is not None else None,
            "conversation": ReferencedConversation.from_dict(obj.get("conversation")) if obj.get("conversation") is not None else None,
            "person": ReferencedPerson.from_dict(obj.get("person")) if obj.get("person") is not None else None,
            "seed": Seed.from_dict(obj.get("seed")) if obj.get("seed") is not None else None,
            "seeds": Seeds.from_dict(obj.get("seeds")) if obj.get("seeds") is not None else None,
            "summaries": FlattenedWorkstreamSummaries.from_dict(obj.get("summaries")) if obj.get("summaries") is not None else None,
            "assets": FlattenedAssets.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "tags": FlattenedTags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None,
            "websites": FlattenedWebsites.from_dict(obj.get("websites")) if obj.get("websites") is not None else None,
            "anchors": FlattenedAnchors.from_dict(obj.get("anchors")) if obj.get("anchors") is not None else None,
            "conversations": FlattenedConversations.from_dict(obj.get("conversations")) if obj.get("conversations") is not None else None,
            "persons": FlattenedPersons.from_dict(obj.get("persons")) if obj.get("persons") is not None else None,
            "related": WorkstreamSuggestions.from_dict(obj.get("related")) if obj.get("related") is not None else None,
            "current": WorkstreamSuggestion.from_dict(obj.get("current")) if obj.get("current") is not None else None,
            "annotation": ReferencedAnnotation.from_dict(obj.get("annotation")) if obj.get("annotation") is not None else None,
            "annotations": FlattenedAnnotations.from_dict(obj.get("annotations")) if obj.get("annotations") is not None else None,
            "conversation_message": ReferencedConversationMessage.from_dict(obj.get("conversationMessage")) if obj.get("conversationMessage") is not None else None,
            "conversation_messages": FlattenedConversationMessages.from_dict(obj.get("conversationMessages")) if obj.get("conversationMessages") is not None else None,
            "hint": ReferencedHint.from_dict(obj.get("hint")) if obj.get("hint") is not None else None,
            "hints": FlattenedHints.from_dict(obj.get("hints")) if obj.get("hints") is not None else None,
            "sensitive": ReferencedSensitive.from_dict(obj.get("sensitive")) if obj.get("sensitive") is not None else None,
            "sensitives": FlattenedSensitives.from_dict(obj.get("sensitives")) if obj.get("sensitives") is not None else None,
            "source": ReferencedIdentifiedWorkstreamPatternEngineSource.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "sources": FlattenedIdentifiedWorkstreamPatternEngineSources.from_dict(obj.get("sources")) if obj.get("sources") is not None else None
        })
        return _obj

from pieces_os_client.models.workstream_suggestions import WorkstreamSuggestions
WorkstreamSuggestion.update_forward_refs()

