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

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.qgpt_conversation_pipeline_for_contextualized_code_dialog import QGPTConversationPipelineForContextualizedCodeDialog
from pieces_os_client.models.qgpt_conversation_pipeline_for_contextualized_code_generation import QGPTConversationPipelineForContextualizedCodeGeneration
from pieces_os_client.models.qgpt_conversation_pipeline_for_generalized_code_dialog import QGPTConversationPipelineForGeneralizedCodeDialog
from typing import Optional, Set
from typing_extensions import Self

class QGPTConversationPipeline(BaseModel):
    """
    This model is specifically for QGPT Conversation pipelines, the model is used to group conversational prompts for instance a conversation around generating code.  here are some use cases- 1. contextualized_code_generation- This is for users that want to have conversations around generating code, when there is provided context. 2. generalized_code- This is for users that want to have conversations without context around code. 3. contextualized_code- This is for users that want to have conversation around code with Context.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    contextualized_code_generation: Optional[QGPTConversationPipelineForContextualizedCodeGeneration] = None
    generalized_code_dialog: Optional[QGPTConversationPipelineForGeneralizedCodeDialog] = None
    contextualized_code_dialog: Optional[QGPTConversationPipelineForContextualizedCodeDialog] = None
    __properties: ClassVar[List[str]] = ["schema", "contextualized_code_generation", "generalized_code_dialog", "contextualized_code_dialog"]

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
        """Create an instance of QGPTConversationPipeline from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of contextualized_code_generation
        if self.contextualized_code_generation:
            _dict['contextualized_code_generation'] = self.contextualized_code_generation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generalized_code_dialog
        if self.generalized_code_dialog:
            _dict['generalized_code_dialog'] = self.generalized_code_dialog.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contextualized_code_dialog
        if self.contextualized_code_dialog:
            _dict['contextualized_code_dialog'] = self.contextualized_code_dialog.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QGPTConversationPipeline from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "contextualized_code_generation": QGPTConversationPipelineForContextualizedCodeGeneration.from_dict(obj["contextualized_code_generation"]) if obj.get("contextualized_code_generation") is not None else None,
            "generalized_code_dialog": QGPTConversationPipelineForGeneralizedCodeDialog.from_dict(obj["generalized_code_dialog"]) if obj.get("generalized_code_dialog") is not None else None,
            "contextualized_code_dialog": QGPTConversationPipelineForContextualizedCodeDialog.from_dict(obj["contextualized_code_dialog"]) if obj.get("contextualized_code_dialog") is not None else None
        })
        return _obj


