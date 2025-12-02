# ReconnectToCloudInstanceConfiguration

Configuration for the Reconnect to Cloud feature (toggle only).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.reconnect_to_cloud_instance_configuration import ReconnectToCloudInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ReconnectToCloudInstanceConfiguration from a JSON string
reconnect_to_cloud_instance_configuration_instance = ReconnectToCloudInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(ReconnectToCloudInstanceConfiguration.to_json())

# convert the object into a dict
reconnect_to_cloud_instance_configuration_dict = reconnect_to_cloud_instance_configuration_instance.to_dict()
# create an instance of ReconnectToCloudInstanceConfiguration from a dict
reconnect_to_cloud_instance_configuration_from_dict = ReconnectToCloudInstanceConfiguration.from_dict(reconnect_to_cloud_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


