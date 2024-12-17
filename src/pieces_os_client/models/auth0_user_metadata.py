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
from pieces_os_client.models.anonymous_temporal_range import AnonymousTemporalRange
from pieces_os_client.models.auth0_open_ai_user_metadata import Auth0OpenAIUserMetadata
from pieces_os_client.models.auth0_user_allocation_metadata import Auth0UserAllocationMetadata
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema

class Auth0UserMetadata(BaseModel):
    """
    User Metadata from Auth0  # noqa: E501
    """
    allocation: Optional[Auth0UserAllocationMetadata] = None
    beta: Optional[AnonymousTemporalRange] = None
    cloud_key: Optional[StrictStr] = None
    global_id: StrictStr = Field(...)
    open_ai: Optional[Auth0OpenAIUserMetadata] = Field(default=None, alias="open_AI")
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    stripe_customer_id: Optional[StrictStr] = Field(default=None, description="A customer ID that is added to the user in the case of payments")
    vanityname: Optional[StrictStr] = Field(default=None, description="this is the vanityname of the user.(set from their custom CNAME dns record.) ie mark.pieces.cloud where \"mark\" is the vanityname.")
    __properties = ["allocation", "beta", "cloud_key", "global_id", "open_AI", "schema", "stripe_customer_id", "vanityname"]

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
    def from_json(cls, json_str: str) -> Auth0UserMetadata:
        """Create an instance of Auth0UserMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of allocation
        if self.allocation:
            _dict['allocation'] = self.allocation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of beta
        if self.beta:
            _dict['beta'] = self.beta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of open_ai
        if self.open_ai:
            _dict['open_AI'] = self.open_ai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Auth0UserMetadata:
        """Create an instance of Auth0UserMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Auth0UserMetadata.parse_obj(obj)

        _obj = Auth0UserMetadata.parse_obj({
            "allocation": Auth0UserAllocationMetadata.from_dict(obj.get("allocation")) if obj.get("allocation") is not None else None,
            "beta": AnonymousTemporalRange.from_dict(obj.get("beta")) if obj.get("beta") is not None else None,
            "cloud_key": obj.get("cloud_key"),
            "global_id": obj.get("global_id"),
            "open_ai": Auth0OpenAIUserMetadata.from_dict(obj.get("open_AI")) if obj.get("open_AI") is not None else None,
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "stripe_customer_id": obj.get("stripe_customer_id"),
            "vanityname": obj.get("vanityname")
        })
        return _obj


