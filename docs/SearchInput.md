# SearchInput

generic endpoint body for the searching endpoints  query: this is optional, but the query string you will use to find your material  mode: this is the searching method/type that we will use to search your materials  TODO: consider passing in a score here ie only return things that match references/reuse/updates/...etc > x  TODO will want to consider returning related materials to this material potentially both associated/ and not associated materials, this would be an input property of suggestions?:boolean that will say if they want suggested materials returned as well

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engines** | [**SearchEngines**](SearchEngines.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.search_input import SearchInput

# TODO update the JSON string below
json = "{}"
# create an instance of SearchInput from a JSON string
search_input_instance = SearchInput.from_json(json)
# print the JSON string representation of the object
print SearchInput.to_json()

# convert the object into a dict
search_input_dict = search_input_instance.to_dict()
# create an instance of SearchInput from a dict
search_input_from_dict = SearchInput.from_dict(search_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


