# SearchedWebsites

This is the plural Model used to return many SearchedWebsite.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[SearchedWebsite]**](SearchedWebsite.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_websites import SearchedWebsites

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedWebsites from a JSON string
searched_websites_instance = SearchedWebsites.from_json(json)
# print the JSON string representation of the object
print(SearchedWebsites.to_json())

# convert the object into a dict
searched_websites_dict = searched_websites_instance.to_dict()
# create an instance of SearchedWebsites from a dict
searched_websites_from_dict = SearchedWebsites.from_dict(searched_websites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


