# FlattenedWorkstreamEvent

This is a singular (DAG Safe) version of a WorkstreamEvent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**Application**](Application.md) |  | 
**context** | [**WorkstreamEventContext**](WorkstreamEventContext.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**id** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**trigger** | [**WorkstreamEventTrigger**](WorkstreamEventTrigger.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 

## Example

```python
from pieces_os_client.models.flattened_workstream_event import FlattenedWorkstreamEvent

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedWorkstreamEvent from a JSON string
flattened_workstream_event_instance = FlattenedWorkstreamEvent.from_json(json)
# print the JSON string representation of the object
print FlattenedWorkstreamEvent.to_json()

# convert the object into a dict
flattened_workstream_event_dict = flattened_workstream_event_instance.to_dict()
# create an instance of FlattenedWorkstreamEvent from a dict
flattened_workstream_event_from_dict = FlattenedWorkstreamEvent.from_dict(flattened_workstream_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


