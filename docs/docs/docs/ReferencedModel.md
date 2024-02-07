# ReferencedModel

*****NOTE:***** This is the basic referencedModel, for Now since we dont have a FlattenedModel, im going to simply not include the reference, because I do NOT want to attach a Model here (would cause breaking changes if we switched from a Model -> a flattenedModel). and (2) we are under going Model changes to the Model, so would cause issues.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | 

## Example

```python
from openapi_client.models.referenced_model import ReferencedModel

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedModel from a JSON string
referenced_model_instance = ReferencedModel.from_json(json)
# print the JSON string representation of the object
print ReferencedModel.to_json()

# convert the object into a dict
referenced_model_dict = referenced_model_instance.to_dict()
# create an instance of ReferencedModel from a dict
referenced_model_form_dict = referenced_model.from_dict(referenced_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


