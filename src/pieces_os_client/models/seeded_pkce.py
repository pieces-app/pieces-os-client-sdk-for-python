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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.seeded_pkceadditionalparameters import SeededPKCEADDITIONALPARAMETERS

class SeededPKCE(BaseModel):
    """
    A model that initialized a PKCE Authentication Flow.  # noqa: E501
    """
    additional_parameters: Optional[SeededPKCEADDITIONALPARAMETERS] = Field(default=None, alias="ADDITIONAL_PARAMETERS")
    audience: Optional[StrictStr] = Field(default=None, description="The unique identifier of the target API you want to access. i.e. https://pieces.us.auth0.com/api/v2/")
    client_id: StrictStr = Field(default=..., description="Your application's Client ID.")
    code_challenge: StrictStr = Field(default=..., description="Generated challenge from the code_verifier.")
    code_challenge_method: StrictStr = Field(default=..., description="Method used to generate the challenge. The PKCE spec defines two methods, S256 and plain, however, Auth0 supports only S256 since the latter is discouraged.")
    domain: Optional[StrictStr] = Field(default=None, description="https://auth.pieces.services/authorize")
    invitation: Optional[StrictStr] = None
    nonce: StrictStr = Field(default=..., description="A local key that is held as the comparator to state, thus they should be the same.")
    organization: Optional[StrictStr] = None
    prompt: Optional[StrictStr] = Field(default=None, description=" To initiate a silent authentication request, use prompt=none (see Remarks for more info).")
    redirect_uri: Optional[StrictStr] = Field(default=None, description="http://localhost:8080/authentication/response")
    response_mode: Optional[StrictStr] = None
    response_type: StrictStr = Field(default=..., description="Indicates to Auth0 which OAuth 2.0 Flow you want to perform. Use code for Authorization Code Grant (PKCE) Flow.")
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    scope: conlist(StrictStr) = Field(default=..., description="The scopes which you want to request authorization for. These must be separated by a space. You can request any of the standard OpenID Connect (OIDC) scopes about users, such as profile and email, custom claims that must conform to a namespaced format, or any scopes supported by the target API (for example, read:contacts). Include offline_access to get a Refresh Token.")
    screen_hint: Optional[StrictStr] = Field(default=None, description="Provides a hint to Auth0 as to what flow should be displayed. The default behavior is to show a login page but you can override this by passing 'signup' to show the signup page instead.")
    state: StrictStr = Field(default=..., description="An opaque value the clients adds to the initial request that Auth0 includes when redirecting the back to the client. This value must be used by the client to prevent CSRF attacks.")
    __properties = ["ADDITIONAL_PARAMETERS", "audience", "client_id", "code_challenge", "code_challenge_method", "domain", "invitation", "nonce", "organization", "prompt", "redirect_uri", "response_mode", "response_type", "schema", "scope", "screen_hint", "state"]

    @validator('code_challenge_method')
    def code_challenge_method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('S256',):
            raise ValueError("must be one of enum values ('S256')")
        return value

    @validator('prompt')
    def prompt_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('login', 'none',):
            raise ValueError("must be one of enum values ('login', 'none')")
        return value

    @validator('response_mode')
    def response_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('form_post', 'web_message', 'fragment', 'query',):
            raise ValueError("must be one of enum values ('form_post', 'web_message', 'fragment', 'query')")
        return value

    @validator('response_type')
    def response_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('code', 'token', 'id_token',):
            raise ValueError("must be one of enum values ('code', 'token', 'id_token')")
        return value

    @validator('scope')
    def scope_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in ('offline_access', 'email', 'profile', 'openid',):
                raise ValueError("each list item must be one of ('offline_access', 'email', 'profile', 'openid')")
        return value

    @validator('screen_hint')
    def screen_hint_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('signup',):
            raise ValueError("must be one of enum values ('signup')")
        return value

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
    def from_json(cls, json_str: str) -> SeededPKCE:
        """Create an instance of SeededPKCE from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of additional_parameters
        if self.additional_parameters:
            _dict['ADDITIONAL_PARAMETERS'] = self.additional_parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededPKCE:
        """Create an instance of SeededPKCE from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededPKCE.parse_obj(obj)

        _obj = SeededPKCE.parse_obj({
            "additional_parameters": SeededPKCEADDITIONALPARAMETERS.from_dict(obj.get("ADDITIONAL_PARAMETERS")) if obj.get("ADDITIONAL_PARAMETERS") is not None else None,
            "audience": obj.get("audience"),
            "client_id": obj.get("client_id"),
            "code_challenge": obj.get("code_challenge"),
            "code_challenge_method": obj.get("code_challenge_method"),
            "domain": obj.get("domain"),
            "invitation": obj.get("invitation"),
            "nonce": obj.get("nonce"),
            "organization": obj.get("organization"),
            "prompt": obj.get("prompt"),
            "redirect_uri": obj.get("redirect_uri"),
            "response_mode": obj.get("response_mode"),
            "response_type": obj.get("response_type"),
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "scope": obj.get("scope"),
            "screen_hint": obj.get("screen_hint"),
            "state": obj.get("state")
        })
        return _obj


