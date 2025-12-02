# FlattenedConversationMessage

This is a flattened DAG safe version of a ConversationMessage.  summaryRoot: one-to-one relationship to the summary created from this message. This allows us to know which summary was created by this message.  agent_id: this is an identifier that will let use know what thinking message came from what agent            specifically within the DEEP_STUDY flow.

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
from pieces_os_client.models.flattened_conversation_message import FlattenedConversationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedConversationMessage from a JSON string
flattened_conversation_message_instance = FlattenedConversationMessage.from_json(json)
# print the JSON string representation of the object
print(FlattenedConversationMessage.to_json())

# convert the object into a dict
flattened_conversation_message_dict = flattened_conversation_message_instance.to_dict()
# create an instance of FlattenedConversationMessage from a dict
flattened_conversation_message_from_dict = FlattenedConversationMessage.from_dict(flattened_conversation_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


