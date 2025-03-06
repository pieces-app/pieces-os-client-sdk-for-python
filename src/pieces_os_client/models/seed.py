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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.seeded_anchor import SeededAnchor
from pieces_os_client.models.seeded_asset import SeededAsset
from pieces_os_client.models.seeded_person import SeededPerson
from pieces_os_client.models.seeded_website import SeededWebsite
from typing import Optional, Set
from typing_extensions import Self

class Seed(BaseModel):
    """
    A seed Model used to wrap a format or asset  Note: we will expand this now to support additional paramerters.  Note: however if create an asset, only pass in the asset, not passing in an asset in this case will cause the endpoint to fail.  TODO: for a breaking change update the type enum here to add support for the additional materials or remove it entirely.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    asset: Optional[SeededAsset] = None
    person: Optional[SeededPerson] = None
    anchor: Optional[SeededAnchor] = None
    website: Optional[SeededWebsite] = None
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["schema", "asset", "person", "anchor", "website", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SEEDED_FORMAT', 'SEEDED_ASSET']):
            raise ValueError("must be one of enum values ('SEEDED_FORMAT', 'SEEDED_ASSET')")
        return value

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
        """Create an instance of Seed from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of person
        if self.person:
            _dict['person'] = self.person.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anchor
        if self.anchor:
            _dict['anchor'] = self.anchor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of website
        if self.website:
            _dict['website'] = self.website.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Seed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "asset": SeededAsset.from_dict(obj["asset"]) if obj.get("asset") is not None else None,
            "person": SeededPerson.from_dict(obj["person"]) if obj.get("person") is not None else None,
            "anchor": SeededAnchor.from_dict(obj["anchor"]) if obj.get("anchor") is not None else None,
            "website": SeededWebsite.from_dict(obj["website"]) if obj.get("website") is not None else None,
            "type": obj.get("type")
        })
        return _obj


