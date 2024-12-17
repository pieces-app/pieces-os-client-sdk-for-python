# Range

This is an identified Range, this is ONLY needed when using plural rangedTimestamps, in order to ensure granularity(add/modify/delete)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**between** | **bool** |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**var_from** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**id** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**to** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 

## Example

```python
from pieces_os_client.models.range import Range

# TODO update the JSON string below
json = "{}"
# create an instance of Range from a JSON string
range_instance = Range.from_json(json)
# print the JSON string representation of the object
print Range.to_json()

# convert the object into a dict
range_dict = range_instance.to_dict()
# create an instance of Range from a dict
range_from_dict = Range.from_dict(range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


