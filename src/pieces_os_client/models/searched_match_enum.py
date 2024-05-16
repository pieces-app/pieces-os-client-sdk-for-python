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





class SearchedMatchEnum(str, Enum):
    """
    SearchedMatchEnum
    """

    """
    allowed enum values
    """
    TITLE = 'TITLE'
    ANNOTATION = 'ANNOTATION'
    HINT = 'HINT'
    CONTENT = 'CONTENT'
    FUZZY = 'FUZZY'
    MULTIPLE = 'MULTIPLE'
    TAGS = 'TAGS'
    WEBSITES = 'WEBSITES'
    PERSONS = 'PERSONS'

    @classmethod
    def from_json(cls, json_str: str) -> SearchedMatchEnum:
        """Create an instance of SearchedMatchEnum from a JSON string"""
        return SearchedMatchEnum(json.loads(json_str))


