# ConversationsCreateFromWorkstreamSummaryOutput

This is the model for the output for the \"/conversations/create/from_workstream_summary/{workstream_summary}\" endpoints.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**conversation** | [**ReferencedConversation**](ReferencedConversation.md) |  | 

## Example

```python
from pieces_os_client.models.conversations_create_from_workstream_summary_output import ConversationsCreateFromWorkstreamSummaryOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationsCreateFromWorkstreamSummaryOutput from a JSON string
conversations_create_from_workstream_summary_output_instance = ConversationsCreateFromWorkstreamSummaryOutput.from_json(json)
# print the JSON string representation of the object
print ConversationsCreateFromWorkstreamSummaryOutput.to_json()

# convert the object into a dict
conversations_create_from_workstream_summary_output_dict = conversations_create_from_workstream_summary_output_instance.to_dict()
# create an instance of ConversationsCreateFromWorkstreamSummaryOutput from a dict
conversations_create_from_workstream_summary_output_from_dict = ConversationsCreateFromWorkstreamSummaryOutput.from_dict(conversations_create_from_workstream_summary_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


