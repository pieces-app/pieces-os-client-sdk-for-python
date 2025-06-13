# SeededWorkstreamPatternEngineSourceWindow

This is the seeded source window for the workstream pattern engine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**name** | **str** | The name of the seeded source window | 
**workstream_events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_workstream_pattern_engine_source_window import SeededWorkstreamPatternEngineSourceWindow

# TODO update the JSON string below
json = "{}"
# create an instance of SeededWorkstreamPatternEngineSourceWindow from a JSON string
seeded_workstream_pattern_engine_source_window_instance = SeededWorkstreamPatternEngineSourceWindow.from_json(json)
# print the JSON string representation of the object
print SeededWorkstreamPatternEngineSourceWindow.to_json()

# convert the object into a dict
seeded_workstream_pattern_engine_source_window_dict = seeded_workstream_pattern_engine_source_window_instance.to_dict()
# create an instance of SeededWorkstreamPatternEngineSourceWindow from a dict
seeded_workstream_pattern_engine_source_window_from_dict = SeededWorkstreamPatternEngineSourceWindow.from_dict(seeded_workstream_pattern_engine_source_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


