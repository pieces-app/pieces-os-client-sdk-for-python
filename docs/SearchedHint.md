# SearchedHint

This is used for the Hint searching endpoint  hint here is only provided if transferables are set to true.  temporal: if this is provided this means that their material matched the input via a timestamp.  TODO will want to consider returning related materials to this material potentially both associated/ and not associated materials ie suggestion: WorkstreamSuggestions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**hint** | [**Hint**](Hint.md) |  | [optional] 
**exact** | **bool** |  | 
**similarity** | **float** |  | 
**temporal** | **bool** |  | [optional] 
**identifier** | **str** | This is the uuid of the hint. | 

## Example

```python
from pieces_os_client.models.searched_hint import SearchedHint

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedHint from a JSON string
searched_hint_instance = SearchedHint.from_json(json)
# print the JSON string representation of the object
print SearchedHint.to_json()

# convert the object into a dict
searched_hint_dict = searched_hint_instance.to_dict()
# create an instance of SearchedHint from a dict
searched_hint_from_dict = SearchedHint.from_dict(searched_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


