# InactiveOSServerApplet

Note: parent is optional here in the case that (parent here is the integration that wants the module launched(VSCode))

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**Application**](Application.md) |  | [optional] 
**port** | **int** | This is the port number in which we want to serve the copilot at. | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**type** | [**OSAppletEnum**](OSAppletEnum.md) |  | 

## Example

```python
from pieces_os_client.models.inactive_os_server_applet import InactiveOSServerApplet

# TODO update the JSON string below
json = "{}"
# create an instance of InactiveOSServerApplet from a JSON string
inactive_os_server_applet_instance = InactiveOSServerApplet.from_json(json)
# print the JSON string representation of the object
print InactiveOSServerApplet.to_json()

# convert the object into a dict
inactive_os_server_applet_dict = inactive_os_server_applet_instance.to_dict()
# create an instance of InactiveOSServerApplet from a dict
inactive_os_server_applet_from_dict = InactiveOSServerApplet.from_dict(inactive_os_server_applet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


