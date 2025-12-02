# SearchedEntity

This is used for the Entities searching endpoint. Entity here is only provided if transferables are set to true.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**Entity**](Entity.md) |  | [optional] 
**exact** | **bool** | Whether this is an exact match | [optional] 
**identifier** | **str** | This is the UUID of the Entity. | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**similarity** | **float** | Similarity score for the match | [optional] 

## Example

```python
from pieces_os_client.models.searched_entity import SearchedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedEntity from a JSON string
searched_entity_instance = SearchedEntity.from_json(json)
# print the JSON string representation of the object
print(SearchedEntity.to_json())

# convert the object into a dict
searched_entity_dict = searched_entity_instance.to_dict()
# create an instance of SearchedEntity from a dict
searched_entity_from_dict = SearchedEntity.from_dict(searched_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


