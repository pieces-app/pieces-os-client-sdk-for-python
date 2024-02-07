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
from pieces_os_client.models.allocation_cloud_status import AllocationCloudStatus
from pieces_os_client.models.allocation_cloud_urls import AllocationCloudUrls
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp

class AllocationCloud(BaseModel):
    """
    update && version: will be present only if your cloud was successfully spun up && running.  updated: is the last time this was updated.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    id: StrictStr = Field(..., description="This is a uuid that represents this cloud.(this is the same as the userid)")
    user: StrictStr = Field(..., description="this is your useruuid.")
    urls: AllocationCloudUrls = Field(...)
    status: AllocationCloudStatus = Field(...)
    project: StrictStr = Field(..., description="This is the project that this is attached to.")
    updated: Optional[GroupedTimestamp] = None
    version: Optional[StrictStr] = Field(None, description="this is the current version of the server.")
    region: Optional[StrictStr] = Field(None, description="this is the region where the project is defined.")
    __properties = ["schema", "id", "user", "urls", "status", "project", "updated", "version", "region"]

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
    def from_json(cls, json_str: str) -> AllocationCloud:
        """Create an instance of AllocationCloud from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of urls
        if self.urls:
            _dict['urls'] = self.urls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AllocationCloud:
        """Create an instance of AllocationCloud from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AllocationCloud.parse_obj(obj)

        _obj = AllocationCloud.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "user": obj.get("user"),
            "urls": AllocationCloudUrls.from_dict(obj.get("urls")) if obj.get("urls") is not None else None,
            "status": AllocationCloudStatus.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "project": obj.get("project"),
            "updated": GroupedTimestamp.from_dict(obj.get("updated")) if obj.get("updated") is not None else None,
            "version": obj.get("version"),
            "region": obj.get("region")
        })
        return _obj


