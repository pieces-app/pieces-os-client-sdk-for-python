# ModelMaxTokens

This will describe the MaxTokens for an MLModel  total is required.  iff there is a differentiator with inputs/outputs, then we can also provide those as well.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **float** |  | [optional] 
**output** | **float** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**total** | **float** |  | 

## Example

```python
from pieces_os_client.models.model_max_tokens import ModelMaxTokens

# TODO update the JSON string below
json = "{}"
# create an instance of ModelMaxTokens from a JSON string
model_max_tokens_instance = ModelMaxTokens.from_json(json)
# print the JSON string representation of the object
print(ModelMaxTokens.to_json())

# convert the object into a dict
model_max_tokens_dict = model_max_tokens_instance.to_dict()
# create an instance of ModelMaxTokens from a dict
model_max_tokens_from_dict = ModelMaxTokens.from_dict(model_max_tokens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


