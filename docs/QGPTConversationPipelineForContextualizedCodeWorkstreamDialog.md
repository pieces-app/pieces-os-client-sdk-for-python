# QGPTConversationPipelineForContextualizedCodeWorkstreamDialog

This is for the users that wants to have contextualized code conversations around their workstream materials, meaning conversations around code with Context provided, as well as workstream information ie information gathered from the WPE.  This is a class so that we can add optional properties in the future.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.qgpt_conversation_pipeline_for_contextualized_code_workstream_dialog import QGPTConversationPipelineForContextualizedCodeWorkstreamDialog

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTConversationPipelineForContextualizedCodeWorkstreamDialog from a JSON string
qgpt_conversation_pipeline_for_contextualized_code_workstream_dialog_instance = QGPTConversationPipelineForContextualizedCodeWorkstreamDialog.from_json(json)
# print the JSON string representation of the object
print QGPTConversationPipelineForContextualizedCodeWorkstreamDialog.to_json()

# convert the object into a dict
qgpt_conversation_pipeline_for_contextualized_code_workstream_dialog_dict = qgpt_conversation_pipeline_for_contextualized_code_workstream_dialog_instance.to_dict()
# create an instance of QGPTConversationPipelineForContextualizedCodeWorkstreamDialog from a dict
qgpt_conversation_pipeline_for_contextualized_code_workstream_dialog_from_dict = QGPTConversationPipelineForContextualizedCodeWorkstreamDialog.from_dict(qgpt_conversation_pipeline_for_contextualized_code_workstream_dialog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


