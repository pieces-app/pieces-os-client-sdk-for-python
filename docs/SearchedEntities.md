# SearchedEntities

This is the plural model used to return many SearchedEntity results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[SearchedEntity]**](SearchedEntity.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_entities import SearchedEntities

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedEntities from a JSON string
searched_entities_instance = SearchedEntities.from_json(json)
# print the JSON string representation of the object
print(SearchedEntities.to_json())

# convert the object into a dict
searched_entities_dict = searched_entities_instance.to_dict()
# create an instance of SearchedEntities from a dict
searched_entities_from_dict = SearchedEntities.from_dict(searched_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


