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
from pydantic import BaseModel, Field, StrictStr, conlist
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.flattened_anchors import FlattenedAnchors
from pieces_os_client.models.flattened_assets import FlattenedAssets
from pieces_os_client.models.flattened_conversation_messages import FlattenedConversationMessages
from pieces_os_client.models.qgpt_relevance_input_options import QGPTRelevanceInputOptions
from pieces_os_client.models.seeds import Seeds
from pieces_os_client.models.temporal_range_grounding import TemporalRangeGrounding

class QGPTRelevanceInput(BaseModel):
    """
    This is the input body for the /code_gpt/relevance endpoint.  There are a couple different options that you may take with this Model.  First we will talk about the space in which you will compare your query too. These are the following cases for the space. 1. provide an absolute path on the users machine that we can use locally. 2. provide Seeds that you want to compare to, which will be ONLY fragment/string values(all other values will be ignored) 3. provide assets, here you can provide an iterable of the asset id, and we will do the rest 4. you can set your database boolean to true which will tell us to use your entire DB as the query space.  Note: - for ease of use, we have an additional boolean called 'question', which will also ask your question to gpt3.5, and compare to the relevant snippets that we found. That way you dont need to call /code_gpt/question. Otherwise the next step would be is to take the results and feed them into /code_gpt/question. to get your question answered.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    query: StrictStr = Field(default=..., description="This is the question that the user is asking.")
    paths: Optional[conlist(StrictStr)] = Field(default=None, description="This is an optional list of file || folder paths.")
    seeds: Optional[Seeds] = None
    assets: Optional[FlattenedAssets] = None
    messages: Optional[FlattenedConversationMessages] = None
    options: Optional[QGPTRelevanceInputOptions] = None
    application: Optional[StrictStr] = Field(default=None, description="optional application id")
    model: Optional[StrictStr] = Field(default=None, description="optional model id")
    temporal: Optional[TemporalRangeGrounding] = None
    anchors: Optional[FlattenedAnchors] = None
    __properties = ["schema", "query", "paths", "seeds", "assets", "messages", "options", "application", "model", "temporal", "anchors"]

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
    def from_json(cls, json_str: str) -> QGPTRelevanceInput:
        """Create an instance of QGPTRelevanceInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of seeds
        if self.seeds:
            _dict['seeds'] = self.seeds.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of messages
        if self.messages:
            _dict['messages'] = self.messages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of temporal
        if self.temporal:
            _dict['temporal'] = self.temporal.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anchors
        if self.anchors:
            _dict['anchors'] = self.anchors.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QGPTRelevanceInput:
        """Create an instance of QGPTRelevanceInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QGPTRelevanceInput.parse_obj(obj)

        _obj = QGPTRelevanceInput.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "query": obj.get("query"),
            "paths": obj.get("paths"),
            "seeds": Seeds.from_dict(obj.get("seeds")) if obj.get("seeds") is not None else None,
            "assets": FlattenedAssets.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "messages": FlattenedConversationMessages.from_dict(obj.get("messages")) if obj.get("messages") is not None else None,
            "options": QGPTRelevanceInputOptions.from_dict(obj.get("options")) if obj.get("options") is not None else None,
            "application": obj.get("application"),
            "model": obj.get("model"),
            "temporal": TemporalRangeGrounding.from_dict(obj.get("temporal")) if obj.get("temporal") is not None else None,
            "anchors": FlattenedAnchors.from_dict(obj.get("anchors")) if obj.get("anchors") is not None else None
        })
        return _obj


