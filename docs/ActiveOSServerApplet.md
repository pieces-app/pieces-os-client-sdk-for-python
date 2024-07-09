# ActiveOSServerApplet

TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**port** | **int** |  | 
**type** | [**OSAppletEnum**](OSAppletEnum.md) |  | 

## Example

```python
from pieces_os_client.models.active_os_server_applet import ActiveOSServerApplet

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveOSServerApplet from a JSON string
active_os_server_applet_instance = ActiveOSServerApplet.from_json(json)
# print the JSON string representation of the object
print ActiveOSServerApplet.to_json()

# convert the object into a dict
active_os_server_applet_dict = active_os_server_applet_instance.to_dict()
# create an instance of ActiveOSServerApplet from a dict
active_os_server_applet_from_dict = ActiveOSServerApplet.from_dict(active_os_server_applet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


