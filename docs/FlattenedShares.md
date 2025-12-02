# FlattenedShares

This is just an iterable of our individual share models.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[FlattenedShare]**](FlattenedShare.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_shares import FlattenedShares

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedShares from a JSON string
flattened_shares_instance = FlattenedShares.from_json(json)
# print the JSON string representation of the object
print(FlattenedShares.to_json())

# convert the object into a dict
flattened_shares_dict = flattened_shares_instance.to_dict()
# create an instance of FlattenedShares from a dict
flattened_shares_from_dict = FlattenedShares.from_dict(flattened_shares_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


