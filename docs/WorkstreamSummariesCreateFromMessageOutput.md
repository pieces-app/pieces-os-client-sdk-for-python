# WorkstreamSummariesCreateFromMessageOutput

Output model for creating a workstream summary from a conversation message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_message** | [**ReferencedConversationMessage**](ReferencedConversationMessage.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**workstream_summary** | [**ReferencedWorkstreamSummary**](ReferencedWorkstreamSummary.md) |  | 

## Example

```python
from pieces_os_client.models.workstream_summaries_create_from_message_output import WorkstreamSummariesCreateFromMessageOutput

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSummariesCreateFromMessageOutput from a JSON string
workstream_summaries_create_from_message_output_instance = WorkstreamSummariesCreateFromMessageOutput.from_json(json)
# print the JSON string representation of the object
print(WorkstreamSummariesCreateFromMessageOutput.to_json())

# convert the object into a dict
workstream_summaries_create_from_message_output_dict = workstream_summaries_create_from_message_output_instance.to_dict()
# create an instance of WorkstreamSummariesCreateFromMessageOutput from a dict
workstream_summaries_create_from_message_output_from_dict = WorkstreamSummariesCreateFromMessageOutput.from_dict(workstream_summaries_create_from_message_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


