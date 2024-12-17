# SearchedIdentifiedWorkstreamPatternEngineSource

TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**workstream_pattern_engine_source** | [**IdentifiedWorkstreamPatternEngineSource**](IdentifiedWorkstreamPatternEngineSource.md) |  | [optional] 
**exact** | **bool** |  | 
**similarity** | **float** |  | 
**temporal** | **bool** |  | [optional] 
**identifier** | **str** | This is the uuid of the source. | 

## Example

```python
from pieces_os_client.models.searched_identified_workstream_pattern_engine_source import SearchedIdentifiedWorkstreamPatternEngineSource

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedIdentifiedWorkstreamPatternEngineSource from a JSON string
searched_identified_workstream_pattern_engine_source_instance = SearchedIdentifiedWorkstreamPatternEngineSource.from_json(json)
# print the JSON string representation of the object
print SearchedIdentifiedWorkstreamPatternEngineSource.to_json()

# convert the object into a dict
searched_identified_workstream_pattern_engine_source_dict = searched_identified_workstream_pattern_engine_source_instance.to_dict()
# create an instance of SearchedIdentifiedWorkstreamPatternEngineSource from a dict
searched_identified_workstream_pattern_engine_source_from_dict = SearchedIdentifiedWorkstreamPatternEngineSource.from_dict(searched_identified_workstream_pattern_engine_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


