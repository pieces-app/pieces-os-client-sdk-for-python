# SearchedTags

This is the plural Model used to return many searchedTags.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[SearchedTag]**](SearchedTag.md) |  | 

## Example

```python
from pieces_os_client.models.searched_tags import SearchedTags

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedTags from a JSON string
searched_tags_instance = SearchedTags.from_json(json)
# print the JSON string representation of the object
print SearchedTags.to_json()

# convert the object into a dict
searched_tags_dict = searched_tags_instance.to_dict()
# create an instance of SearchedTags from a dict
searched_tags_from_dict = SearchedTags.from_dict(searched_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


