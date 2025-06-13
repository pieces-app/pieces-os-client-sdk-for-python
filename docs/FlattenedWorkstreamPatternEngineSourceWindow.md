# FlattenedWorkstreamPatternEngineSourceWindow

This is the flattened source window for the workstream pattern engine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** | The id of the flattened source window | 
**name** | **str** | The name of the flattened source window | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**score** | [**Score**](Score.md) |  | [optional] 
**workstream_events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 
**tags** | [**FlattenedTags**](FlattenedTags.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_workstream_pattern_engine_source_window import FlattenedWorkstreamPatternEngineSourceWindow

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedWorkstreamPatternEngineSourceWindow from a JSON string
flattened_workstream_pattern_engine_source_window_instance = FlattenedWorkstreamPatternEngineSourceWindow.from_json(json)
# print the JSON string representation of the object
print FlattenedWorkstreamPatternEngineSourceWindow.to_json()

# convert the object into a dict
flattened_workstream_pattern_engine_source_window_dict = flattened_workstream_pattern_engine_source_window_instance.to_dict()
# create an instance of FlattenedWorkstreamPatternEngineSourceWindow from a dict
flattened_workstream_pattern_engine_source_window_from_dict = FlattenedWorkstreamPatternEngineSourceWindow.from_dict(flattened_workstream_pattern_engine_source_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


