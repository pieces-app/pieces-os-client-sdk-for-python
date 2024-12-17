# WorkstreamPatternEngineVisionEvent

This will return a specific event for the WPE.  note: value is nullable here because we may want to pass in transferables:true/false

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**id** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**source** | [**WorkstreamPatternEngineSource**](WorkstreamPatternEngineSource.md) |  | [optional] 
**textual** | [**WorkstreamPatternEngineVisionEventTextualValue**](WorkstreamPatternEngineVisionEventTextualValue.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_pattern_engine_vision_event import WorkstreamPatternEngineVisionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamPatternEngineVisionEvent from a JSON string
workstream_pattern_engine_vision_event_instance = WorkstreamPatternEngineVisionEvent.from_json(json)
# print the JSON string representation of the object
print WorkstreamPatternEngineVisionEvent.to_json()

# convert the object into a dict
workstream_pattern_engine_vision_event_dict = workstream_pattern_engine_vision_event_instance.to_dict()
# create an instance of WorkstreamPatternEngineVisionEvent from a dict
workstream_pattern_engine_vision_event_from_dict = WorkstreamPatternEngineVisionEvent.from_dict(workstream_pattern_engine_vision_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


