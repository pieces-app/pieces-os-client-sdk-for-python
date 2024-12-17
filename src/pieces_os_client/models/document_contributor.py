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
from pieces_os_client.models.classification import Classification
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.person_basic_type import PersonBasicType
from pieces_os_client.models.transferable_string import TransferableString

class DocumentContributor(BaseModel):
    """
    A DocumentContributor is a preseeded representation of a Person  This can be used in the case of the browser, or in the IDE  If they are apart of an IDE, we can in the future provide git information (IE add a Git object for their commits)  person: this is most important part which is the email/name xyz  # noqa: E501
    """
    classification: Optional[Classification] = None
    person: PersonBasicType = Field(...)
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    updated: Optional[GroupedTimestamp] = None
    value: Optional[TransferableString] = None
    __properties = ["classification", "person", "schema", "updated", "value"]

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
    def from_json(cls, json_str: str) -> DocumentContributor:
        """Create an instance of DocumentContributor from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of classification
        if self.classification:
            _dict['classification'] = self.classification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of person
        if self.person:
            _dict['person'] = self.person.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DocumentContributor:
        """Create an instance of DocumentContributor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DocumentContributor.parse_obj(obj)

        _obj = DocumentContributor.parse_obj({
            "classification": Classification.from_dict(obj.get("classification")) if obj.get("classification") is not None else None,
            "person": PersonBasicType.from_dict(obj.get("person")) if obj.get("person") is not None else None,
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "updated": GroupedTimestamp.from_dict(obj.get("updated")) if obj.get("updated") is not None else None,
            "value": TransferableString.from_dict(obj.get("value")) if obj.get("value") is not None else None
        })
        return _obj


