# InstanceConfiguration

Configuration settings for the entity.  Extended with strongly-typed per-feature properties organized into hierarchical groupings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytics** | [**InstanceConfigurationAnalytics**](InstanceConfigurationAnalytics.md) |  | [optional] 
**external_cloud** | [**InstanceConfigurationExternalCloud**](InstanceConfigurationExternalCloud.md) |  | [optional] 
**external_provider** | [**InstanceConfigurationExternalProvider**](InstanceConfigurationExternalProvider.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.instance_configuration import InstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceConfiguration from a JSON string
instance_configuration_instance = InstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(InstanceConfiguration.to_json())

# convert the object into a dict
instance_configuration_dict = instance_configuration_instance.to_dict()
# create an instance of InstanceConfiguration from a dict
instance_configuration_from_dict = InstanceConfiguration.from_dict(instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


