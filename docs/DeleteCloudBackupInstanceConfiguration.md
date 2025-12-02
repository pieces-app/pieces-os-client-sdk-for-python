# DeleteCloudBackupInstanceConfiguration

Configuration for the Delete Cloud Backup feature (toggle only).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.delete_cloud_backup_instance_configuration import DeleteCloudBackupInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCloudBackupInstanceConfiguration from a JSON string
delete_cloud_backup_instance_configuration_instance = DeleteCloudBackupInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(DeleteCloudBackupInstanceConfiguration.to_json())

# convert the object into a dict
delete_cloud_backup_instance_configuration_dict = delete_cloud_backup_instance_configuration_instance.to_dict()
# create an instance of DeleteCloudBackupInstanceConfiguration from a dict
delete_cloud_backup_instance_configuration_from_dict = DeleteCloudBackupInstanceConfiguration.from_dict(delete_cloud_backup_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


