# InstanceConfigurationAllowedCloudModelsDefaultModels

Default model configurations for different use cases in allowed cloud models instance configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accurate** | [**InstanceConfigurationAllowedModel**](InstanceConfigurationAllowedModel.md) |  | [optional] 
**fallback_accurate** | [**InstanceConfigurationAllowedModel**](InstanceConfigurationAllowedModel.md) |  | [optional] 
**fallback_fast** | [**InstanceConfigurationAllowedModel**](InstanceConfigurationAllowedModel.md) |  | [optional] 
**fast** | [**InstanceConfigurationAllowedModel**](InstanceConfigurationAllowedModel.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.instance_configuration_allowed_cloud_models_default_models import InstanceConfigurationAllowedCloudModelsDefaultModels

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceConfigurationAllowedCloudModelsDefaultModels from a JSON string
instance_configuration_allowed_cloud_models_default_models_instance = InstanceConfigurationAllowedCloudModelsDefaultModels.from_json(json)
# print the JSON string representation of the object
print(InstanceConfigurationAllowedCloudModelsDefaultModels.to_json())

# convert the object into a dict
instance_configuration_allowed_cloud_models_default_models_dict = instance_configuration_allowed_cloud_models_default_models_instance.to_dict()
# create an instance of InstanceConfigurationAllowedCloudModelsDefaultModels from a dict
instance_configuration_allowed_cloud_models_default_models_from_dict = InstanceConfigurationAllowedCloudModelsDefaultModels.from_dict(instance_configuration_allowed_cloud_models_default_models_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


