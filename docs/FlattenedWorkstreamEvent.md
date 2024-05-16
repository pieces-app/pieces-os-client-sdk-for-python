# FlattenedWorkstreamEvent

This is a singular (DAG Safe) version of a WorkstreamEvent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | 
**score** | [**Score**](Score.md) |  | [optional] 
**application** | [**Application**](Application.md) |  | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**trigger** | [**WorkstreamEventTrigger**](WorkstreamEventTrigger.md) |  | 
**context** | [**WorkstreamEventContext**](WorkstreamEventContext.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 

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
flattened_workstream_event_form_dict = flattened_workstream_event.from_dict(flattened_workstream_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


