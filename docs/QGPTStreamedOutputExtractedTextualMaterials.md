# QGPTStreamedOutputExtractedTextualMaterials

This is all the textually extracted materials from the QGPT stream

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**message** | [**TextuallyExtractedMaterials**](TextuallyExtractedMaterials.md) |  | [optional] 
**workstream** | [**TextuallyExtractedMaterials**](TextuallyExtractedMaterials.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.qgpt_streamed_output_extracted_textual_materials import QGPTStreamedOutputExtractedTextualMaterials

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTStreamedOutputExtractedTextualMaterials from a JSON string
qgpt_streamed_output_extracted_textual_materials_instance = QGPTStreamedOutputExtractedTextualMaterials.from_json(json)
# print the JSON string representation of the object
print QGPTStreamedOutputExtractedTextualMaterials.to_json()

# convert the object into a dict
qgpt_streamed_output_extracted_textual_materials_dict = qgpt_streamed_output_extracted_textual_materials_instance.to_dict()
# create an instance of QGPTStreamedOutputExtractedTextualMaterials from a dict
qgpt_streamed_output_extracted_textual_materials_from_dict = QGPTStreamedOutputExtractedTextualMaterials.from_dict(qgpt_streamed_output_extracted_textual_materials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


