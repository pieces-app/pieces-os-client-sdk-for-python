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





class LanguageServerProtocolSeverityEnum(str, Enum):
    """
    modeled of of https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#diagnosticSeverity
    """

    """
    allowed enum values
    """
    ERROR = 'ERROR'
    WARNING = 'WARNING'
    INFORMATION = 'INFORMATION'
    HINT = 'HINT'

    @classmethod
    def from_json(cls, json_str: str) -> LanguageServerProtocolSeverityEnum:
        """Create an instance of LanguageServerProtocolSeverityEnum from a JSON string"""
        return LanguageServerProtocolSeverityEnum(json.loads(json_str))


