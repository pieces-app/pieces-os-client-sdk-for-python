# Session

This is a specific model that will let us know at what time this user was using the application.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**id** | **str** | The UUID of the current Session | 
**opened** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 

## Example

```python
from pieces_os_client.models.session import Session

# TODO update the JSON string below
json = "{}"
# create an instance of Session from a JSON string
session_instance = Session.from_json(json)
# print the JSON string representation of the object
print Session.to_json()

# convert the object into a dict
session_dict = session_instance.to_dict()
# create an instance of Session from a dict
session_from_dict = Session.from_dict(session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


