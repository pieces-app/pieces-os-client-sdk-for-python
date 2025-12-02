# SeededBackup

This is a precursor to a Backup, for now this will not need to take any properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_backup import SeededBackup

# TODO update the JSON string below
json = "{}"
# create an instance of SeededBackup from a JSON string
seeded_backup_instance = SeededBackup.from_json(json)
# print the JSON string representation of the object
print(SeededBackup.to_json())

# convert the object into a dict
seeded_backup_dict = seeded_backup_instance.to_dict()
# create an instance of SeededBackup from a dict
seeded_backup_from_dict = SeededBackup.from_dict(seeded_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


