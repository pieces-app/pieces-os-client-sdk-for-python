# FlattenedWorkstreamPatternEngineSourceWindows

This is the flattened source windows for the workstream pattern engine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[ReferencedWorkstreamPatternEngineSourceWindow]**](ReferencedWorkstreamPatternEngineSourceWindow.md) | This is the iterable of the flattened source windows | 
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an source window id. | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_workstream_pattern_engine_source_windows import FlattenedWorkstreamPatternEngineSourceWindows

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedWorkstreamPatternEngineSourceWindows from a JSON string
flattened_workstream_pattern_engine_source_windows_instance = FlattenedWorkstreamPatternEngineSourceWindows.from_json(json)
# print the JSON string representation of the object
print FlattenedWorkstreamPatternEngineSourceWindows.to_json()

# convert the object into a dict
flattened_workstream_pattern_engine_source_windows_dict = flattened_workstream_pattern_engine_source_windows_instance.to_dict()
# create an instance of FlattenedWorkstreamPatternEngineSourceWindows from a dict
flattened_workstream_pattern_engine_source_windows_from_dict = FlattenedWorkstreamPatternEngineSourceWindows.from_dict(flattened_workstream_pattern_engine_source_windows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


