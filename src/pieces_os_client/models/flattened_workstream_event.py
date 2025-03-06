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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from pieces_os_client.models.application import Application
from pieces_os_client.models.capabilities_enum import CapabilitiesEnum
from pieces_os_client.models.embedded_model_schema import EmbeddedModelSchema
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp
from pieces_os_client.models.score import Score
from pieces_os_client.models.workstream_event_trigger import WorkstreamEventTrigger
from typing import Optional, Set
from typing_extensions import Self

class FlattenedWorkstreamEvent(BaseModel):
    """
    This is a singular (DAG Safe) version of a WorkstreamEvent.
    """ # noqa: E501
    var_schema: Optional[EmbeddedModelSchema] = Field(default=None, alias="schema")
    id: StrictStr
    score: Optional[Score] = None
    application: Application
    created: GroupedTimestamp
    updated: GroupedTimestamp
    trigger: WorkstreamEventTrigger
    context: Optional[WorkstreamEventContext] = None
    summaries: Optional[FlattenedWorkstreamSummaries] = None
    tags: Optional[FlattenedTags] = None
    workstream_events_vector: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="This is the embedding for the format.(NEEDs to connection.vector) and specific here because we can only index on a single name", alias="workstreamEventsVector")
    sources: Optional[FlattenedIdentifiedWorkstreamPatternEngineSources] = None
    window_title: Optional[StrictStr] = Field(default=None, description="This is the title of a tab, or a title of a file in the ide (this is a temporary property used for the WPE flow)", alias="windowTitle")
    browser_url: Optional[StrictStr] = Field(default=None, alias="browserUrl")
    processing: Optional[CapabilitiesEnum] = None
    __properties: ClassVar[List[str]] = ["schema", "id", "score", "application", "created", "updated", "trigger", "context", "summaries", "tags", "workstreamEventsVector", "sources", "windowTitle", "browserUrl", "processing"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FlattenedWorkstreamEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of score
        if self.score:
            _dict['score'] = self.score.to_dict()
        # override the default output from pydantic by calling `to_dict()` of application
        if self.application:
            _dict['application'] = self.application.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trigger
        if self.trigger:
            _dict['trigger'] = self.trigger.to_dict()
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['context'] = self.context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summaries
        if self.summaries:
            _dict['summaries'] = self.summaries.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sources
        if self.sources:
            _dict['sources'] = self.sources.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FlattenedWorkstreamEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": EmbeddedModelSchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "id": obj.get("id"),
            "score": Score.from_dict(obj["score"]) if obj.get("score") is not None else None,
            "application": Application.from_dict(obj["application"]) if obj.get("application") is not None else None,
            "created": GroupedTimestamp.from_dict(obj["created"]) if obj.get("created") is not None else None,
            "updated": GroupedTimestamp.from_dict(obj["updated"]) if obj.get("updated") is not None else None,
            "trigger": WorkstreamEventTrigger.from_dict(obj["trigger"]) if obj.get("trigger") is not None else None,
            "context": WorkstreamEventContext.from_dict(obj["context"]) if obj.get("context") is not None else None,
            "summaries": FlattenedWorkstreamSummaries.from_dict(obj["summaries"]) if obj.get("summaries") is not None else None,
            "tags": FlattenedTags.from_dict(obj["tags"]) if obj.get("tags") is not None else None,
            "workstreamEventsVector": obj.get("workstreamEventsVector"),
            "sources": FlattenedIdentifiedWorkstreamPatternEngineSources.from_dict(obj["sources"]) if obj.get("sources") is not None else None,
            "windowTitle": obj.get("windowTitle"),
            "browserUrl": obj.get("browserUrl"),
            "processing": obj.get("processing")
        })
        return _obj

from pieces_os_client.models.flattened_identified_workstream_pattern_engine_sources import FlattenedIdentifiedWorkstreamPatternEngineSources
from pieces_os_client.models.flattened_tags import FlattenedTags
from pieces_os_client.models.flattened_workstream_summaries import FlattenedWorkstreamSummaries
from pieces_os_client.models.workstream_event_context import WorkstreamEventContext
# TODO: Rewrite to not use raise_errors
FlattenedWorkstreamEvent.model_rebuild(raise_errors=False)

