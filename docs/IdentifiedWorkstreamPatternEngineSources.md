# IdentifiedWorkstreamPatternEngineSources



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[IdentifiedWorkstreamPatternEngineSource]**](IdentifiedWorkstreamPatternEngineSource.md) |  | 
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an source id. | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.identified_workstream_pattern_engine_sources import IdentifiedWorkstreamPatternEngineSources

# TODO update the JSON string below
json = "{}"
# create an instance of IdentifiedWorkstreamPatternEngineSources from a JSON string
identified_workstream_pattern_engine_sources_instance = IdentifiedWorkstreamPatternEngineSources.from_json(json)
# print the JSON string representation of the object
print IdentifiedWorkstreamPatternEngineSources.to_json()

# convert the object into a dict
identified_workstream_pattern_engine_sources_dict = identified_workstream_pattern_engine_sources_instance.to_dict()
# create an instance of IdentifiedWorkstreamPatternEngineSources from a dict
identified_workstream_pattern_engine_sources_from_dict = IdentifiedWorkstreamPatternEngineSources.from_dict(identified_workstream_pattern_engine_sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


