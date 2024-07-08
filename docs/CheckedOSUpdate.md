# CheckedOSUpdate

This is the model for the progress of the current update of Pieces os.  /os/update/check/stream && /os/update/check/  we will emit on a progress update  updated: is an optional property that will let us know when the update was checked last.  NOTE: it is reccommended to use the stream instead of pulling. NOTE: lets think about if we want to have a closing(as well as how we want to handle restarts)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**status** | [**UpdatingStatusEnum**](UpdatingStatusEnum.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**percentage** | **float** | Optionally if the update is in progress you will recieve a download percent(from 0-100). | [optional] 

## Example

```python
from pieces_os_client.models.checked_os_update import CheckedOSUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CheckedOSUpdate from a JSON string
checked_os_update_instance = CheckedOSUpdate.from_json(json)
# print the JSON string representation of the object
print CheckedOSUpdate.to_json()

# convert the object into a dict
checked_os_update_dict = checked_os_update_instance.to_dict()
# create an instance of CheckedOSUpdate from a dict
checked_os_update_form_dict = checked_os_update.from_dict(checked_os_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


