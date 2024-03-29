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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pieces_os_client.models.edges import Edges
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.embeddings import Embeddings
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from typing import Optional, Set
from typing_extensions import Self

class Relationship(BaseModel):
    """
    A relationship expresses a graph of like types, to build a relationship graph.   To get the type of relationship, this is for ie Asset, tag, website, format ...etc, you will need to iterate through the edges and get the root or you can just get the first edge's type as a relationship can only be expressed through same type
    """ # noqa: E501
    id: StrictStr
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    embeddings: Embeddings
    edges: Edges
    created: GroupedTimestamp
    updated: GroupedTimestamp
    deleted: Optional[GroupedTimestamp] = None
    __properties: ClassVar[List[str]] = ["id", "schema", "embeddings", "edges", "created", "updated", "deleted"]

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
        """Create an instance of Relationship from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of embeddings
        if self.embeddings:
            _dict['embeddings'] = self.embeddings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of edges
        if self.edges:
            _dict['edges'] = self.edges.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleted
        if self.deleted:
            _dict['deleted'] = self.deleted.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Relationship from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "embeddings": Embeddings.from_dict(obj["embeddings"]) if obj.get("embeddings") is not None else None,
            "edges": Edges.from_dict(obj["edges"]) if obj.get("edges") is not None else None,
            "created": GroupedTimestamp.from_dict(obj["created"]) if obj.get("created") is not None else None,
            "updated": GroupedTimestamp.from_dict(obj["updated"]) if obj.get("updated") is not None else None,
            "deleted": GroupedTimestamp.from_dict(obj["deleted"]) if obj.get("deleted") is not None else None
        })
        return _obj


