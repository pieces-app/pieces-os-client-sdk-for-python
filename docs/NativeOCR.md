# NativeOCR

This is a specific model to encapsulate nativeOCR(previously named WorkflowMapping) data from the LTM(used within the WorkstreamEvent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_title** | **str** | The title of the application. | 
**browser_url** | **str** | The URL of the browser. | [optional] 
**embedding_model_unique_name** | **str** | Optional unique name for the embedding model. | [optional] 
**is_cached** | **bool** | Indicates whether the workflow mapping is cached. &#x60;cached&#x60; means that it has been used as context either in a conversation or in a summary, xyz | 
**is_merged** | **bool** | Indicates whether the workflow mapping is merged. | 
**ocr_text** | **str** | The OCR text extracted. | 
**ocr_text_hash** | **str** | The hash of the OCR text. | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**window_title** | **str** | The title of the window. | 

## Example

```python
from pieces_os_client.models.native_ocr import NativeOCR

# TODO update the JSON string below
json = "{}"
# create an instance of NativeOCR from a JSON string
native_ocr_instance = NativeOCR.from_json(json)
# print the JSON string representation of the object
print(NativeOCR.to_json())

# convert the object into a dict
native_ocr_dict = native_ocr_instance.to_dict()
# create an instance of NativeOCR from a dict
native_ocr_from_dict = NativeOCR.from_dict(native_ocr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


