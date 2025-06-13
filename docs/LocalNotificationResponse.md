# LocalNotificationResponse

For now this will just return the id of the notification  This will be light weight in order to scale.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **int** |  | 

## Example

```python
from pieces_os_client.models.local_notification_response import LocalNotificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LocalNotificationResponse from a JSON string
local_notification_response_instance = LocalNotificationResponse.from_json(json)
# print the JSON string representation of the object
print LocalNotificationResponse.to_json()

# convert the object into a dict
local_notification_response_dict = local_notification_response_instance.to_dict()
# create an instance of LocalNotificationResponse from a dict
local_notification_response_from_dict = LocalNotificationResponse.from_dict(local_notification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


