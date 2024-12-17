# SearchedTag

This is used for the Tags searching endpoint.  tag here is only provided if transferables are set to true.  temporal: if this is provided this means that their material matched the input via a timestamp.  TODO will want to consider returning related materials to this material potentially both associated/ and not associated materials ie suggestion: WorkstreamSuggestions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exact** | **bool** |  | 
**identifier** | **str** | This is the uuid of the tag. | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**similarity** | **float** |  | 
**tag** | [**Tag**](Tag.md) |  | [optional] 
**temporal** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_tag import SearchedTag

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedTag from a JSON string
searched_tag_instance = SearchedTag.from_json(json)
# print the JSON string representation of the object
print SearchedTag.to_json()

# convert the object into a dict
searched_tag_dict = searched_tag_instance.to_dict()
# create an instance of SearchedTag from a dict
searched_tag_from_dict = SearchedTag.from_dict(searched_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


