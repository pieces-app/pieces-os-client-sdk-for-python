# FlattenedIdentifiedWorkstreamPatternEngineSource

TODO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | [**WorkstreamPatternEngineSourceSupportedAccessibility**](WorkstreamPatternEngineSourceSupportedAccessibility.md) |  | [optional] 
**anchors** | [**FlattenedAnchors**](FlattenedAnchors.md) |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**filter** | **bool** | This will determine if we want to filter this specific source | [optional] 
**id** | **str** |  | 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**name** | **str** | This is the name of the source(defualt original data) this is NOT used for matching just for readability | 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**raw** | [**WorkstreamPatternEngineSource**](WorkstreamPatternEngineSource.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 
**workstream_pattern_engine_sources_vector** | **List[float]** | This is the embedding for the wpeSource.(NEEDs to collection.vector) and specific here because we can only index on a single name NOTE: this is the vector index that corresponds to the couchbase lite index. | [optional] 
**workstream_events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_identified_workstream_pattern_engine_source import FlattenedIdentifiedWorkstreamPatternEngineSource

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedIdentifiedWorkstreamPatternEngineSource from a JSON string
flattened_identified_workstream_pattern_engine_source_instance = FlattenedIdentifiedWorkstreamPatternEngineSource.from_json(json)
# print the JSON string representation of the object
print(FlattenedIdentifiedWorkstreamPatternEngineSource.to_json())

# convert the object into a dict
flattened_identified_workstream_pattern_engine_source_dict = flattened_identified_workstream_pattern_engine_source_instance.to_dict()
# create an instance of FlattenedIdentifiedWorkstreamPatternEngineSource from a dict
flattened_identified_workstream_pattern_engine_source_from_dict = FlattenedIdentifiedWorkstreamPatternEngineSource.from_dict(flattened_identified_workstream_pattern_engine_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


