# SeededWorkstreamSummary

This is a seeded version of a WorkstreamSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 
**name** | **str** |  | 
**annotations** | [**List[SeededAnnotation]**](SeededAnnotation.md) |  | [optional] 
**ranges** | [**FlattenedRanges**](FlattenedRanges.md) |  | [optional] 
**model** | [**Model**](Model.md) |  | 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 
**anchors** | [**FlattenedAnchors**](FlattenedAnchors.md) |  | [optional] 
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**applications** | [**Applications**](Applications.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_workstream_summary import SeededWorkstreamSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SeededWorkstreamSummary from a JSON string
seeded_workstream_summary_instance = SeededWorkstreamSummary.from_json(json)
# print the JSON string representation of the object
print SeededWorkstreamSummary.to_json()

# convert the object into a dict
seeded_workstream_summary_dict = seeded_workstream_summary_instance.to_dict()
# create an instance of SeededWorkstreamSummary from a dict
seeded_workstream_summary_from_dict = SeededWorkstreamSummary.from_dict(seeded_workstream_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


