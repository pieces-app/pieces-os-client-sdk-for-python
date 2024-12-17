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
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.qgpt_task_pipeline_for_code_commentation import QGPTTaskPipelineForCodeCommentation
from pieces_os_client.models.qgpt_task_pipeline_for_code_completion import QGPTTaskPipelineForCodeCompletion
from pieces_os_client.models.qgpt_task_pipeline_for_code_explanation import QGPTTaskPipelineForCodeExplanation
from pieces_os_client.models.qgpt_task_pipeline_for_code_fix import QGPTTaskPipelineForCodeFix
from pieces_os_client.models.qgpt_task_pipeline_for_code_modification import QGPTTaskPipelineForCodeModification

class QGPTTaskPipeline(BaseModel):
    """
    This model is specifically for QGPT Task pipelines, the model is used to group one off tasks for instance fix/explaining/commenting that dont necessarily require a conversation form factor.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    code_explanation: Optional[QGPTTaskPipelineForCodeExplanation] = None
    code_commentation: Optional[QGPTTaskPipelineForCodeCommentation] = None
    code_fix: Optional[QGPTTaskPipelineForCodeFix] = None
    code_modification: Optional[QGPTTaskPipelineForCodeModification] = None
    code_completion: Optional[QGPTTaskPipelineForCodeCompletion] = None
    __properties = ["schema", "code_explanation", "code_commentation", "code_fix", "code_modification", "code_completion"]

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
    def from_json(cls, json_str: str) -> QGPTTaskPipeline:
        """Create an instance of QGPTTaskPipeline from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of code_explanation
        if self.code_explanation:
            _dict['code_explanation'] = self.code_explanation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of code_commentation
        if self.code_commentation:
            _dict['code_commentation'] = self.code_commentation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of code_fix
        if self.code_fix:
            _dict['code_fix'] = self.code_fix.to_dict()
        # override the default output from pydantic by calling `to_dict()` of code_modification
        if self.code_modification:
            _dict['code_modification'] = self.code_modification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of code_completion
        if self.code_completion:
            _dict['code_completion'] = self.code_completion.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QGPTTaskPipeline:
        """Create an instance of QGPTTaskPipeline from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QGPTTaskPipeline.parse_obj(obj)

        _obj = QGPTTaskPipeline.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "code_explanation": QGPTTaskPipelineForCodeExplanation.from_dict(obj.get("code_explanation")) if obj.get("code_explanation") is not None else None,
            "code_commentation": QGPTTaskPipelineForCodeCommentation.from_dict(obj.get("code_commentation")) if obj.get("code_commentation") is not None else None,
            "code_fix": QGPTTaskPipelineForCodeFix.from_dict(obj.get("code_fix")) if obj.get("code_fix") is not None else None,
            "code_modification": QGPTTaskPipelineForCodeModification.from_dict(obj.get("code_modification")) if obj.get("code_modification") is not None else None,
            "code_completion": QGPTTaskPipelineForCodeCompletion.from_dict(obj.get("code_completion")) if obj.get("code_completion") is not None else None
        })
        return _obj


