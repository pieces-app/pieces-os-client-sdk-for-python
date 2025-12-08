# ListSpecificCloudBackupInstanceConfiguration

Configuration for the List Specific Cloud Backup feature (toggle only).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.list_specific_cloud_backup_instance_configuration import ListSpecificCloudBackupInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ListSpecificCloudBackupInstanceConfiguration from a JSON string
list_specific_cloud_backup_instance_configuration_instance = ListSpecificCloudBackupInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(ListSpecificCloudBackupInstanceConfiguration.to_json())

# convert the object into a dict
list_specific_cloud_backup_instance_configuration_dict = list_specific_cloud_backup_instance_configuration_instance.to_dict()
# create an instance of ListSpecificCloudBackupInstanceConfiguration from a dict
list_specific_cloud_backup_instance_configuration_from_dict = ListSpecificCloudBackupInstanceConfiguration.from_dict(list_specific_cloud_backup_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


