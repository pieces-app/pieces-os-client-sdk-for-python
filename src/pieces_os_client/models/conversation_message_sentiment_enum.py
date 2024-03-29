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


class ConversationMessageSentimentEnum(str, Enum):
    """
    This will describe the sentiment of a specific message ie if the message was liked/disliked/reported
    """

    """
    allowed enum values
    """
    LIKE = 'LIKE'
    DISLIKE = 'DISLIKE'
    REPORT = 'REPORT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConversationMessageSentimentEnum from a JSON string"""
        return cls(json.loads(json_str))


