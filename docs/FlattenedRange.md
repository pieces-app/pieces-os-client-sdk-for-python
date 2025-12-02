# FlattenedRange

This is a DAG-Safe minimal representation of a Range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**between** | **bool** |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**var_from** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**id** | **str** |  | 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**to** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 

## Example

```python
from pieces_os_client.models.flattened_range import FlattenedRange

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedRange from a JSON string
flattened_range_instance = FlattenedRange.from_json(json)
# print the JSON string representation of the object
print(FlattenedRange.to_json())

# convert the object into a dict
flattened_range_dict = flattened_range_instance.to_dict()
# create an instance of FlattenedRange from a dict
flattened_range_from_dict = FlattenedRange.from_dict(flattened_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


