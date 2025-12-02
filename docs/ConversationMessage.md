# ConversationMessage

This is a fully referenced ConversationMessage.  This has the minimum amount of properties to keep this light weight  (will consider additional properties in the future like people/tags/links xyz)  summaryRoot: one-to-one relationship to the summary created from this message. This allows us to know which summary was created by this message.  agent_id: this is an identifier that will let use know what thinking message came from what agent            specifically within the DEEP_STUDY flow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | [**ConversationMessageAgent**](ConversationMessageAgent.md) |  | [optional] 
**anchors** | [**FlattenedAnchors**](FlattenedAnchors.md) |  | [optional] 
**annotations** | [**FlattenedAnnotations**](FlattenedAnnotations.md) |  | [optional] 
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**conversation** | [**ReferencedConversation**](ReferencedConversation.md) |  | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**fragment** | [**FragmentFormat**](FragmentFormat.md) |  | [optional] 
**id** | **str** |  | 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**model** | [**Model**](Model.md) |  | [optional] 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**ranges** | [**FlattenedRanges**](FlattenedRanges.md) |  | [optional] 
**role** | [**QGPTConversationMessageRoleEnum**](QGPTConversationMessageRoleEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**sentiment** | [**ConversationMessageSentimentEnum**](ConversationMessageSentimentEnum.md) |  | [optional] 
**sources** | [**FlattenedIdentifiedWorkstreamPatternEngineSources**](FlattenedIdentifiedWorkstreamPatternEngineSources.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**summary_root** | [**ReferencedWorkstreamSummary**](ReferencedWorkstreamSummary.md) |  | [optional] 
**tags** | [**FlattenedTags**](FlattenedTags.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 
**workstream_events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.conversation_message import ConversationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessage from a JSON string
conversation_message_instance = ConversationMessage.from_json(json)
# print the JSON string representation of the object
print(ConversationMessage.to_json())

# convert the object into a dict
conversation_message_dict = conversation_message_instance.to_dict()
# create an instance of ConversationMessage from a dict
conversation_message_from_dict = ConversationMessage.from_dict(conversation_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


