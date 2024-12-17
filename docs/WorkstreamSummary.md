# WorkstreamSummary

This is representation or a summarized version of the highly relevant WorkstreamEvent events from a given time period, 1 day, 1 week, 1 month, dependinng on your given flow.

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

## Example

```python
from pieces_os_client.models.workstream_summary import WorkstreamSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSummary from a JSON string
workstream_summary_instance = WorkstreamSummary.from_json(json)
# print the JSON string representation of the object
print WorkstreamSummary.to_json()

# convert the object into a dict
workstream_summary_dict = workstream_summary_instance.to_dict()
# create an instance of WorkstreamSummary from a dict
workstream_summary_from_dict = WorkstreamSummary.from_dict(workstream_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


