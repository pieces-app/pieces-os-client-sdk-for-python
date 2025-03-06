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
from pieces_os_client.models.referenced_conversation import ReferencedConversation
from pieces_os_client.models.seeded_range_conversation_grounding_association import SeededRangeConversationGroundingAssociation
from typing import Optional, Set
from typing_extensions import Self

class SeededRangeConversationAssociation(BaseModel):
    """
    SeededRangeConversationAssociation
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    reference: ReferencedConversation
    grounding: Optional[SeededRangeConversationGroundingAssociation] = None
    __properties: ClassVar[List[str]] = ["schema", "reference", "grounding"]

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
        """Create an instance of SeededRangeConversationAssociation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of reference
        if self.reference:
            _dict['reference'] = self.reference.to_dict()
        # override the default output from pydantic by calling `to_dict()` of grounding
        if self.grounding:
            _dict['grounding'] = self.grounding.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SeededRangeConversationAssociation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "reference": ReferencedConversation.from_dict(obj["reference"]) if obj.get("reference") is not None else None,
            "grounding": SeededRangeConversationGroundingAssociation.from_dict(obj["grounding"]) if obj.get("grounding") is not None else None
        })
        return _obj


