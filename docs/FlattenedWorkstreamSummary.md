# FlattenedWorkstreamSummary

This is a DAG-Safe minimal representation of a workstream summary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | 
**score** | [**Score**](Score.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 
**name** | **str** |  | 
**annotations** | [**FlattenedAnnotations**](FlattenedAnnotations.md) |  | [optional] 
**ranges** | [**FlattenedRanges**](FlattenedRanges.md) |  | [optional] 
**model** | [**Model**](Model.md) |  | 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 
**anchors** | [**FlattenedAnchors**](FlattenedAnchors.md) |  | [optional] 
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**applications** | [**Applications**](Applications.md) |  | [optional] 
**tags** | [**FlattenedTags**](FlattenedTags.md) |  | [optional] 
**sources** | [**FlattenedIdentifiedWorkstreamPatternEngineSources**](FlattenedIdentifiedWorkstreamPatternEngineSources.md) |  | [optional] 
**workstream_summaries_vector** | **List[float]** | This is the embedding for the format.(NEEDs to connection.vector) and specific here because we can only index on a single name | [optional] 
**processing** | [**CapabilitiesEnum**](CapabilitiesEnum.md) |  | [optional] 
**favorited** | **bool** |  | [optional] 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_workstream_summary import FlattenedWorkstreamSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedWorkstreamSummary from a JSON string
flattened_workstream_summary_instance = FlattenedWorkstreamSummary.from_json(json)
# print the JSON string representation of the object
print FlattenedWorkstreamSummary.to_json()

# convert the object into a dict
flattened_workstream_summary_dict = flattened_workstream_summary_instance.to_dict()
# create an instance of FlattenedWorkstreamSummary from a dict
flattened_workstream_summary_from_dict = FlattenedWorkstreamSummary.from_dict(flattened_workstream_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


