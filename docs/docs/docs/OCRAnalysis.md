# OCRAnalysis

This is the data collected during the ocr analysis of an image.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | 
**raw** | [**Format**](Format.md) |  | 
**hocr** | [**Format**](Format.md) |  | 
**image** | **str** | this is a reference the the imageAnalysis. | 
**model** | [**Model**](Model.md) |  | 

## Example

```python
from openapi_client.models.ocr_analysis import OCRAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of OCRAnalysis from a JSON string
ocr_analysis_instance = OCRAnalysis.from_json(json)
# print the JSON string representation of the object
print OCRAnalysis.to_json()

# convert the object into a dict
ocr_analysis_dict = ocr_analysis_instance.to_dict()
# create an instance of OCRAnalysis from a dict
ocr_analysis_form_dict = ocr_analysis.from_dict(ocr_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


