# OSServerSettings

This is the model for the PiecesOS specific settings.  autoboot: refers to both the bootup of POS on the system login, default is false

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoboot** | **bool** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.os_server_settings import OSServerSettings

# TODO update the JSON string below
json = "{}"
# create an instance of OSServerSettings from a JSON string
os_server_settings_instance = OSServerSettings.from_json(json)
# print the JSON string representation of the object
print(OSServerSettings.to_json())

# convert the object into a dict
os_server_settings_dict = os_server_settings_instance.to_dict()
# create an instance of OSServerSettings from a dict
os_server_settings_from_dict = OSServerSettings.from_dict(os_server_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


