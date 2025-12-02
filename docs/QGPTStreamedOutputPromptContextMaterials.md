# QGPTStreamedOutputPromptContextMaterials

The prompt context materials are the materials that were used to generate the response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**summaries** | [**List[QGPTStreamedOutputPromptContextMaterial]**](QGPTStreamedOutputPromptContextMaterial.md) |  | [optional] 
**workstream_events** | [**List[QGPTStreamedOutputPromptContextMaterial]**](QGPTStreamedOutputPromptContextMaterial.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.qgpt_streamed_output_prompt_context_materials import QGPTStreamedOutputPromptContextMaterials

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTStreamedOutputPromptContextMaterials from a JSON string
qgpt_streamed_output_prompt_context_materials_instance = QGPTStreamedOutputPromptContextMaterials.from_json(json)
# print the JSON string representation of the object
print(QGPTStreamedOutputPromptContextMaterials.to_json())

# convert the object into a dict
qgpt_streamed_output_prompt_context_materials_dict = qgpt_streamed_output_prompt_context_materials_instance.to_dict()
# create an instance of QGPTStreamedOutputPromptContextMaterials from a dict
qgpt_streamed_output_prompt_context_materials_from_dict = QGPTStreamedOutputPromptContextMaterials.from_dict(qgpt_streamed_output_prompt_context_materials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


