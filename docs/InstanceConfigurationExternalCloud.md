# InstanceConfigurationExternalCloud

Grouping of all cloud-related operations and features.  This includes connection management, allocation updates, backups, and sharing capabilities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_backup_creation** | [**CloudBackupCreationInstanceConfiguration**](CloudBackupCreationInstanceConfiguration.md) |  | [optional] 
**connect_to_cloud** | [**ConnectToCloudInstanceConfiguration**](ConnectToCloudInstanceConfiguration.md) |  | [optional] 
**delete_cloud_backup** | [**DeleteCloudBackupInstanceConfiguration**](DeleteCloudBackupInstanceConfiguration.md) |  | [optional] 
**list_cloud_backups** | [**ListCloudBackupsInstanceConfiguration**](ListCloudBackupsInstanceConfiguration.md) |  | [optional] 
**list_specific_cloud_backup** | [**ListSpecificCloudBackupInstanceConfiguration**](ListSpecificCloudBackupInstanceConfiguration.md) |  | [optional] 
**reconnect_to_cloud** | [**ReconnectToCloudInstanceConfiguration**](ReconnectToCloudInstanceConfiguration.md) |  | [optional] 
**restore_cloud_backup** | [**RestoreCloudBackupInstanceConfiguration**](RestoreCloudBackupInstanceConfiguration.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**share_snippet** | [**ShareSnippetInstanceConfiguration**](ShareSnippetInstanceConfiguration.md) |  | [optional] 
**update_allocation_cloud** | [**UpdateAllocationCloudInstanceConfiguration**](UpdateAllocationCloudInstanceConfiguration.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.instance_configuration_external_cloud import InstanceConfigurationExternalCloud

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceConfigurationExternalCloud from a JSON string
instance_configuration_external_cloud_instance = InstanceConfigurationExternalCloud.from_json(json)
# print the JSON string representation of the object
print(InstanceConfigurationExternalCloud.to_json())

# convert the object into a dict
instance_configuration_external_cloud_dict = instance_configuration_external_cloud_instance.to_dict()
# create an instance of InstanceConfigurationExternalCloud from a dict
instance_configuration_external_cloud_from_dict = InstanceConfigurationExternalCloud.from_dict(instance_configuration_external_cloud_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


