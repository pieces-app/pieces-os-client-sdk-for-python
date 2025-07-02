# UserLastCheckedInStreamOutput

This model represents the data streamed over the user last checked in websocket endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**user_id** | **str** | The user ID, can be null if no user is logged in. | [optional] 
**last_checked_in** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**needs_refresh** | **bool** | Indicates whether the client needs to refresh its data. | 
**update_required** | **bool** | Indicates whether POS requires an update. | [optional] 

## Example

```python
from pieces_os_client.models.user_last_checked_in_stream_output import UserLastCheckedInStreamOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UserLastCheckedInStreamOutput from a JSON string
user_last_checked_in_stream_output_instance = UserLastCheckedInStreamOutput.from_json(json)
# print the JSON string representation of the object
print UserLastCheckedInStreamOutput.to_json()

# convert the object into a dict
user_last_checked_in_stream_output_dict = user_last_checked_in_stream_output_instance.to_dict()
# create an instance of UserLastCheckedInStreamOutput from a dict
user_last_checked_in_stream_output_from_dict = UserLastCheckedInStreamOutput.from_dict(user_last_checked_in_stream_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


