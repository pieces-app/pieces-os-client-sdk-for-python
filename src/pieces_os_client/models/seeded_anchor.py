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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.anchor_type_enum import AnchorTypeEnum
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.platform_enum import PlatformEnum
from typing import Optional, Set
from typing_extensions import Self

class SeededAnchor(BaseModel):
    """
    SeededAnchor
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    type: AnchorTypeEnum
    watch: Optional[StrictBool] = None
    fullpath: StrictStr
    asset: Optional[StrictStr] = Field(default=None, description="You may associate a SeededAnchor with an asset")
    platform: Optional[PlatformEnum] = None
    name: Optional[StrictStr] = None
    annotations: Optional[List[SeededAnnotation]] = None
    conversation: Optional[StrictStr] = None
    persons: Optional[FlattenedPersons] = None
    __properties: ClassVar[List[str]] = ["schema", "type", "watch", "fullpath", "asset", "platform", "name", "annotations", "conversation", "persons"]

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
        """Create an instance of SeededAnchor from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in annotations (list)
        _items = []
        if self.annotations:
            for _item_annotations in self.annotations:
                if _item_annotations:
                    _items.append(_item_annotations.to_dict())
            _dict['annotations'] = _items
        # override the default output from pydantic by calling `to_dict()` of persons
        if self.persons:
            _dict['persons'] = self.persons.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SeededAnchor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "type": obj.get("type"),
            "watch": obj.get("watch"),
            "fullpath": obj.get("fullpath"),
            "asset": obj.get("asset"),
            "platform": obj.get("platform"),
            "name": obj.get("name"),
            "annotations": [SeededAnnotation.from_dict(_item) for _item in obj["annotations"]] if obj.get("annotations") is not None else None,
            "conversation": obj.get("conversation"),
            "persons": FlattenedPersons.from_dict(obj["persons"]) if obj.get("persons") is not None else None
        })
        return _obj

from pieces_os_client.models.flattened_persons import FlattenedPersons
from pieces_os_client.models.seeded_annotation import SeededAnnotation
# TODO: Rewrite to not use raise_errors
SeededAnchor.model_rebuild(raise_errors=False)

