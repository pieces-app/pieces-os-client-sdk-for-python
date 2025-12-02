# SearchedHints

This is the plural Model used to return many SearchedHint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[SearchedHint]**](SearchedHint.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_hints import SearchedHints

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedHints from a JSON string
searched_hints_instance = SearchedHints.from_json(json)
# print the JSON string representation of the object
print(SearchedHints.to_json())

# convert the object into a dict
searched_hints_dict = searched_hints_instance.to_dict()
# create an instance of SearchedHints from a dict
searched_hints_from_dict = SearchedHints.from_dict(searched_hints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


