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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.anonymous_temporal_range import AnonymousTemporalRange
from pieces_os_client.models.auth0_open_ai_user_metadata import Auth0OpenAIUserMetadata
from pieces_os_client.models.auth0_user_allocation_metadata import Auth0UserAllocationMetadata
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from typing import Optional, Set
from typing_extensions import Self

class Auth0UserMetadata(BaseModel):
    """
    User Metadata from Auth0
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    global_id: StrictStr
    cloud_key: Optional[StrictStr] = None
    stripe_customer_id: Optional[StrictStr] = Field(default=None, description="A customer ID that is added to the user in the case of payments")
    vanityname: Optional[StrictStr] = Field(default=None, description="this is the vanityname of the user.(set from their custom CNAME dns record.) ie mark.pieces.cloud where \"mark\" is the vanityname.")
    allocation: Optional[Auth0UserAllocationMetadata] = None
    open_ai: Optional[Auth0OpenAIUserMetadata] = Field(default=None, alias="open_AI")
    beta: Optional[AnonymousTemporalRange] = None
    __properties: ClassVar[List[str]] = ["schema", "global_id", "cloud_key", "stripe_customer_id", "vanityname", "allocation", "open_AI", "beta"]

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
        """Create an instance of Auth0UserMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of allocation
        if self.allocation:
            _dict['allocation'] = self.allocation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of open_ai
        if self.open_ai:
            _dict['open_AI'] = self.open_ai.to_dict()
        # override the default output from pydantic by calling `to_dict()` of beta
        if self.beta:
            _dict['beta'] = self.beta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Auth0UserMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "global_id": obj.get("global_id"),
            "cloud_key": obj.get("cloud_key"),
            "stripe_customer_id": obj.get("stripe_customer_id"),
            "vanityname": obj.get("vanityname"),
            "allocation": Auth0UserAllocationMetadata.from_dict(obj["allocation"]) if obj.get("allocation") is not None else None,
            "open_AI": Auth0OpenAIUserMetadata.from_dict(obj["open_AI"]) if obj.get("open_AI") is not None else None,
            "beta": AnonymousTemporalRange.from_dict(obj["beta"]) if obj.get("beta") is not None else None
        })
        return _obj


