# SeededWorkstreamSummary

This is a seeded version of a WorkstreamSummary Note: sources for the summary will be calculated based on the events used  merged: This property is only provided when a summary was created via the merged summaries flow.         If ranges are provided on the underlying summaries, then this merge property will be the most recent \"to\" date, out of the \"to\"/\"from\" pairs attached to the underlying summaries.         If ranges are not provided on the underlying summaries, then this merge property will be the most recent created date out of all of the underlying summaries.  Merged summaries specific behavior: The top-level ranges property on the merged summary ends up being the oldest from and the most recent to out of all the underlying ranges. And if the underlying ranges do not exist, then the top-level ranges property on the merge summary is the oldest created date of one of the underlying summaries and the most recent created date of one of the underlying summaries to give a to-from to the range associated to the top-level merge summary. add that this is 1 deep study at a time for now

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchors** | [**FlattenedAnchors**](FlattenedAnchors.md) |  | [optional] 
**annotations** | [**List[SeededAnnotation]**](SeededAnnotation.md) |  | [optional] 
**applications** | [**Applications**](Applications.md) |  | [optional] 
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 
**favorited** | **bool** |  | [optional] 
**mechanism** | [**MechanismEnum**](MechanismEnum.md) |  | [optional] 
**merged** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**model** | [**Model**](Model.md) |  | 
**name** | **str** |  | 
**parent_hierarchical_type** | [**WorkstreamSummaryHierarchicalParentTypeEnum**](WorkstreamSummaryHierarchicalParentTypeEnum.md) |  | [optional] 
**parent_hierarchical_type_descriptor** | **str** |  | [optional] 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**phase** | [**WorkstreamSummaryPhaseEnum**](WorkstreamSummaryPhaseEnum.md) |  | [optional] 
**processing** | [**CapabilitiesEnum**](CapabilitiesEnum.md) |  | [optional] 
**ranges** | [**FlattenedRanges**](FlattenedRanges.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**tags** | [**FlattenedTags**](FlattenedTags.md) |  | [optional] 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 
**workstream_summaries_vector** | **List[float]** | This is the embedding for the format.(NEEDs to connection.vector) and specific here because we can only index on a single name NOTE: this is the vector index that corresponds to the couchbase lite index. | [optional] 

## Example

```python
from pieces_os_client.models.seeded_workstream_summary import SeededWorkstreamSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SeededWorkstreamSummary from a JSON string
seeded_workstream_summary_instance = SeededWorkstreamSummary.from_json(json)
# print the JSON string representation of the object
print(SeededWorkstreamSummary.to_json())

# convert the object into a dict
seeded_workstream_summary_dict = seeded_workstream_summary_instance.to_dict()
# create an instance of SeededWorkstreamSummary from a dict
seeded_workstream_summary_from_dict = SeededWorkstreamSummary.from_dict(seeded_workstream_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


