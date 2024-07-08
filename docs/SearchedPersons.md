# SearchedPersons

This is the plural Model used to return many SearchedPerson.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[SearchedPerson]**](SearchedPerson.md) |  | 

## Example

```python
from pieces_os_client.models.searched_persons import SearchedPersons

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedPersons from a JSON string
searched_persons_instance = SearchedPersons.from_json(json)
# print the JSON string representation of the object
print SearchedPersons.to_json()

# convert the object into a dict
searched_persons_dict = searched_persons_instance.to_dict()
# create an instance of SearchedPersons from a dict
searched_persons_from_dict = SearchedPersons.from_dict(searched_persons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


