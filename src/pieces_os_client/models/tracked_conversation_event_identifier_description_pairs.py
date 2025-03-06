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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from typing import Optional, Set
from typing_extensions import Self

class TrackedConversationEventIdentifierDescriptionPairs(BaseModel):
    """
    These are all of the available event types that are permitted in an object pair notation.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    conversation_created: Optional[StrictStr] = Field(default=None, description="The key value pair for an conversation being created.")
    conversation_referenced: Optional[StrictStr] = Field(default=None, description="This means that an conversation was view/used while the user was looking at the default view.")
    conversation_deleted: Optional[StrictStr] = Field(default=None, description="A conversation was deleted")
    conversation_summary_annotation_generated_by_the_user: Optional[StrictStr] = Field(default=None, description="A conversation summary was generated by the user")
    conversation_name_updated_by_the_system: Optional[StrictStr] = Field(default=None, description="A conversation was renamed by the system")
    conversation_name_updated_by_the_user: Optional[StrictStr] = Field(default=None, description="A conversation was renamed by the user")
    conversation_summary_annotation_generated_by_the_system: Optional[StrictStr] = Field(default=None, description="A conversation summary was generated")
    __properties: ClassVar[List[str]] = ["schema", "conversation_created", "conversation_referenced", "conversation_deleted", "conversation_summary_annotation_generated_by_the_user", "conversation_name_updated_by_the_system", "conversation_name_updated_by_the_user", "conversation_summary_annotation_generated_by_the_system"]

    @field_validator('conversation_created')
    def conversation_created_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['a_conversation_was_created']):
            raise ValueError("must be one of enum values ('a_conversation_was_created')")
        return value

    @field_validator('conversation_referenced')
    def conversation_referenced_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['a_conversation_was_referenced_by_the_user']):
            raise ValueError("must be one of enum values ('a_conversation_was_referenced_by_the_user')")
        return value

    @field_validator('conversation_deleted')
    def conversation_deleted_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['a_conversation_was_deleted']):
            raise ValueError("must be one of enum values ('a_conversation_was_deleted')")
        return value

    @field_validator('conversation_summary_annotation_generated_by_the_user')
    def conversation_summary_annotation_generated_by_the_user_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['a_conversation_summary_annotation_was_generated_by_the_user']):
            raise ValueError("must be one of enum values ('a_conversation_summary_annotation_was_generated_by_the_user')")
        return value

    @field_validator('conversation_name_updated_by_the_system')
    def conversation_name_updated_by_the_system_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['a_conversation_was_renamed_by_the_system']):
            raise ValueError("must be one of enum values ('a_conversation_was_renamed_by_the_system')")
        return value

    @field_validator('conversation_name_updated_by_the_user')
    def conversation_name_updated_by_the_user_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['a_conversation_was_renamed_by_the_user']):
            raise ValueError("must be one of enum values ('a_conversation_was_renamed_by_the_user')")
        return value

    @field_validator('conversation_summary_annotation_generated_by_the_system')
    def conversation_summary_annotation_generated_by_the_system_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['a_conversation_summary_annotation_was_generated_by_the_system']):
            raise ValueError("must be one of enum values ('a_conversation_summary_annotation_was_generated_by_the_system')")
        return value

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
        """Create an instance of TrackedConversationEventIdentifierDescriptionPairs from a JSON string"""
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
        """Create an instance of TrackedConversationEventIdentifierDescriptionPairs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "conversation_created": obj.get("conversation_created"),
            "conversation_referenced": obj.get("conversation_referenced"),
            "conversation_deleted": obj.get("conversation_deleted"),
            "conversation_summary_annotation_generated_by_the_user": obj.get("conversation_summary_annotation_generated_by_the_user"),
            "conversation_name_updated_by_the_system": obj.get("conversation_name_updated_by_the_system"),
            "conversation_name_updated_by_the_user": obj.get("conversation_name_updated_by_the_user"),
            "conversation_summary_annotation_generated_by_the_system": obj.get("conversation_summary_annotation_generated_by_the_system")
        })
        return _obj


