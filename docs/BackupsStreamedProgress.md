# BackupsStreamedProgress

This is used in the backups plural stream to stream the changes to all the restorations and backups in progress.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**backups** | [**List[BackupStreamedProgress]**](BackupStreamedProgress.md) |  | [optional] 
**restorations** | [**List[BackupStreamedProgress]**](BackupStreamedProgress.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.backups_streamed_progress import BackupsStreamedProgress

# TODO update the JSON string below
json = "{}"
# create an instance of BackupsStreamedProgress from a JSON string
backups_streamed_progress_instance = BackupsStreamedProgress.from_json(json)
# print the JSON string representation of the object
print BackupsStreamedProgress.to_json()

# convert the object into a dict
backups_streamed_progress_dict = backups_streamed_progress_instance.to_dict()
# create an instance of BackupsStreamedProgress from a dict
backups_streamed_progress_from_dict = BackupsStreamedProgress.from_dict(backups_streamed_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


