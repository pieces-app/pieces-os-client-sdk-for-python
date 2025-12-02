# RestoreCloudBackupInstanceConfiguration

Configuration for the Restore Cloud Backup feature (toggle only).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.restore_cloud_backup_instance_configuration import RestoreCloudBackupInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreCloudBackupInstanceConfiguration from a JSON string
restore_cloud_backup_instance_configuration_instance = RestoreCloudBackupInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(RestoreCloudBackupInstanceConfiguration.to_json())

# convert the object into a dict
restore_cloud_backup_instance_configuration_dict = restore_cloud_backup_instance_configuration_instance.to_dict()
# create an instance of RestoreCloudBackupInstanceConfiguration from a dict
restore_cloud_backup_instance_configuration_from_dict = RestoreCloudBackupInstanceConfiguration.from_dict(restore_cloud_backup_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


