# QGPTConversationPipeline

This model is specifically for QGPT Conversation pipelines, the model is used to group conversational prompts for instance a conversation around generating code.  here are some use cases- 1. contextualized_code_generation- This is for users that want to have conversations around generating code, when there is provided context. 2. generalized_code- This is for users that want to have conversations without context around code. 3. contextualized_code- This is for users that want to have conversation around code with Context. 4. contextualized_code_workstream: this is for the users that want to use context as well as WPE information in their chat (we wiil prioritize WPE infomration, but also support other info as well)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**contextualized_code_generation** | [**QGPTConversationPipelineForContextualizedCodeGeneration**](QGPTConversationPipelineForContextualizedCodeGeneration.md) |  | [optional] 
**generalized_code_dialog** | [**QGPTConversationPipelineForGeneralizedCodeDialog**](QGPTConversationPipelineForGeneralizedCodeDialog.md) |  | [optional] 
**contextualized_code_dialog** | [**QGPTConversationPipelineForContextualizedCodeDialog**](QGPTConversationPipelineForContextualizedCodeDialog.md) |  | [optional] 
**contextualized_code_workstream_dialog** | [**QGPTConversationPipelineForContextualizedCodeWorkstreamDialog**](QGPTConversationPipelineForContextualizedCodeWorkstreamDialog.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.qgpt_conversation_pipeline import QGPTConversationPipeline

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTConversationPipeline from a JSON string
qgpt_conversation_pipeline_instance = QGPTConversationPipeline.from_json(json)
# print the JSON string representation of the object
print QGPTConversationPipeline.to_json()

# convert the object into a dict
qgpt_conversation_pipeline_dict = qgpt_conversation_pipeline_instance.to_dict()
# create an instance of QGPTConversationPipeline from a dict
qgpt_conversation_pipeline_from_dict = QGPTConversationPipeline.from_dict(qgpt_conversation_pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


