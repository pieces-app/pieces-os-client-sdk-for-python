# Backups

This is a plural model of many Cloud Backups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an website id. | [optional] 
**iterable** | [**List[Backup]**](Backup.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.backups import Backups

# TODO update the JSON string below
json = "{}"
# create an instance of Backups from a JSON string
backups_instance = Backups.from_json(json)
# print the JSON string representation of the object
print Backups.to_json()

# convert the object into a dict
backups_dict = backups_instance.to_dict()
# create an instance of Backups from a dict
backups_from_dict = Backups.from_dict(backups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


