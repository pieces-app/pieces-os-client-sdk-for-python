# QGPTTaskPipeline

This model is specifically for QGPT Task pipelines, the model is used to group one off tasks for instance fix/explaining/commenting that dont necessarily require a conversation form factor.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**code_explanation** | [**QGPTTaskPipelineForCodeExplanation**](QGPTTaskPipelineForCodeExplanation.md) |  | [optional] 
**code_commentation** | [**QGPTTaskPipelineForCodeCommentation**](QGPTTaskPipelineForCodeCommentation.md) |  | [optional] 
**code_fix** | [**QGPTTaskPipelineForCodeFix**](QGPTTaskPipelineForCodeFix.md) |  | [optional] 
**code_modification** | [**QGPTTaskPipelineForCodeModification**](QGPTTaskPipelineForCodeModification.md) |  | [optional] 
**code_completion** | [**QGPTTaskPipelineForCodeCompletion**](QGPTTaskPipelineForCodeCompletion.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.qgpt_task_pipeline import QGPTTaskPipeline

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTTaskPipeline from a JSON string
qgpt_task_pipeline_instance = QGPTTaskPipeline.from_json(json)
# print the JSON string representation of the object
print QGPTTaskPipeline.to_json()

# convert the object into a dict
qgpt_task_pipeline_dict = qgpt_task_pipeline_instance.to_dict()
# create an instance of QGPTTaskPipeline from a dict
qgpt_task_pipeline_from_dict = QGPTTaskPipeline.from_dict(qgpt_task_pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


