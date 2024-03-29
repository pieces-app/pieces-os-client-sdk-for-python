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

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.activities import Activities
from pieces_os_client.models.anchors import Anchors
from pieces_os_client.models.annotations import Annotations
from pieces_os_client.models.conversations import Conversations
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.formats import Formats
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.hints import Hints
from pieces_os_client.models.mechanism_enum import MechanismEnum
from pieces_os_client.models.persons import Persons
from pieces_os_client.models.preview import Preview
from pieces_os_client.models.referenced_format import ReferencedFormat
from pieces_os_client.models.score import Score
from pieces_os_client.models.sensitives import Sensitives
from pieces_os_client.models.shares import Shares
from pieces_os_client.models.tags import Tags
from pieces_os_client.models.websites import Websites
from typing import Optional, Set
from typing_extensions import Self

class Asset(BaseModel):
    """
    An Asset Model representing data extracted from an Application connecting a group of data containing one or more Formats.  Below formats, preview, and original CAN to be pollinated (DAG Unsafe) because it is a root node and it's child leaf nodes will prevent cycles agressively.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    id: StrictStr = Field(description="The globally available UID representing the asset in the Database, both locally and in the cloud.")
    name: Optional[StrictStr] = None
    creator: StrictStr
    created: GroupedTimestamp
    updated: GroupedTimestamp
    synced: Optional[GroupedTimestamp] = None
    deleted: Optional[GroupedTimestamp] = None
    formats: Formats
    preview: Preview
    original: ReferencedFormat
    shares: Optional[Shares] = None
    mechanism: MechanismEnum
    websites: Optional[Websites] = None
    interacted: Optional[GroupedTimestamp] = None
    tags: Optional[Tags] = None
    sensitives: Optional[Sensitives] = None
    persons: Optional[Persons] = None
    curated: Optional[StrictBool] = Field(default=None, description="This is an optional boolean that will flag that this asset came from a currated collection.")
    discovered: Optional[StrictBool] = None
    activities: Optional[Activities] = None
    score: Optional[Score] = None
    favorited: Optional[StrictBool] = None
    pseudo: Optional[StrictBool] = Field(default=None, description="This will determine if this is a asset that the user did not explicitly save.")
    annotations: Optional[Annotations] = None
    hints: Optional[Hints] = None
    anchors: Optional[Anchors] = None
    conversations: Optional[Conversations] = None
    demo: Optional[StrictBool] = Field(default=None, description="This will let us know if this asset was generated as a 'demo' snippet")
    __properties: ClassVar[List[str]] = ["schema", "id", "name", "creator", "created", "updated", "synced", "deleted", "formats", "preview", "original", "shares", "mechanism", "websites", "interacted", "tags", "sensitives", "persons", "curated", "discovered", "activities", "score", "favorited", "pseudo", "annotations", "hints", "anchors", "conversations", "demo"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Asset from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of synced
        if self.synced:
            _dict['synced'] = self.synced.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleted
        if self.deleted:
            _dict['deleted'] = self.deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of formats
        if self.formats:
            _dict['formats'] = self.formats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of preview
        if self.preview:
            _dict['preview'] = self.preview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of original
        if self.original:
            _dict['original'] = self.original.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shares
        if self.shares:
            _dict['shares'] = self.shares.to_dict()
        # override the default output from pydantic by calling `to_dict()` of websites
        if self.websites:
            _dict['websites'] = self.websites.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interacted
        if self.interacted:
            _dict['interacted'] = self.interacted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sensitives
        if self.sensitives:
            _dict['sensitives'] = self.sensitives.to_dict()
        # override the default output from pydantic by calling `to_dict()` of persons
        if self.persons:
            _dict['persons'] = self.persons.to_dict()
        # override the default output from pydantic by calling `to_dict()` of activities
        if self.activities:
            _dict['activities'] = self.activities.to_dict()
        # override the default output from pydantic by calling `to_dict()` of score
        if self.score:
            _dict['score'] = self.score.to_dict()
        # override the default output from pydantic by calling `to_dict()` of annotations
        if self.annotations:
            _dict['annotations'] = self.annotations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hints
        if self.hints:
            _dict['hints'] = self.hints.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anchors
        if self.anchors:
            _dict['anchors'] = self.anchors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversations
        if self.conversations:
            _dict['conversations'] = self.conversations.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Asset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "creator": obj.get("creator"),
            "created": GroupedTimestamp.from_dict(obj["created"]) if obj.get("created") is not None else None,
            "updated": GroupedTimestamp.from_dict(obj["updated"]) if obj.get("updated") is not None else None,
            "synced": GroupedTimestamp.from_dict(obj["synced"]) if obj.get("synced") is not None else None,
            "deleted": GroupedTimestamp.from_dict(obj["deleted"]) if obj.get("deleted") is not None else None,
            "formats": Formats.from_dict(obj["formats"]) if obj.get("formats") is not None else None,
            "preview": Preview.from_dict(obj["preview"]) if obj.get("preview") is not None else None,
            "original": ReferencedFormat.from_dict(obj["original"]) if obj.get("original") is not None else None,
            "shares": Shares.from_dict(obj["shares"]) if obj.get("shares") is not None else None,
            "mechanism": obj.get("mechanism"),
            "websites": Websites.from_dict(obj["websites"]) if obj.get("websites") is not None else None,
            "interacted": GroupedTimestamp.from_dict(obj["interacted"]) if obj.get("interacted") is not None else None,
            "tags": Tags.from_dict(obj["tags"]) if obj.get("tags") is not None else None,
            "sensitives": Sensitives.from_dict(obj["sensitives"]) if obj.get("sensitives") is not None else None,
            "persons": Persons.from_dict(obj["persons"]) if obj.get("persons") is not None else None,
            "curated": obj.get("curated"),
            "discovered": obj.get("discovered"),
            "activities": Activities.from_dict(obj["activities"]) if obj.get("activities") is not None else None,
            "score": Score.from_dict(obj["score"]) if obj.get("score") is not None else None,
            "favorited": obj.get("favorited"),
            "pseudo": obj.get("pseudo"),
            "annotations": Annotations.from_dict(obj["annotations"]) if obj.get("annotations") is not None else None,
            "hints": Hints.from_dict(obj["hints"]) if obj.get("hints") is not None else None,
            "anchors": Anchors.from_dict(obj["anchors"]) if obj.get("anchors") is not None else None,
            "conversations": Conversations.from_dict(obj["conversations"]) if obj.get("conversations") is not None else None,
            "demo": obj.get("demo")
        })
        return _obj


