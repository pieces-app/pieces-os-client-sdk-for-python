# ReferencedWorkstreamPatternEngineSourceWindow

This is the referenced source window for the workstream pattern engine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** | The id of the referenced source window | 
**reference** | [**FlattenedWorkstreamPatternEngineSourceWindow**](FlattenedWorkstreamPatternEngineSourceWindow.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.referenced_workstream_pattern_engine_source_window import ReferencedWorkstreamPatternEngineSourceWindow

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedWorkstreamPatternEngineSourceWindow from a JSON string
referenced_workstream_pattern_engine_source_window_instance = ReferencedWorkstreamPatternEngineSourceWindow.from_json(json)
# print the JSON string representation of the object
print ReferencedWorkstreamPatternEngineSourceWindow.to_json()

# convert the object into a dict
referenced_workstream_pattern_engine_source_window_dict = referenced_workstream_pattern_engine_source_window_instance.to_dict()
# create an instance of ReferencedWorkstreamPatternEngineSourceWindow from a dict
referenced_workstream_pattern_engine_source_window_from_dict = ReferencedWorkstreamPatternEngineSourceWindow.from_dict(referenced_workstream_pattern_engine_source_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


