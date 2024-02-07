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
from pieces_os_client.models.model import Model


class FlattenedOCRAnalysis(BaseModel):
    """
    [DAG Safe] Ocr Analysis that will reference FlattenedFormats.  # noqa: E501
    """

    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    id: StrictStr = Field(...)
    raw: ReferencedFormat = Field(...)
    hocr: ReferencedFormat = Field(...)
    model: Model = Field(...)
    image: StrictStr = Field(
        ..., description="this is a refernece to the image analysis."
    )
    __properties = ["schema", "id", "raw", "hocr", "model", "image"]

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
    def from_json(cls, json_str: str) -> FlattenedOCRAnalysis:
        """Create an instance of FlattenedOCRAnalysis from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict["schema"] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of raw
        if self.raw:
            _dict["raw"] = self.raw.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hocr
        if self.hocr:
            _dict["hocr"] = self.hocr.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict["model"] = self.model.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FlattenedOCRAnalysis:
        """Create an instance of FlattenedOCRAnalysis from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FlattenedOCRAnalysis.parse_obj(obj)

        _obj = FlattenedOCRAnalysis.parse_obj(
            {
                "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema"))
                if obj.get("schema") is not None
                else None,
                "id": obj.get("id"),
                "raw": ReferencedFormat.from_dict(obj.get("raw"))
                if obj.get("raw") is not None
                else None,
                "hocr": ReferencedFormat.from_dict(obj.get("hocr"))
                if obj.get("hocr") is not None
                else None,
                "model": Model.from_dict(obj.get("model"))
                if obj.get("model") is not None
                else None,
                "image": obj.get("image"),
            }
        )
        return _obj


from pieces_os_client.models.referenced_format import ReferencedFormat

# FlattenedOCRAnalysis.update_forward_refs()
