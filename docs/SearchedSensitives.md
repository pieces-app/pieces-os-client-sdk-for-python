# SearchedSensitives

This is the plural Model used to return many SearchedSensitive.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[SearchedSensitive]**](SearchedSensitive.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_sensitives import SearchedSensitives

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedSensitives from a JSON string
searched_sensitives_instance = SearchedSensitives.from_json(json)
# print the JSON string representation of the object
print SearchedSensitives.to_json()

# convert the object into a dict
searched_sensitives_dict = searched_sensitives_instance.to_dict()
# create an instance of SearchedSensitives from a dict
searched_sensitives_from_dict = SearchedSensitives.from_dict(searched_sensitives_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


