# NativeClipboardContent

This is an object used specifically for the NativeClipboard object that is used on a WorkstreamEvent  NOTE: at least one of these fields must be present.  TODO:(future support) we do have support for files, but these are file paths, the reason for holding on this is so we can discuss the format here and funcky edge cases(moved, deleted or if we do not care.) TODO:(future support) we do have support for images, but we will hold off for now because 1 we are not ready for it, and 2 because we might want to have a specific value for this ie the NativeOCR format nested within the NativeClipboard)  NOTE: (if html: we will provide the html format, + the raw plain text) NOTE: (if RTF: we will provide the RTF format, + the plain text)  TODO: @mark-at-pieces @rob-at-pieces @tsavo-at-pieces confirm structure of this model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | **str** | this should get trigger when I copy &#x60;html&#x60; which could still be plan text or if we copy raw html from inspecting an &#x60;html&#x60; page | [optional] 
**rtf** | **str** | rich-text-format, ie colored text generally copied from an ide | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**text** | **str** | this is just generally any plain text that is not classified as &#x60;html&#x60; | [optional] 

## Example

```python
from pieces_os_client.models.native_clipboard_content import NativeClipboardContent

# TODO update the JSON string below
json = "{}"
# create an instance of NativeClipboardContent from a JSON string
native_clipboard_content_instance = NativeClipboardContent.from_json(json)
# print the JSON string representation of the object
print(NativeClipboardContent.to_json())

# convert the object into a dict
native_clipboard_content_dict = native_clipboard_content_instance.to_dict()
# create an instance of NativeClipboardContent from a dict
native_clipboard_content_from_dict = NativeClipboardContent.from_dict(native_clipboard_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


