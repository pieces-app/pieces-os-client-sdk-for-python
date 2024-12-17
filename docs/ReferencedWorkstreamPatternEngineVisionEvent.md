# ReferencedWorkstreamPatternEngineVisionEvent

This will return a specific event for the WPE.  note: value is nullable here because we may want to pass in transferables:true/false

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**reference** | [**FlattenedWorkstreamPatternEngineVisionEvent**](FlattenedWorkstreamPatternEngineVisionEvent.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.referenced_workstream_pattern_engine_vision_event import ReferencedWorkstreamPatternEngineVisionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedWorkstreamPatternEngineVisionEvent from a JSON string
referenced_workstream_pattern_engine_vision_event_instance = ReferencedWorkstreamPatternEngineVisionEvent.from_json(json)
# print the JSON string representation of the object
print ReferencedWorkstreamPatternEngineVisionEvent.to_json()

# convert the object into a dict
referenced_workstream_pattern_engine_vision_event_dict = referenced_workstream_pattern_engine_vision_event_instance.to_dict()
# create an instance of ReferencedWorkstreamPatternEngineVisionEvent from a dict
referenced_workstream_pattern_engine_vision_event_from_dict = ReferencedWorkstreamPatternEngineVisionEvent.from_dict(referenced_workstream_pattern_engine_vision_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


