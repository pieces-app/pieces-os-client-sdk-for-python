# Embedding



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**model** | [**Model**](Model.md) |  | 
**raw** | **List[float]** | this is the raw value of the embedding | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 

## Example

```python
from pieces_os_client.models.embedding import Embedding

# TODO update the JSON string below
json = "{}"
# create an instance of Embedding from a JSON string
embedding_instance = Embedding.from_json(json)
# print the JSON string representation of the object
print Embedding.to_json()

# convert the object into a dict
embedding_dict = embedding_instance.to_dict()
# create an instance of Embedding from a dict
embedding_from_dict = Embedding.from_dict(embedding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


