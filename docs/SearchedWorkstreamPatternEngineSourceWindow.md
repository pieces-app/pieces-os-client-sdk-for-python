# SearchedWorkstreamPatternEngineSourceWindow

TODO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exact** | **bool** |  | 
**identifier** | **str** | This is the uuid of the source. | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**similarity** | **float** |  | 
**temporal** | **bool** |  | [optional] 
**workstream_pattern_engine_source_window** | [**WorkstreamPatternEngineSourceWindow**](WorkstreamPatternEngineSourceWindow.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_workstream_pattern_engine_source_window import SearchedWorkstreamPatternEngineSourceWindow

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedWorkstreamPatternEngineSourceWindow from a JSON string
searched_workstream_pattern_engine_source_window_instance = SearchedWorkstreamPatternEngineSourceWindow.from_json(json)
# print the JSON string representation of the object
print(SearchedWorkstreamPatternEngineSourceWindow.to_json())

# convert the object into a dict
searched_workstream_pattern_engine_source_window_dict = searched_workstream_pattern_engine_source_window_instance.to_dict()
# create an instance of SearchedWorkstreamPatternEngineSourceWindow from a dict
searched_workstream_pattern_engine_source_window_from_dict = SearchedWorkstreamPatternEngineSourceWindow.from_dict(searched_workstream_pattern_engine_source_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


