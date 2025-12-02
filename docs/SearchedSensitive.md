# SearchedSensitive

This is used for the Sensitives searching endpoint.  sensitive here is only provided if transferables are set to true.  temporal: if this is provided this means that their material matched the input via a timestamp.  TODO will want to consider returning related materials to this material potentially both associated/ and not associated materials ie suggestion: WorkstreamSuggestions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exact** | **bool** |  | 
**identifier** | **str** | This is the uuid of the sensitive. | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**sensitive** | [**Sensitive**](Sensitive.md) |  | [optional] 
**similarity** | **float** |  | 
**temporal** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_sensitive import SearchedSensitive

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedSensitive from a JSON string
searched_sensitive_instance = SearchedSensitive.from_json(json)
# print the JSON string representation of the object
print(SearchedSensitive.to_json())

# convert the object into a dict
searched_sensitive_dict = searched_sensitive_instance.to_dict()
# create an instance of SearchedSensitive from a dict
searched_sensitive_from_dict = SearchedSensitive.from_dict(searched_sensitive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


