# InstanceConfigurationAllowedModels

A collection of allowed models for an entity configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[InstanceConfigurationAllowedModel]**](InstanceConfigurationAllowedModel.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.instance_configuration_allowed_models import InstanceConfigurationAllowedModels

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceConfigurationAllowedModels from a JSON string
instance_configuration_allowed_models_instance = InstanceConfigurationAllowedModels.from_json(json)
# print the JSON string representation of the object
print(InstanceConfigurationAllowedModels.to_json())

# convert the object into a dict
instance_configuration_allowed_models_dict = instance_configuration_allowed_models_instance.to_dict()
# create an instance of InstanceConfigurationAllowedModels from a dict
instance_configuration_allowed_models_from_dict = InstanceConfigurationAllowedModels.from_dict(instance_configuration_allowed_models_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


