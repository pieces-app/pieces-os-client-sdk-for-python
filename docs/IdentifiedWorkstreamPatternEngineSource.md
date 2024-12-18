# IdentifiedWorkstreamPatternEngineSource

This is a specific persisted model for WorkstreamPatternEngineSources that are persisted in the database(not just on the WPE event)  note: there is a \"WorkstreamPatternEngineSource\" model however we will NOT be modify this because it is linked to a different model that would require additional code to properly associate/disassociate.  note: we get 3 raw events from the WPE data so far:(encapsulated in the \"WorkstreamPatternEngineSource\") event 1. browserUrl - defaults to null 2. appTitle - ** not sure on default here ** (this is because this is always present on all WPE events.) 3. windowTitle - defaults to \"Window Title Not Found\"  note: raw is the raw value from the WPE(expect I will replace the defaults w/ nullish values)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | 
**raw** | [**WorkstreamPatternEngineSource**](WorkstreamPatternEngineSource.md) |  | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**filter** | **bool** | This will determine if we want to filter this specific source | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**readable** | **str** | This is the name of the source(defualt original data) this is NOT used for matching just for readability | 

## Example

```python
from pieces_os_client.models.identified_workstream_pattern_engine_source import IdentifiedWorkstreamPatternEngineSource

# TODO update the JSON string below
json = "{}"
# create an instance of IdentifiedWorkstreamPatternEngineSource from a JSON string
identified_workstream_pattern_engine_source_instance = IdentifiedWorkstreamPatternEngineSource.from_json(json)
# print the JSON string representation of the object
print IdentifiedWorkstreamPatternEngineSource.to_json()

# convert the object into a dict
identified_workstream_pattern_engine_source_dict = identified_workstream_pattern_engine_source_instance.to_dict()
# create an instance of IdentifiedWorkstreamPatternEngineSource from a dict
identified_workstream_pattern_engine_source_from_dict = IdentifiedWorkstreamPatternEngineSource.from_dict(identified_workstream_pattern_engine_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


