# ModelDeleteCacheOutput

This is the output model for '/model/{model}/delete/cache'

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**ReferencedModel**](ReferencedModel.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.model_delete_cache_output import ModelDeleteCacheOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ModelDeleteCacheOutput from a JSON string
model_delete_cache_output_instance = ModelDeleteCacheOutput.from_json(json)
# print the JSON string representation of the object
print(ModelDeleteCacheOutput.to_json())

# convert the object into a dict
model_delete_cache_output_dict = model_delete_cache_output_instance.to_dict()
# create an instance of ModelDeleteCacheOutput from a dict
model_delete_cache_output_from_dict = ModelDeleteCacheOutput.from_dict(model_delete_cache_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


