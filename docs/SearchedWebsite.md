# SearchedWebsite

This is used for the Websites searching endpoint.  website here is only provided if transferables are set to true.  temporal: if this is provided this means that their material matched the input via a timestamp.  TODO will want to consider returning related materials to this material potentially both associated/ and not associated materials ie suggestion: WorkstreamSuggestions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**website** | [**Website**](Website.md) |  | [optional] 
**exact** | **bool** |  | 
**similarity** | **float** |  | 
**temporal** | **bool** |  | [optional] 
**identifier** | **str** | This is the uuid of the website. | 

## Example

```python
from pieces_os_client.models.searched_website import SearchedWebsite

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedWebsite from a JSON string
searched_website_instance = SearchedWebsite.from_json(json)
# print the JSON string representation of the object
print SearchedWebsite.to_json()

# convert the object into a dict
searched_website_dict = searched_website_instance.to_dict()
# create an instance of SearchedWebsite from a dict
searched_website_from_dict = SearchedWebsite.from_dict(searched_website_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


