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

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.application_name_enum import ApplicationNameEnum
from pieces_os_client.models.capabilities_enum import CapabilitiesEnum
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.mechanism_enum import MechanismEnum
from pieces_os_client.models.platform_enum import PlatformEnum
from pieces_os_client.models.privacy_enum import PrivacyEnum
from typing import Optional, Set
from typing_extensions import Self

class Application(BaseModel):
    """
    A Model to describe what application a format/analytics event originated.  mechanism: This will let us know where this came from. ie.only 2 enums are used here or else throw and error. default mechanism here is MANUAL- meaning that this came from our user Connecting an application. INTERNAL - means that this came from a shareable link
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    id: StrictStr = Field(description="The ID of the application at the device level")
    name: ApplicationNameEnum
    version: StrictStr = Field(description="This is the specific version number 0.0.0")
    platform: PlatformEnum
    onboarded: StrictBool
    privacy: PrivacyEnum
    capabilities: Optional[CapabilitiesEnum] = None
    mechanism: Optional[MechanismEnum] = None
    automatic_unload: Optional[StrictBool] = Field(default=None, description="This is a proper that will let us know if we will proactivity unload all of your machine learning models.by default this is false.", alias="automaticUnload")
    __properties: ClassVar[List[str]] = ["schema", "id", "name", "version", "platform", "onboarded", "privacy", "capabilities", "mechanism", "automaticUnload"]

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
        """Create an instance of Application from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Application from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "version": obj.get("version"),
            "platform": obj.get("platform"),
            "onboarded": obj.get("onboarded"),
            "privacy": obj.get("privacy"),
            "capabilities": obj.get("capabilities"),
            "mechanism": obj.get("mechanism"),
            "automaticUnload": obj.get("automaticUnload")
        })
        return _obj


