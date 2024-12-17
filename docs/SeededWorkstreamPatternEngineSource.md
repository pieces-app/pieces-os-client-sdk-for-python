# SeededWorkstreamPatternEngineSource

TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**raw** | [**WorkstreamPatternEngineSource**](WorkstreamPatternEngineSource.md) |  | 
**filter** | **bool** | This will determine if we want to filter this specific source | [optional] 
**readable** | **str** | This is the name of the source(defualt original data) this is NOT used for matching just for readability | 

## Example

```python
from pieces_os_client.models.seeded_workstream_pattern_engine_source import SeededWorkstreamPatternEngineSource

# TODO update the JSON string below
json = "{}"
# create an instance of SeededWorkstreamPatternEngineSource from a JSON string
seeded_workstream_pattern_engine_source_instance = SeededWorkstreamPatternEngineSource.from_json(json)
# print the JSON string representation of the object
print SeededWorkstreamPatternEngineSource.to_json()

# convert the object into a dict
seeded_workstream_pattern_engine_source_dict = seeded_workstream_pattern_engine_source_instance.to_dict()
# create an instance of SeededWorkstreamPatternEngineSource from a dict
seeded_workstream_pattern_engine_source_from_dict = SeededWorkstreamPatternEngineSource.from_dict(seeded_workstream_pattern_engine_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


