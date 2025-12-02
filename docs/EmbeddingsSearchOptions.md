# EmbeddingsSearchOptions

similarity: this is optional from 0 - 1, (where 1 is exact and 0 is everything)  TODO consider a plural of types for running many embedding search scopes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**similarity** | **float** |  | [optional] 
**type** | [**EmbeddingsSearchOptionsEmbeddingTypeEnum**](EmbeddingsSearchOptionsEmbeddingTypeEnum.md) |  | 

## Example

```python
from pieces_os_client.models.embeddings_search_options import EmbeddingsSearchOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingsSearchOptions from a JSON string
embeddings_search_options_instance = EmbeddingsSearchOptions.from_json(json)
# print the JSON string representation of the object
print(EmbeddingsSearchOptions.to_json())

# convert the object into a dict
embeddings_search_options_dict = embeddings_search_options_instance.to_dict()
# create an instance of EmbeddingsSearchOptions from a dict
embeddings_search_options_from_dict = EmbeddingsSearchOptions.from_dict(embeddings_search_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


