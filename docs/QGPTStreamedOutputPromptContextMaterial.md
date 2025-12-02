# QGPTStreamedOutputPromptContextMaterial

The prompt context materials are the materials that were used to generate the response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | **float** |  | 

## Example

```python
from pieces_os_client.models.qgpt_streamed_output_prompt_context_material import QGPTStreamedOutputPromptContextMaterial

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTStreamedOutputPromptContextMaterial from a JSON string
qgpt_streamed_output_prompt_context_material_instance = QGPTStreamedOutputPromptContextMaterial.from_json(json)
# print the JSON string representation of the object
print(QGPTStreamedOutputPromptContextMaterial.to_json())

# convert the object into a dict
qgpt_streamed_output_prompt_context_material_dict = qgpt_streamed_output_prompt_context_material_instance.to_dict()
# create an instance of QGPTStreamedOutputPromptContextMaterial from a dict
qgpt_streamed_output_prompt_context_material_from_dict = QGPTStreamedOutputPromptContextMaterial.from_dict(qgpt_streamed_output_prompt_context_material_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


