# NativeAccessibility

This is a specific model to encapsulate NativeAccessibility data from the LTM(used within the WorkstreamEvent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**accessibility_text** | **str** | The accessibility text extracted. | 
**app_title** | **str** | The title of the application. | 
**window_title** | **str** | The title of the window. | 
**browser_url** | **str** | The URL of the browser. | [optional] 
**is_merged** | **bool** | Indicates whether the workflow mapping is merged. | 
**is_cached** | **bool** | Indicates whether the workflow mapping is cached. | 

## Example

```python
from pieces_os_client.models.native_accessibility import NativeAccessibility

# TODO update the JSON string below
json = "{}"
# create an instance of NativeAccessibility from a JSON string
native_accessibility_instance = NativeAccessibility.from_json(json)
# print the JSON string representation of the object
print NativeAccessibility.to_json()

# convert the object into a dict
native_accessibility_dict = native_accessibility_instance.to_dict()
# create an instance of NativeAccessibility from a dict
native_accessibility_from_dict = NativeAccessibility.from_dict(native_accessibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


