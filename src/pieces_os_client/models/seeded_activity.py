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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.application import Application
from pieces_os_client.models.mechanism_enum import MechanismEnum
from pieces_os_client.models.referenced_asset import ReferencedAsset
from pieces_os_client.models.referenced_conversation import ReferencedConversation
from pieces_os_client.models.referenced_format import ReferencedFormat
from pieces_os_client.models.referenced_user import ReferencedUser
from pieces_os_client.models.seeded_connector_tracking import SeededConnectorTracking
from typing import Optional, Set
from typing_extensions import Self

class SeededActivity(BaseModel):
    """
    This is the preseed to a full blown Activity.  This is the minimum information needed to create an Activity, used within our [POST] /activities/create  if mechenism is not passed in we will default to AUTOMATIC  NOT required to pass in an asset/user/format.
    """ # noqa: E501
    event: SeededConnectorTracking
    application: Application
    asset: Optional[ReferencedAsset] = None
    user: Optional[ReferencedUser] = None
    format: Optional[ReferencedFormat] = None
    mechanism: Optional[MechanismEnum] = None
    conversation: Optional[ReferencedConversation] = None
    __properties: ClassVar[List[str]] = ["event", "application", "asset", "user", "format", "mechanism", "conversation"]

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
        """Create an instance of SeededActivity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of event
        if self.event:
            _dict['event'] = self.event.to_dict()
        # override the default output from pydantic by calling `to_dict()` of application
        if self.application:
            _dict['application'] = self.application.to_dict()
        # override the default output from pydantic by calling `to_dict()` of asset
        if self.asset:
            _dict['asset'] = self.asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of format
        if self.format:
            _dict['format'] = self.format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conversation
        if self.conversation:
            _dict['conversation'] = self.conversation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SeededActivity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event": SeededConnectorTracking.from_dict(obj["event"]) if obj.get("event") is not None else None,
            "application": Application.from_dict(obj["application"]) if obj.get("application") is not None else None,
            "asset": ReferencedAsset.from_dict(obj["asset"]) if obj.get("asset") is not None else None,
            "user": ReferencedUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "format": ReferencedFormat.from_dict(obj["format"]) if obj.get("format") is not None else None,
            "mechanism": obj.get("mechanism"),
            "conversation": ReferencedConversation.from_dict(obj["conversation"]) if obj.get("conversation") is not None else None
        })
        return _obj


