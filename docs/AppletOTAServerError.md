# AppletOTAServerError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.applet_ota_server_error import AppletOTAServerError

# TODO update the JSON string below
json = "{}"
# create an instance of AppletOTAServerError from a JSON string
applet_ota_server_error_instance = AppletOTAServerError.from_json(json)
# print the JSON string representation of the object
print(AppletOTAServerError.to_json())

# convert the object into a dict
applet_ota_server_error_dict = applet_ota_server_error_instance.to_dict()
# create an instance of AppletOTAServerError from a dict
applet_ota_server_error_from_dict = AppletOTAServerError.from_dict(applet_ota_server_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


