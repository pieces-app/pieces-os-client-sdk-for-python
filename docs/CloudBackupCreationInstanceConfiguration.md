# CloudBackupCreationInstanceConfiguration

Configuration for the Cloud Backup Creation feature (toggle only).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.cloud_backup_creation_instance_configuration import CloudBackupCreationInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CloudBackupCreationInstanceConfiguration from a JSON string
cloud_backup_creation_instance_configuration_instance = CloudBackupCreationInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(CloudBackupCreationInstanceConfiguration.to_json())

# convert the object into a dict
cloud_backup_creation_instance_configuration_dict = cloud_backup_creation_instance_configuration_instance.to_dict()
# create an instance of CloudBackupCreationInstanceConfiguration from a dict
cloud_backup_creation_instance_configuration_from_dict = CloudBackupCreationInstanceConfiguration.from_dict(cloud_backup_creation_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


