# QGPTStreamedOutputExtractedMaterials

This is used as an object that will return some of the extracted materials from both the message w/ compeleted/ or stopped  as well as the context(if using WorkstreamContext)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**textual** | [**QGPTStreamedOutputExtractedTextualMaterials**](QGPTStreamedOutputExtractedTextualMaterials.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.qgpt_streamed_output_extracted_materials import QGPTStreamedOutputExtractedMaterials

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTStreamedOutputExtractedMaterials from a JSON string
qgpt_streamed_output_extracted_materials_instance = QGPTStreamedOutputExtractedMaterials.from_json(json)
# print the JSON string representation of the object
print(QGPTStreamedOutputExtractedMaterials.to_json())

# convert the object into a dict
qgpt_streamed_output_extracted_materials_dict = qgpt_streamed_output_extracted_materials_instance.to_dict()
# create an instance of QGPTStreamedOutputExtractedMaterials from a dict
qgpt_streamed_output_extracted_materials_from_dict = QGPTStreamedOutputExtractedMaterials.from_dict(qgpt_streamed_output_extracted_materials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


