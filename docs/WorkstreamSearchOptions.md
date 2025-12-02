# WorkstreamSearchOptions

This is a search realted to the workstream pattern engine data, for instance in a WPE/vision/search we will want to be able to search via a WorkstreamPatternEngineSource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**sources** | [**WorkstreamPatternEngineSources**](WorkstreamPatternEngineSources.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_search_options import WorkstreamSearchOptions

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSearchOptions from a JSON string
workstream_search_options_instance = WorkstreamSearchOptions.from_json(json)
# print the JSON string representation of the object
print(WorkstreamSearchOptions.to_json())

# convert the object into a dict
workstream_search_options_dict = workstream_search_options_instance.to_dict()
# create an instance of WorkstreamSearchOptions from a dict
workstream_search_options_from_dict = WorkstreamSearchOptions.from_dict(workstream_search_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


