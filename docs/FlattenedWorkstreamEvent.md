# FlattenedWorkstreamEvent

This is a singular (DAG Safe) version of a WorkstreamEvent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchors** | [**FlattenedAnchors**](FlattenedAnchors.md) |  | [optional] 
**annotations** | [**FlattenedAnnotations**](FlattenedAnnotations.md) |  | [optional] 
**application** | [**Application**](Application.md) |  | 
**browser_url** | **str** |  | [optional] 
**context** | [**WorkstreamEventContext**](WorkstreamEventContext.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**id** | **str** |  | 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**processing** | [**CapabilitiesEnum**](CapabilitiesEnum.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**source_windows** | [**FlattenedWorkstreamPatternEngineSourceWindows**](FlattenedWorkstreamPatternEngineSourceWindows.md) |  | [optional] 
**sources** | [**FlattenedIdentifiedWorkstreamPatternEngineSources**](FlattenedIdentifiedWorkstreamPatternEngineSources.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**tags** | [**FlattenedTags**](FlattenedTags.md) |  | [optional] 
**trigger** | [**WorkstreamEventTrigger**](WorkstreamEventTrigger.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 
**window_title** | **str** | This is the title of a tab, or a title of a file in the ide (this is a temporary property used for the WPE flow) | [optional] 
**workstream_events_vector** | **List[float]** | This is the embedding for the format.(NEEDs to connection.vector) and specific here because we can only index on a single name NOTE: this is the vector index that corresponds to the couchbase lite index. | [optional] 

## Example

```python
from pieces_os_client.models.flattened_workstream_event import FlattenedWorkstreamEvent

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedWorkstreamEvent from a JSON string
flattened_workstream_event_instance = FlattenedWorkstreamEvent.from_json(json)
# print the JSON string representation of the object
print(FlattenedWorkstreamEvent.to_json())

# convert the object into a dict
flattened_workstream_event_dict = flattened_workstream_event_instance.to_dict()
# create an instance of FlattenedWorkstreamEvent from a dict
flattened_workstream_event_from_dict = FlattenedWorkstreamEvent.from_dict(flattened_workstream_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


