# WorkstreamPatternEngineSourceWindows

This is the source windows for the workstream pattern engine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an source window id. | [optional] 
**iterable** | [**List[WorkstreamPatternEngineSourceWindow]**](WorkstreamPatternEngineSourceWindow.md) | This is the iterable of the source windows | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_pattern_engine_source_windows import WorkstreamPatternEngineSourceWindows

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamPatternEngineSourceWindows from a JSON string
workstream_pattern_engine_source_windows_instance = WorkstreamPatternEngineSourceWindows.from_json(json)
# print the JSON string representation of the object
print(WorkstreamPatternEngineSourceWindows.to_json())

# convert the object into a dict
workstream_pattern_engine_source_windows_dict = workstream_pattern_engine_source_windows_instance.to_dict()
# create an instance of WorkstreamPatternEngineSourceWindows from a dict
workstream_pattern_engine_source_windows_from_dict = WorkstreamPatternEngineSourceWindows.from_dict(workstream_pattern_engine_source_windows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


