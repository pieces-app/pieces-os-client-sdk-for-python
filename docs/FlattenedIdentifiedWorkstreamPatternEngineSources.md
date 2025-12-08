# FlattenedIdentifiedWorkstreamPatternEngineSources

TODO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an source id. | [optional] 
**iterable** | [**List[ReferencedIdentifiedWorkstreamPatternEngineSource]**](ReferencedIdentifiedWorkstreamPatternEngineSource.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_identified_workstream_pattern_engine_sources import FlattenedIdentifiedWorkstreamPatternEngineSources

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedIdentifiedWorkstreamPatternEngineSources from a JSON string
flattened_identified_workstream_pattern_engine_sources_instance = FlattenedIdentifiedWorkstreamPatternEngineSources.from_json(json)
# print the JSON string representation of the object
print(FlattenedIdentifiedWorkstreamPatternEngineSources.to_json())

# convert the object into a dict
flattened_identified_workstream_pattern_engine_sources_dict = flattened_identified_workstream_pattern_engine_sources_instance.to_dict()
# create an instance of FlattenedIdentifiedWorkstreamPatternEngineSources from a dict
flattened_identified_workstream_pattern_engine_sources_from_dict = FlattenedIdentifiedWorkstreamPatternEngineSources.from_dict(flattened_identified_workstream_pattern_engine_sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


