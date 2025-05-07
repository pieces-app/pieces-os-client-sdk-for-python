# TerminatingOSServerApplet

TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**parent** | [**Application**](Application.md) |  | [optional] 
**port** | **int** | Validation check if the port is passed in. | [optional] 
**type** | [**OSAppletEnum**](OSAppletEnum.md) |  | 
**handler** | [**AppletServingHandlerType**](AppletServingHandlerType.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.terminating_os_server_applet import TerminatingOSServerApplet

# TODO update the JSON string below
json = "{}"
# create an instance of TerminatingOSServerApplet from a JSON string
terminating_os_server_applet_instance = TerminatingOSServerApplet.from_json(json)
# print the JSON string representation of the object
print TerminatingOSServerApplet.to_json()

# convert the object into a dict
terminating_os_server_applet_dict = terminating_os_server_applet_instance.to_dict()
# create an instance of TerminatingOSServerApplet from a dict
terminating_os_server_applet_from_dict = TerminatingOSServerApplet.from_dict(terminating_os_server_applet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


