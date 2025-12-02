# SeededConversationMessage

This is a seeded version of a ConversationMessage.  conversation is optional, this is because it can be used within the SeededConversation, however if this is passed into the /messages/create w/o a conversation uuid then we will throw an error.  summaryRoot: one-to-one relationship to the summary created from this message. This allows us to know which summary was created by this message.  agent_id: this is an identifier that will let use know what thinking message came from what agent            specifically within the DEEP_STUDY flow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | [**ConversationMessageAgent**](ConversationMessageAgent.md) |  | [optional] 
**anchors** | [**FlattenedAnchors**](FlattenedAnchors.md) |  | [optional] 
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**conversation** | [**ReferencedConversation**](ReferencedConversation.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**fragment** | [**FragmentFormat**](FragmentFormat.md) |  | 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**model** | [**Model**](Model.md) |  | [optional] 
**ranges** | [**FlattenedRanges**](FlattenedRanges.md) |  | [optional] 
**role** | [**QGPTConversationMessageRoleEnum**](QGPTConversationMessageRoleEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**sentiment** | [**ConversationMessageSentimentEnum**](ConversationMessageSentimentEnum.md) |  | [optional] 
**sources** | [**FlattenedIdentifiedWorkstreamPatternEngineSources**](FlattenedIdentifiedWorkstreamPatternEngineSources.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**tags** | [**FlattenedTags**](FlattenedTags.md) |  | [optional] 
**workstream_events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_conversation_message import SeededConversationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SeededConversationMessage from a JSON string
seeded_conversation_message_instance = SeededConversationMessage.from_json(json)
# print the JSON string representation of the object
print(SeededConversationMessage.to_json())

# convert the object into a dict
seeded_conversation_message_dict = seeded_conversation_message_instance.to_dict()
# create an instance of SeededConversationMessage from a dict
seeded_conversation_message_from_dict = SeededConversationMessage.from_dict(seeded_conversation_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


