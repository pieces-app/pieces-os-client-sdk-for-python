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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.flattened_anchors import FlattenedAnchors
from pieces_os_client.models.flattened_assets import FlattenedAssets
from pieces_os_client.models.flattened_conversations import FlattenedConversations
from pieces_os_client.models.flattened_persons import FlattenedPersons
from pieces_os_client.models.flattened_tags import FlattenedTags
from pieces_os_client.models.flattened_websites import FlattenedWebsites
from pieces_os_client.models.flattened_workstream_summaries import FlattenedWorkstreamSummaries
from pieces_os_client.models.referenced_anchor import ReferencedAnchor
from pieces_os_client.models.referenced_asset import ReferencedAsset
from pieces_os_client.models.referenced_conversation import ReferencedConversation
from pieces_os_client.models.referenced_person import ReferencedPerson
from pieces_os_client.models.referenced_tag import ReferencedTag
from pieces_os_client.models.referenced_website import ReferencedWebsite
from pieces_os_client.models.referenced_workstream_summary import ReferencedWorkstreamSummary
from pieces_os_client.models.seed import Seed
from pieces_os_client.models.seeds import Seeds
from typing import Optional, Set
from typing_extensions import Self

class WorkstreamSuggestion(BaseModel):
    """
    This is an individual material that is apart of the workstream feed. might want to also consider plural uuids ie top websites/tags/and others..  related: this is an optional field that will only be calculated for first degree relationships.          ie. an anchor may have related.iterable.first.persons that are not associated but related.          via the workstream patturn engine.  current: if current is defined then this is the current viewed object
    """ # noqa: E501
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
    __properties: ClassVar[List[str]] = ["schema", "summary", "asset", "tag", "website", "anchor", "conversation", "person", "seed", "seeds", "summaries", "assets", "tags", "websites", "anchors", "conversations", "persons", "related", "current"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WorkstreamSuggestion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkstreamSuggestion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "summary": ReferencedWorkstreamSummary.from_dict(obj["summary"]) if obj.get("summary") is not None else None,
            "asset": ReferencedAsset.from_dict(obj["asset"]) if obj.get("asset") is not None else None,
            "tag": ReferencedTag.from_dict(obj["tag"]) if obj.get("tag") is not None else None,
            "website": ReferencedWebsite.from_dict(obj["website"]) if obj.get("website") is not None else None,
            "anchor": ReferencedAnchor.from_dict(obj["anchor"]) if obj.get("anchor") is not None else None,
            "conversation": ReferencedConversation.from_dict(obj["conversation"]) if obj.get("conversation") is not None else None,
            "person": ReferencedPerson.from_dict(obj["person"]) if obj.get("person") is not None else None,
            "seed": Seed.from_dict(obj["seed"]) if obj.get("seed") is not None else None,
            "seeds": Seeds.from_dict(obj["seeds"]) if obj.get("seeds") is not None else None,
            "summaries": FlattenedWorkstreamSummaries.from_dict(obj["summaries"]) if obj.get("summaries") is not None else None,
            "assets": FlattenedAssets.from_dict(obj["assets"]) if obj.get("assets") is not None else None,
            "tags": FlattenedTags.from_dict(obj["tags"]) if obj.get("tags") is not None else None,
            "websites": FlattenedWebsites.from_dict(obj["websites"]) if obj.get("websites") is not None else None,
            "anchors": FlattenedAnchors.from_dict(obj["anchors"]) if obj.get("anchors") is not None else None,
            "conversations": FlattenedConversations.from_dict(obj["conversations"]) if obj.get("conversations") is not None else None,
            "persons": FlattenedPersons.from_dict(obj["persons"]) if obj.get("persons") is not None else None,
            "related": WorkstreamSuggestions.from_dict(obj["related"]) if obj.get("related") is not None else None,
            "current": WorkstreamSuggestion.from_dict(obj["current"]) if obj.get("current") is not None else None
        })
        return _obj

from pieces_os_client.models.workstream_suggestions import WorkstreamSuggestions
# TODO: Rewrite to not use raise_errors
WorkstreamSuggestion.model_rebuild(raise_errors=False)

