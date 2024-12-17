# FullTextSearchOptions

similarity: you will want to pass in a value from 0-1. (where 1 is exact and 0 is everything)  exact: (optional) this will default to false, which will run a fuzzy search, unless set to true.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exact** | **bool** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**similarity** | **float** |  | [optional] 

## Example

```python
from pieces_os_client.models.full_text_search_options import FullTextSearchOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FullTextSearchOptions from a JSON string
full_text_search_options_instance = FullTextSearchOptions.from_json(json)
# print the JSON string representation of the object
print FullTextSearchOptions.to_json()

# convert the object into a dict
full_text_search_options_dict = full_text_search_options_instance.to_dict()
# create an instance of FullTextSearchOptions from a dict
full_text_search_options_from_dict = FullTextSearchOptions.from_dict(full_text_search_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


