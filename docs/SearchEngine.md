# SearchEngine

This will determine the type of search that will run  These are all different searching methods all of which are exclusive. Meaning that you cannot mix & match types.  operations: is here if you want to build complex searching behavior. (A || B) && (B || C) , note this can get very complex but can be as flexible as you need.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embeddings** | [**EmbeddingsSearchOptions**](EmbeddingsSearchOptions.md) |  | [optional] 
**full_text** | [**FullTextSearchOptions**](FullTextSearchOptions.md) |  | [optional] 
**operations** | [**SearchEngines**](SearchEngines.md) |  | [optional] 
**query** | **str** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**temporal** | [**TemporalSearchOptions**](TemporalSearchOptions.md) |  | [optional] 
**workstream** | [**WorkstreamSearchOptions**](WorkstreamSearchOptions.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.search_engine import SearchEngine

# TODO update the JSON string below
json = "{}"
# create an instance of SearchEngine from a JSON string
search_engine_instance = SearchEngine.from_json(json)
# print the JSON string representation of the object
print SearchEngine.to_json()

# convert the object into a dict
search_engine_dict = search_engine_instance.to_dict()
# create an instance of SearchEngine from a dict
search_engine_from_dict = SearchEngine.from_dict(search_engine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


