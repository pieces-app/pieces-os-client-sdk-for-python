# ReferencedIdentifiedWorkstreamPatternEngineSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**reference** | [**FlattenedIdentifiedWorkstreamPatternEngineSource**](FlattenedIdentifiedWorkstreamPatternEngineSource.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.referenced_identified_workstream_pattern_engine_source import ReferencedIdentifiedWorkstreamPatternEngineSource

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedIdentifiedWorkstreamPatternEngineSource from a JSON string
referenced_identified_workstream_pattern_engine_source_instance = ReferencedIdentifiedWorkstreamPatternEngineSource.from_json(json)
# print the JSON string representation of the object
print(ReferencedIdentifiedWorkstreamPatternEngineSource.to_json())

# convert the object into a dict
referenced_identified_workstream_pattern_engine_source_dict = referenced_identified_workstream_pattern_engine_source_instance.to_dict()
# create an instance of ReferencedIdentifiedWorkstreamPatternEngineSource from a dict
referenced_identified_workstream_pattern_engine_source_from_dict = ReferencedIdentifiedWorkstreamPatternEngineSource.from_dict(referenced_identified_workstream_pattern_engine_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


