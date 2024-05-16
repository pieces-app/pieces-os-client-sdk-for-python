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





class AnchorTypeEnum(str, Enum):
    """
    This is an enum used to differentiate the different between different anchors. Used in the Anchor data model.
    """

    """
    allowed enum values
    """
    FILE = 'FILE'
    DIRECTORY = 'DIRECTORY'

    @classmethod
    def from_json(cls, json_str: str) -> AnchorTypeEnum:
        """Create an instance of AnchorTypeEnum from a JSON string"""
        return AnchorTypeEnum(json.loads(json_str))


