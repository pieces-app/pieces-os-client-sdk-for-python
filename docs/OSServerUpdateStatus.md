# OSServerUpdateStatus

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
from pieces_os_client.models.os_server_update_status import OSServerUpdateStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OSServerUpdateStatus from a JSON string
os_server_update_status_instance = OSServerUpdateStatus.from_json(json)
# print the JSON string representation of the object
print OSServerUpdateStatus.to_json()

# convert the object into a dict
os_server_update_status_dict = os_server_update_status_instance.to_dict()
# create an instance of OSServerUpdateStatus from a dict
os_server_update_status_from_dict = OSServerUpdateStatus.from_dict(os_server_update_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


