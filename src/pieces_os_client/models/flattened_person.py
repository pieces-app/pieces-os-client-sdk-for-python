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


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.mechanism_enum import MechanismEnum
from pieces_os_client.models.person_access import PersonAccess
from pieces_os_client.models.person_type import PersonType
from pieces_os_client.models.score import Score

class FlattenedPerson(BaseModel):
    """
    if expiration is add then, after the alloted expiration date the user will only have view && comment only permissions. Only present in the case there is a scope such as a defined collection/asset...  if asset is passed then that means this person belongs to a scoped asset.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    id: StrictStr = Field(...)
    created: GroupedTimestamp = Field(...)
    updated: GroupedTimestamp = Field(...)
    deleted: Optional[GroupedTimestamp] = None
    type: PersonType = Field(...)
    assets: Optional[FlattenedAssets] = None
    mechanisms: Optional[Dict[str, MechanismEnum]] = Field(None, description="This is a Map<String, MechanismEnum> where the the key is an asset id.")
    interactions: Optional[StrictInt] = Field(None, description="This is an optional value that will keep track of the number of times this has been interacted with.")
    access: Optional[Dict[str, PersonAccess]] = Field(None, description="This is a Map<String, PersonAccess> where the the key is an asset id.")
    tags: Optional[FlattenedTags] = None
    websites: Optional[FlattenedWebsites] = None
    models: Optional[Dict[str, PersonModel]] = Field(None, description="This is a Map<String, PersonModel>, where the the key is an asset id.")
    annotations: Optional[FlattenedAnnotations] = None
    score: Optional[Score] = None
    summaries: Optional[FlattenedWorkstreamSummaries] = None
    __properties = ["schema", "id", "created", "updated", "deleted", "type", "assets", "mechanisms", "interactions", "access", "tags", "websites", "models", "annotations", "score", "summaries"]

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
    def from_json(cls, json_str: str) -> FlattenedPerson:
        """Create an instance of FlattenedPerson from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleted
        if self.deleted:
            _dict['deleted'] = self.deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in access (dict)
        _field_dict = {}
        if self.access:
            for _key in self.access:
                if self.access[_key]:
                    _field_dict[_key] = self.access[_key].to_dict()
            _dict['access'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of websites
        if self.websites:
            _dict['websites'] = self.websites.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in models (dict)
        _field_dict = {}
        if self.models:
            for _key in self.models:
                if self.models[_key]:
                    _field_dict[_key] = self.models[_key].to_dict()
            _dict['models'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of annotations
        if self.annotations:
            _dict['annotations'] = self.annotations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of score
        if self.score:
            _dict['score'] = self.score.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summaries
        if self.summaries:
            _dict['summaries'] = self.summaries.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FlattenedPerson:
        """Create an instance of FlattenedPerson from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FlattenedPerson.parse_obj(obj)

        _obj = FlattenedPerson.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "created": GroupedTimestamp.from_dict(obj.get("created")) if obj.get("created") is not None else None,
            "updated": GroupedTimestamp.from_dict(obj.get("updated")) if obj.get("updated") is not None else None,
            "deleted": GroupedTimestamp.from_dict(obj.get("deleted")) if obj.get("deleted") is not None else None,
            "type": PersonType.from_dict(obj.get("type")) if obj.get("type") is not None else None,
            "assets": FlattenedAssets.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "mechanisms": dict((_k, _v) for _k, _v in obj.get("mechanisms").items()),
            "interactions": obj.get("interactions"),
            "access": dict(
                (_k, PersonAccess.from_dict(_v))
                for _k, _v in obj.get("access").items()
            )
            if obj.get("access") is not None
            else None,
            "tags": FlattenedTags.from_dict(obj.get("tags")) if obj.get("tags") is not None else None,
            "websites": FlattenedWebsites.from_dict(obj.get("websites")) if obj.get("websites") is not None else None,
            "models": dict(
                (_k, PersonModel.from_dict(_v))
                for _k, _v in obj.get("models").items()
            )
            if obj.get("models") is not None
            else None,
            "annotations": FlattenedAnnotations.from_dict(obj.get("annotations")) if obj.get("annotations") is not None else None,
            "score": Score.from_dict(obj.get("score")) if obj.get("score") is not None else None,
            "summaries": FlattenedWorkstreamSummaries.from_dict(obj.get("summaries")) if obj.get("summaries") is not None else None
        })
        return _obj

from pieces_os_client.models.flattened_annotations import FlattenedAnnotations
from pieces_os_client.models.flattened_assets import FlattenedAssets
from pieces_os_client.models.flattened_tags import FlattenedTags
from pieces_os_client.models.flattened_websites import FlattenedWebsites
from pieces_os_client.models.flattened_workstream_summaries import FlattenedWorkstreamSummaries
from pieces_os_client.models.person_model import PersonModel
FlattenedPerson.update_forward_refs()

