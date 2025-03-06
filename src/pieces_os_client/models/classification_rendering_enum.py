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
import json
from enum import Enum
from typing_extensions import Self


class ClassificationRenderingEnum(str, Enum):
    """
    Specifically supported renderings...usually between generic types
    """

    """
    allowed enum values
    """
    HTML = 'HTML'
    TWENTY_FOUR_BIT_ANSI_ESCAPED_SEQUENCES = 'TWENTY_FOUR_BIT_ANSI_ESCAPED_SEQUENCES'
    HIGHLIGHT_JS_HTML = 'HIGHLIGHT_JS_HTML'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ClassificationRenderingEnum from a JSON string"""
        return cls(json.loads(json_str))


