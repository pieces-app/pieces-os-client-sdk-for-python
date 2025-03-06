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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.mechanism_enum import MechanismEnum
from pieces_os_client.models.score import Score
from pieces_os_client.models.sensitive_category_enum import SensitiveCategoryEnum
from pieces_os_client.models.sensitive_metadata import SensitiveMetadata
from pieces_os_client.models.sensitive_severity_enum import SensitiveSeverityEnum
from typing import Optional, Set
from typing_extensions import Self

class FlattenedSensitive(BaseModel):
    """
    This is a dereferenced representation of a sensitive pieces of data.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    id: StrictStr
    created: GroupedTimestamp
    updated: GroupedTimestamp
    deleted: Optional[GroupedTimestamp] = None
    asset: ReferencedAsset
    text: StrictStr
    mechanism: MechanismEnum
    category: SensitiveCategoryEnum
    severity: SensitiveSeverityEnum
    name: StrictStr
    description: StrictStr
    metadata: Optional[SensitiveMetadata] = None
    interactions: Optional[StrictInt] = Field(default=None, description="This is an optional value that will keep track of the number of times this has been interacted with.")
    score: Optional[Score] = None
    __properties: ClassVar[List[str]] = ["schema", "id", "created", "updated", "deleted", "asset", "text", "mechanism", "category", "severity", "name", "description", "metadata", "interactions", "score"]

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
        """Create an instance of FlattenedSensitive from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of deleted
        if self.deleted:
            _dict['deleted'] = self.deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of score
        if self.score:
            _dict['score'] = self.score.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlattenedSensitive from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "created": GroupedTimestamp.from_dict(obj["created"]) if obj.get("created") is not None else None,
            "updated": GroupedTimestamp.from_dict(obj["updated"]) if obj.get("updated") is not None else None,
            "deleted": GroupedTimestamp.from_dict(obj["deleted"]) if obj.get("deleted") is not None else None,
            "asset": ReferencedAsset.from_dict(obj["asset"]) if obj.get("asset") is not None else None,
            "text": obj.get("text"),
            "mechanism": obj.get("mechanism"),
            "category": obj.get("category"),
            "severity": obj.get("severity"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "metadata": SensitiveMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "interactions": obj.get("interactions"),
            "score": Score.from_dict(obj["score"]) if obj.get("score") is not None else None
        })
        return _obj

from pieces_os_client.models.referenced_asset import ReferencedAsset
# TODO: Rewrite to not use raise_errors
FlattenedSensitive.model_rebuild(raise_errors=False)

