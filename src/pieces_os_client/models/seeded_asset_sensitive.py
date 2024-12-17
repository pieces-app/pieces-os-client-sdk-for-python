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
from pydantic import BaseModel, Field, StrictStr
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.mechanism_enum import MechanismEnum
from pieces_os_client.models.sensitive_category_enum import SensitiveCategoryEnum
from pieces_os_client.models.sensitive_metadata import SensitiveMetadata
from pieces_os_client.models.sensitive_severity_enum import SensitiveSeverityEnum

class SeededAssetSensitive(BaseModel):
    """
    This is the seededAssetSensitive, this does not have an id yet as we will add it on the server side.  can optionally pass in our mechanism here, as the default will be manual unless specified.  This is different that hte SeededSensitive as this is pre-before the asset has been created.(but added when the asset is created.  # noqa: E501
    """
    category: SensitiveCategoryEnum = Field(...)
    description: StrictStr = Field(...)
    mechanism: Optional[MechanismEnum] = None
    metadata: Optional[SensitiveMetadata] = None
    name: StrictStr = Field(...)
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    severity: SensitiveSeverityEnum = Field(...)
    text: StrictStr = Field(default=..., description="this is the string representative of the sensative piece of data.")
    __properties = ["category", "description", "mechanism", "metadata", "name", "schema", "severity", "text"]

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
    def from_json(cls, json_str: str) -> SeededAssetSensitive:
        """Create an instance of SeededAssetSensitive from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededAssetSensitive:
        """Create an instance of SeededAssetSensitive from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededAssetSensitive.parse_obj(obj)

        _obj = SeededAssetSensitive.parse_obj({
            "category": obj.get("category"),
            "description": obj.get("description"),
            "mechanism": obj.get("mechanism"),
            "metadata": SensitiveMetadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "name": obj.get("name"),
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "severity": obj.get("severity"),
            "text": obj.get("text")
        })
        return _obj


