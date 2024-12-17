# FlattenedWorkstreamEvents

This is a plural (DAG Safe) version of a WorkstreamEvents.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an activity id. | [optional] 
**iterable** | [**List[ReferencedWorkstreamEvent]**](ReferencedWorkstreamEvent.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_workstream_events import FlattenedWorkstreamEvents

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedWorkstreamEvents from a JSON string
flattened_workstream_events_instance = FlattenedWorkstreamEvents.from_json(json)
# print the JSON string representation of the object
print FlattenedWorkstreamEvents.to_json()

# convert the object into a dict
flattened_workstream_events_dict = flattened_workstream_events_instance.to_dict()
# create an instance of FlattenedWorkstreamEvents from a dict
flattened_workstream_events_from_dict = FlattenedWorkstreamEvents.from_dict(flattened_workstream_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


