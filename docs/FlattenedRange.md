# FlattenedRange

This is a DAG-Safe minimal representation of a Range.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | 
**score** | [**Score**](Score.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**to** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**var_from** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**between** | **bool** |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_range import FlattenedRange

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedRange from a JSON string
flattened_range_instance = FlattenedRange.from_json(json)
# print the JSON string representation of the object
print FlattenedRange.to_json()

# convert the object into a dict
flattened_range_dict = flattened_range_instance.to_dict()
# create an instance of FlattenedRange from a dict
flattened_range_from_dict = FlattenedRange.from_dict(flattened_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


