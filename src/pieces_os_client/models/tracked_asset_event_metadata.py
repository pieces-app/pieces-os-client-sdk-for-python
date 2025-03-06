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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.tracked_asset_event_creation_metadata import TrackedAssetEventCreationMetadata
from pieces_os_client.models.tracked_asset_event_format_reclassification_metadata import TrackedAssetEventFormatReclassificationMetadata
from pieces_os_client.models.tracked_asset_event_rename_metadata import TrackedAssetEventRenameMetadata
from typing import Optional, Set
from typing_extensions import Self

class TrackedAssetEventMetadata(BaseModel):
    """
    TrackedAssetEventMetadata
    """ # noqa: E501
    reclassification: Optional[TrackedAssetEventFormatReclassificationMetadata] = None
    creation: Optional[TrackedAssetEventCreationMetadata] = None
    rename: Optional[TrackedAssetEventRenameMetadata] = None
    tag: Optional[ReferencedTag] = None
    website: Optional[ReferencedWebsite] = None
    person: Optional[ReferencedPerson] = None
    sensitive: Optional[ReferencedSensitive] = None
    share: Optional[ReferencedShare] = None
    search: Optional[TrackedAssetsEventSearchMetadata] = None
    annotation: Optional[ReferencedAnnotation] = None
    hint: Optional[ReferencedHint] = None
    anchor: Optional[ReferencedAnchor] = None
    __properties: ClassVar[List[str]] = ["reclassification", "creation", "rename", "tag", "website", "person", "sensitive", "share", "search", "annotation", "hint", "anchor"]

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
        """Create an instance of TrackedAssetEventMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of reclassification
        if self.reclassification:
            _dict['reclassification'] = self.reclassification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of creation
        if self.creation:
            _dict['creation'] = self.creation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rename
        if self.rename:
            _dict['rename'] = self.rename.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tag
        if self.tag:
            _dict['tag'] = self.tag.to_dict()
        # override the default output from pydantic by calling `to_dict()` of website
        if self.website:
            _dict['website'] = self.website.to_dict()
        # override the default output from pydantic by calling `to_dict()` of person
        if self.person:
            _dict['person'] = self.person.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sensitive
        if self.sensitive:
            _dict['sensitive'] = self.sensitive.to_dict()
        # override the default output from pydantic by calling `to_dict()` of share
        if self.share:
            _dict['share'] = self.share.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search
        if self.search:
            _dict['search'] = self.search.to_dict()
        # override the default output from pydantic by calling `to_dict()` of annotation
        if self.annotation:
            _dict['annotation'] = self.annotation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hint
        if self.hint:
            _dict['hint'] = self.hint.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anchor
        if self.anchor:
            _dict['anchor'] = self.anchor.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrackedAssetEventMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reclassification": TrackedAssetEventFormatReclassificationMetadata.from_dict(obj["reclassification"]) if obj.get("reclassification") is not None else None,
            "creation": TrackedAssetEventCreationMetadata.from_dict(obj["creation"]) if obj.get("creation") is not None else None,
            "rename": TrackedAssetEventRenameMetadata.from_dict(obj["rename"]) if obj.get("rename") is not None else None,
            "tag": ReferencedTag.from_dict(obj["tag"]) if obj.get("tag") is not None else None,
            "website": ReferencedWebsite.from_dict(obj["website"]) if obj.get("website") is not None else None,
            "person": ReferencedPerson.from_dict(obj["person"]) if obj.get("person") is not None else None,
            "sensitive": ReferencedSensitive.from_dict(obj["sensitive"]) if obj.get("sensitive") is not None else None,
            "share": ReferencedShare.from_dict(obj["share"]) if obj.get("share") is not None else None,
            "search": TrackedAssetsEventSearchMetadata.from_dict(obj["search"]) if obj.get("search") is not None else None,
            "annotation": ReferencedAnnotation.from_dict(obj["annotation"]) if obj.get("annotation") is not None else None,
            "hint": ReferencedHint.from_dict(obj["hint"]) if obj.get("hint") is not None else None,
            "anchor": ReferencedAnchor.from_dict(obj["anchor"]) if obj.get("anchor") is not None else None
        })
        return _obj

from pieces_os_client.models.referenced_anchor import ReferencedAnchor
from pieces_os_client.models.referenced_annotation import ReferencedAnnotation
from pieces_os_client.models.referenced_hint import ReferencedHint
from pieces_os_client.models.referenced_person import ReferencedPerson
from pieces_os_client.models.referenced_sensitive import ReferencedSensitive
from pieces_os_client.models.referenced_share import ReferencedShare
from pieces_os_client.models.referenced_tag import ReferencedTag
from pieces_os_client.models.referenced_website import ReferencedWebsite
from pieces_os_client.models.tracked_assets_event_search_metadata import TrackedAssetsEventSearchMetadata
# TODO: Rewrite to not use raise_errors
TrackedAssetEventMetadata.model_rebuild(raise_errors=False)

