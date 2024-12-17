# WorkstreamPatternEngineSources

This is a plural version of the WPE qdrant applications

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[WorkstreamPatternEngineSource]**](WorkstreamPatternEngineSource.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_pattern_engine_sources import WorkstreamPatternEngineSources

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamPatternEngineSources from a JSON string
workstream_pattern_engine_sources_instance = WorkstreamPatternEngineSources.from_json(json)
# print the JSON string representation of the object
print WorkstreamPatternEngineSources.to_json()

# convert the object into a dict
workstream_pattern_engine_sources_dict = workstream_pattern_engine_sources_instance.to_dict()
# create an instance of WorkstreamPatternEngineSources from a dict
workstream_pattern_engine_sources_from_dict = WorkstreamPatternEngineSources.from_dict(workstream_pattern_engine_sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


