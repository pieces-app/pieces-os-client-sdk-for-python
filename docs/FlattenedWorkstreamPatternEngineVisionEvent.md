# FlattenedWorkstreamPatternEngineVisionEvent

This is a flattened version of the WorkstreamPatternEngineVisionEvent, where the referenced to other materials are also flattened(DAG Safe)  Note: TODO later add textual and need to correspond w/ both transferables as well as the FlattenedMaterial

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**id** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_workstream_pattern_engine_vision_event import FlattenedWorkstreamPatternEngineVisionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedWorkstreamPatternEngineVisionEvent from a JSON string
flattened_workstream_pattern_engine_vision_event_instance = FlattenedWorkstreamPatternEngineVisionEvent.from_json(json)
# print the JSON string representation of the object
print FlattenedWorkstreamPatternEngineVisionEvent.to_json()

# convert the object into a dict
flattened_workstream_pattern_engine_vision_event_dict = flattened_workstream_pattern_engine_vision_event_instance.to_dict()
# create an instance of FlattenedWorkstreamPatternEngineVisionEvent from a dict
flattened_workstream_pattern_engine_vision_event_from_dict = FlattenedWorkstreamPatternEngineVisionEvent.from_dict(flattened_workstream_pattern_engine_vision_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


