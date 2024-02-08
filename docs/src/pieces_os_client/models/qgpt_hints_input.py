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
from pieces_os_client.models.qgpt_question_answer import QGPTQuestionAnswer
from pieces_os_client.models.relevant_qgpt_seeds import RelevantQGPTSeeds

class QGPTHintsInput(BaseModel):
    """
    Query is your hints question. Relevant is the relevant snippets. Answer is the previous answer.(that we are asking a hint up for.)  Query and Answer are both optional here because, you may pass over relevant snippets over ahead of hand if you already have them to answer your questions.  # noqa: E501
    """
    query: Optional[StrictStr] = None
    answer: Optional[QGPTQuestionAnswer] = None
    relevant: RelevantQGPTSeeds = Field(...)
    application: Optional[StrictStr] = Field(None, description="optional application id")
    model: Optional[StrictStr] = Field(None, description="optional model id")
    __properties = ["query", "answer", "relevant", "application", "model"]

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
    def from_json(cls, json_str: str) -> QGPTHintsInput:
        """Create an instance of QGPTHintsInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of answer
        if self.answer:
            _dict['answer'] = self.answer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relevant
        if self.relevant:
            _dict['relevant'] = self.relevant.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QGPTHintsInput:
        """Create an instance of QGPTHintsInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QGPTHintsInput.parse_obj(obj)

        _obj = QGPTHintsInput.parse_obj({
            "query": obj.get("query"),
            "answer": QGPTQuestionAnswer.from_dict(obj.get("answer")) if obj.get("answer") is not None else None,
            "relevant": RelevantQGPTSeeds.from_dict(obj.get("relevant")) if obj.get("relevant") is not None else None,
            "application": obj.get("application"),
            "model": obj.get("model")
        })
        return _obj


