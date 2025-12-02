# NativeClipboard

This is a specific model to encapsulate NativeClipboard, this is specifically used for the WorkstreamEventContext object.  note for our 'content' field of the native clipboard, we have text, html, rtf(rich-text-format), image, and files(will hold on this for now this is a list of file paths.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_title** | **str** | The title of the application. | [optional] 
**content** | [**NativeClipboardContent**](NativeClipboardContent.md) |  | 
**is_cached** | **bool** | Indicates whether the nativeClipbaord object is cached. &#x60;cached&#x60; means that it has been used as context either in a conversation or in a summary, xyz | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**window_title** | **str** | The title of the window. | [optional] 

## Example

```python
from pieces_os_client.models.native_clipboard import NativeClipboard

# TODO update the JSON string below
json = "{}"
# create an instance of NativeClipboard from a JSON string
native_clipboard_instance = NativeClipboard.from_json(json)
# print the JSON string representation of the object
print(NativeClipboard.to_json())

# convert the object into a dict
native_clipboard_dict = native_clipboard_instance.to_dict()
# create an instance of NativeClipboard from a dict
native_clipboard_from_dict = NativeClipboard.from_dict(native_clipboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


