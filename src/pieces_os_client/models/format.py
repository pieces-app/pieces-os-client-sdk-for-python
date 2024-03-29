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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.activities import Activities
from pieces_os_client.models.application import Application
from pieces_os_client.models.byte_descriptor import ByteDescriptor
from pieces_os_client.models.classification import Classification
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.file_format import FileFormat
from pieces_os_client.models.flattened_asset import FlattenedAsset
from pieces_os_client.models.fragment_format import FragmentFormat
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.relationship import Relationship
from pieces_os_client.models.role import Role
from typing import Optional, Set
from typing_extensions import Self

class Format(BaseModel):
    """
    A representation of Data for a particular Form Factor of an Asset.  Below asset HAS to be Flattened because it is a leaf node and must prevent cycles agressively.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    id: StrictStr
    creator: StrictStr
    classification: Classification
    icon: Optional[StrictStr] = None
    role: Role
    application: Application
    asset: FlattenedAsset
    bytes: ByteDescriptor
    created: GroupedTimestamp
    updated: GroupedTimestamp
    deleted: Optional[GroupedTimestamp] = None
    synced: Optional[GroupedTimestamp] = None
    cloud: Optional[StrictStr] = Field(default=None, description="This is a path used to determine what path this format lives at within the cloud.")
    fragment: Optional[FragmentFormat] = None
    file: Optional[FileFormat] = None
    analysis: Optional[Analysis] = None
    relationship: Optional[Relationship] = None
    activities: Optional[Activities] = None
    __properties: ClassVar[List[str]] = ["schema", "id", "creator", "classification", "icon", "role", "application", "asset", "bytes", "created", "updated", "deleted", "synced", "cloud", "fragment", "file", "analysis", "relationship", "activities"]

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
        """Create an instance of Format from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of classification
        if self.classification:
            _dict['classification'] = self.classification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of application
        if self.application:
            _dict['application'] = self.application.to_dict()
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bytes
        if self.bytes:
            _dict['bytes'] = self.bytes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleted
        if self.deleted:
            _dict['deleted'] = self.deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of synced
        if self.synced:
            _dict['synced'] = self.synced.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fragment
        if self.fragment:
            _dict['fragment'] = self.fragment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file
        if self.file:
            _dict['file'] = self.file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of analysis
        if self.analysis:
            _dict['analysis'] = self.analysis.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relationship
        if self.relationship:
            _dict['relationship'] = self.relationship.to_dict()
        # override the default output from pydantic by calling `to_dict()` of activities
        if self.activities:
            _dict['activities'] = self.activities.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Format from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "creator": obj.get("creator"),
            "classification": Classification.from_dict(obj["classification"]) if obj.get("classification") is not None else None,
            "icon": obj.get("icon"),
            "role": obj.get("role"),
            "application": Application.from_dict(obj["application"]) if obj.get("application") is not None else None,
            "asset": FlattenedAsset.from_dict(obj["asset"]) if obj.get("asset") is not None else None,
            "bytes": ByteDescriptor.from_dict(obj["bytes"]) if obj.get("bytes") is not None else None,
            "created": GroupedTimestamp.from_dict(obj["created"]) if obj.get("created") is not None else None,
            "updated": GroupedTimestamp.from_dict(obj["updated"]) if obj.get("updated") is not None else None,
            "deleted": GroupedTimestamp.from_dict(obj["deleted"]) if obj.get("deleted") is not None else None,
            "synced": GroupedTimestamp.from_dict(obj["synced"]) if obj.get("synced") is not None else None,
            "cloud": obj.get("cloud"),
            "fragment": FragmentFormat.from_dict(obj["fragment"]) if obj.get("fragment") is not None else None,
            "file": FileFormat.from_dict(obj["file"]) if obj.get("file") is not None else None,
            "analysis": Analysis.from_dict(obj["analysis"]) if obj.get("analysis") is not None else None,
            "relationship": Relationship.from_dict(obj["relationship"]) if obj.get("relationship") is not None else None,
            "activities": Activities.from_dict(obj["activities"]) if obj.get("activities") is not None else None
        })
        return _obj

from pieces_os_client.models.analysis import Analysis
# TODO: Rewrite to not use raise_errors
Format.model_rebuild(raise_errors=False)

