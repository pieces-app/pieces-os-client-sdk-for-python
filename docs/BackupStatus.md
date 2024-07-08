# BackupStatus

TODO add more description to this.  can eventually add a number that display the percent downloaded an so on.(this is called percent 0-100)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**value** | [**BackupStatusEnum**](BackupStatusEnum.md) |  | [optional] 
**percentage** | **float** | Optionally if the download is in progress you will receive a download percent(from 0-100). | [optional] 
**backup** | [**Backup**](Backup.md) |  | 

## Example

```python
from pieces_os_client.models.backup_status import BackupStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BackupStatus from a JSON string
backup_status_instance = BackupStatus.from_json(json)
# print the JSON string representation of the object
print BackupStatus.to_json()

# convert the object into a dict
backup_status_dict = backup_status_instance.to_dict()
# create an instance of BackupStatus from a dict
backup_status_from_dict = BackupStatus.from_dict(backup_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


