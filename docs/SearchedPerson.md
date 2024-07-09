# SearchedPerson

This is used for the Persons searching endpoint.  person here is only provided if transferables are set to true.  temporal: if this is provided this means that their material matched the input via a timestamp.  TODO will want to consider returning related materials to this material potentially both associated/ and not associated materials ie suggestion: WorkstreamSuggestions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**person** | [**Person**](Person.md) |  | [optional] 
**exact** | **bool** |  | 
**similarity** | **float** |  | 
**temporal** | **bool** |  | [optional] 
**identifier** | **str** | This is the uuid of the person. | 

## Example

```python
from pieces_os_client.models.searched_person import SearchedPerson

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedPerson from a JSON string
searched_person_instance = SearchedPerson.from_json(json)
# print the JSON string representation of the object
print SearchedPerson.to_json()

# convert the object into a dict
searched_person_dict = searched_person_instance.to_dict()
# create an instance of SearchedPerson from a dict
searched_person_from_dict = SearchedPerson.from_dict(searched_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


