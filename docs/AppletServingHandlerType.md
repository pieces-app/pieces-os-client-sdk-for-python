# AppletServingHandlerType

A type representing a handler with optional folder/asset flags and a required key

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_folder** | **bool** | Indicates if the handler is for a folder (optional) | [optional] 
**is_asset** | **bool** | Indicates if the handler is for an asset (optional) | [optional] 
**version** | **str** | The version of the applet served by the handler | [optional] 
**type** | **str** | A required unique identifier for the handler | 

## Example

```python
from pieces_os_client.models.applet_serving_handler_type import AppletServingHandlerType

# TODO update the JSON string below
json = "{}"
# create an instance of AppletServingHandlerType from a JSON string
applet_serving_handler_type_instance = AppletServingHandlerType.from_json(json)
# print the JSON string representation of the object
print AppletServingHandlerType.to_json()

# convert the object into a dict
applet_serving_handler_type_dict = applet_serving_handler_type_instance.to_dict()
# create an instance of AppletServingHandlerType from a dict
applet_serving_handler_type_from_dict = AppletServingHandlerType.from_dict(applet_serving_handler_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


