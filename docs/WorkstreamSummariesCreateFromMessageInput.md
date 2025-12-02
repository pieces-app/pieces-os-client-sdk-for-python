# WorkstreamSummariesCreateFromMessageInput

Input model for creating a workstream summary from a conversation message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_message** | [**ReferencedConversationMessage**](ReferencedConversationMessage.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_summaries_create_from_message_input import WorkstreamSummariesCreateFromMessageInput

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSummariesCreateFromMessageInput from a JSON string
workstream_summaries_create_from_message_input_instance = WorkstreamSummariesCreateFromMessageInput.from_json(json)
# print the JSON string representation of the object
print(WorkstreamSummariesCreateFromMessageInput.to_json())

# convert the object into a dict
workstream_summaries_create_from_message_input_dict = workstream_summaries_create_from_message_input_instance.to_dict()
# create an instance of WorkstreamSummariesCreateFromMessageInput from a dict
workstream_summaries_create_from_message_input_from_dict = WorkstreamSummariesCreateFromMessageInput.from_dict(workstream_summaries_create_from_message_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


