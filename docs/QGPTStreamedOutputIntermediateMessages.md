# QGPTStreamedOutputIntermediateMessages

This is the intermediate messages that were sent from the LLM.  messages: is list of the TOTAL messages that were sent from the LLM to us, or can also be used as message like 'search for relevant files'... xyz, ie, both messages from the LLM but also from context ingestion This is a continous list of intermediate messages(ie from the 1st message to the last message)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.qgpt_streamed_output_intermediate_messages import QGPTStreamedOutputIntermediateMessages

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTStreamedOutputIntermediateMessages from a JSON string
qgpt_streamed_output_intermediate_messages_instance = QGPTStreamedOutputIntermediateMessages.from_json(json)
# print the JSON string representation of the object
print(QGPTStreamedOutputIntermediateMessages.to_json())

# convert the object into a dict
qgpt_streamed_output_intermediate_messages_dict = qgpt_streamed_output_intermediate_messages_instance.to_dict()
# create an instance of QGPTStreamedOutputIntermediateMessages from a dict
qgpt_streamed_output_intermediate_messages_from_dict = QGPTStreamedOutputIntermediateMessages.from_dict(qgpt_streamed_output_intermediate_messages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


