# ListCloudBackupsInstanceConfiguration

Configuration for the List Cloud Backups feature (toggle only).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.list_cloud_backups_instance_configuration import ListCloudBackupsInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ListCloudBackupsInstanceConfiguration from a JSON string
list_cloud_backups_instance_configuration_instance = ListCloudBackupsInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(ListCloudBackupsInstanceConfiguration.to_json())

# convert the object into a dict
list_cloud_backups_instance_configuration_dict = list_cloud_backups_instance_configuration_instance.to_dict()
# create an instance of ListCloudBackupsInstanceConfiguration from a dict
list_cloud_backups_instance_configuration_from_dict = ListCloudBackupsInstanceConfiguration.from_dict(list_cloud_backups_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


