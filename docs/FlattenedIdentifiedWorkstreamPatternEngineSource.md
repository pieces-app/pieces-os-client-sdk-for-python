# FlattenedIdentifiedWorkstreamPatternEngineSource

TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | 
**raw** | [**WorkstreamPatternEngineSource**](WorkstreamPatternEngineSource.md) |  | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**filter** | **bool** | This will determine if we want to filter this specific source | [optional] 
**name** | **str** | This is the name of the source(defualt original data) this is NOT used for matching just for readability | 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**workstream_events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**accessibility** | [**WorkstreamPatternEngineSourceSupportedAccessibility**](WorkstreamPatternEngineSourceSupportedAccessibility.md) |  | [optional] 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 
**anchors** | [**FlattenedAnchors**](FlattenedAnchors.md) |  | [optional] 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**workstream_pattern_engine_sources_vector** | **List[float]** | This is the embedding for the wpeSource.(NEEDs to collectionection.vector) and specific here because we can only index on a single name NOTE: this the the vector index that corresponds the the couchbase lite index. | [optional] 

## Example

```python
from pieces_os_client.models.flattened_identified_workstream_pattern_engine_source import FlattenedIdentifiedWorkstreamPatternEngineSource

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedIdentifiedWorkstreamPatternEngineSource from a JSON string
flattened_identified_workstream_pattern_engine_source_instance = FlattenedIdentifiedWorkstreamPatternEngineSource.from_json(json)
# print the JSON string representation of the object
print FlattenedIdentifiedWorkstreamPatternEngineSource.to_json()

# convert the object into a dict
flattened_identified_workstream_pattern_engine_source_dict = flattened_identified_workstream_pattern_engine_source_instance.to_dict()
# create an instance of FlattenedIdentifiedWorkstreamPatternEngineSource from a dict
flattened_identified_workstream_pattern_engine_source_from_dict = FlattenedIdentifiedWorkstreamPatternEngineSource.from_dict(flattened_identified_workstream_pattern_engine_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


