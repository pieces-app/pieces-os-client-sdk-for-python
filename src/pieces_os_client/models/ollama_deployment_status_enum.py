# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class OllamaDeploymentStatusEnum(str, Enum):
    """
    Enum used for the status of Ollama
    """

    """
    allowed enum values
    """
    UNKNOWN = 'UNKNOWN'
    INITIALIZED = 'INITIALIZED'
    IN_MINUS_PROGRESS = 'IN-PROGRESS'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    CANCELED = 'CANCELED'
    RESET = 'RESET'

    @classmethod
    def from_json(cls, json_str: str) -> OllamaDeploymentStatusEnum:
        """Create an instance of OllamaDeploymentStatusEnum from a JSON string"""
        return OllamaDeploymentStatusEnum(json.loads(json_str))


