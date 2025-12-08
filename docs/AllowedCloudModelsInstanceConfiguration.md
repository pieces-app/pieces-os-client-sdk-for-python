# AllowedCloudModelsInstanceConfiguration

Configuration for allowed cloud models with allow-list  note: this model can scale to use rate-limits and so on in the future

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_models** | [**InstanceConfigurationAllowedModels**](InstanceConfigurationAllowedModels.md) |  | [optional] 
**default_models** | [**InstanceConfigurationAllowedCloudModelsDefaultModels**](InstanceConfigurationAllowedCloudModelsDefaultModels.md) |  | [optional] 
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.allowed_cloud_models_instance_configuration import AllowedCloudModelsInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedCloudModelsInstanceConfiguration from a JSON string
allowed_cloud_models_instance_configuration_instance = AllowedCloudModelsInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(AllowedCloudModelsInstanceConfiguration.to_json())

# convert the object into a dict
allowed_cloud_models_instance_configuration_dict = allowed_cloud_models_instance_configuration_instance.to_dict()
# create an instance of AllowedCloudModelsInstanceConfiguration from a dict
allowed_cloud_models_instance_configuration_from_dict = AllowedCloudModelsInstanceConfiguration.from_dict(allowed_cloud_models_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


