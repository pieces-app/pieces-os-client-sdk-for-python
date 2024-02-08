# SeededModels

This is a Model that will hold an iterable of SeededModels.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[SeededModel]**](SeededModel.md) |  | 

## Example

```python
from openapi_client.models.seeded_models import SeededModels

# TODO update the JSON string below
json = "{}"
# create an instance of SeededModels from a JSON string
seeded_models_instance = SeededModels.from_json(json)
# print the JSON string representation of the object
print SeededModels.to_json()

# convert the object into a dict
seeded_models_dict = seeded_models_instance.to_dict()
# create an instance of SeededModels from a dict
seeded_models_form_dict = seeded_models.from_dict(seeded_models_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


