# BackupStreamedProgress

This is a specific model to the /backups/create/streamed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**status** | [**ModelDownloadProgressStatusEnum**](ModelDownloadProgressStatusEnum.md) |  | [optional] 
**percentage** | **float** | Optionally if the download is in progress you will recieve a download percent(from 0-100). | [optional] 
**backup** | [**Backup**](Backup.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.backup_streamed_progress import BackupStreamedProgress

# TODO update the JSON string below
json = "{}"
# create an instance of BackupStreamedProgress from a JSON string
backup_streamed_progress_instance = BackupStreamedProgress.from_json(json)
# print the JSON string representation of the object
print BackupStreamedProgress.to_json()

# convert the object into a dict
backup_streamed_progress_dict = backup_streamed_progress_instance.to_dict()
# create an instance of BackupStreamedProgress from a dict
backup_streamed_progress_form_dict = backup_streamed_progress.from_dict(backup_streamed_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


