# ConnectToCloudInstanceConfiguration

Configuration for the Connect to Cloud feature.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.connect_to_cloud_instance_configuration import ConnectToCloudInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectToCloudInstanceConfiguration from a JSON string
connect_to_cloud_instance_configuration_instance = ConnectToCloudInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(ConnectToCloudInstanceConfiguration.to_json())

# convert the object into a dict
connect_to_cloud_instance_configuration_dict = connect_to_cloud_instance_configuration_instance.to_dict()
# create an instance of ConnectToCloudInstanceConfiguration from a dict
connect_to_cloud_instance_configuration_from_dict = ConnectToCloudInstanceConfiguration.from_dict(connect_to_cloud_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


