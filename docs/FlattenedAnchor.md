# FlattenedAnchor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | 
**type** | [**AnchorTypeEnum**](AnchorTypeEnum.md) |  | 
**watch** | **bool** |  | [optional] 
**points** | [**FlattenedAnchorPoints**](FlattenedAnchorPoints.md) |  | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**name** | **str** |  | [optional] 
**annotations** | [**FlattenedAnnotations**](FlattenedAnnotations.md) |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**workstream_events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 
**sources** | [**FlattenedIdentifiedWorkstreamPatternEngineSources**](FlattenedIdentifiedWorkstreamPatternEngineSources.md) |  | [optional] 
**tags** | [**FlattenedTags**](FlattenedTags.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_anchor import FlattenedAnchor

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedAnchor from a JSON string
flattened_anchor_instance = FlattenedAnchor.from_json(json)
# print the JSON string representation of the object
print FlattenedAnchor.to_json()

# convert the object into a dict
flattened_anchor_dict = flattened_anchor_instance.to_dict()
# create an instance of FlattenedAnchor from a dict
flattened_anchor_from_dict = FlattenedAnchor.from_dict(flattened_anchor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


