# GroupedTimestamp

A helper classs to wrap Date-Time Values with Useful Helper Properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**readable** | **str** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**value** | **datetime** |  | 

## Example

```python
from pieces_os_client.models.grouped_timestamp import GroupedTimestamp

# TODO update the JSON string below
json = "{}"
# create an instance of GroupedTimestamp from a JSON string
grouped_timestamp_instance = GroupedTimestamp.from_json(json)
# print the JSON string representation of the object
print(GroupedTimestamp.to_json())

# convert the object into a dict
grouped_timestamp_dict = grouped_timestamp_instance.to_dict()
# create an instance of GroupedTimestamp from a dict
grouped_timestamp_from_dict = GroupedTimestamp.from_dict(grouped_timestamp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


