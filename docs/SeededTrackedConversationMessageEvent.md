# SeededTrackedConversationMessageEvent

This is a pre-created(seed) TrackedConversationMessageEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**identifier_description_pair** | [**TrackedConversationMessageEventIdentifierDescriptionPairs**](TrackedConversationMessageEventIdentifierDescriptionPairs.md) |  | 
**message** | [**ReferencedConversationMessage**](ReferencedConversationMessage.md) |  | 
**metadata** | [**TrackedConversationMessageEventMetadata**](TrackedConversationMessageEventMetadata.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_tracked_conversation_message_event import SeededTrackedConversationMessageEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SeededTrackedConversationMessageEvent from a JSON string
seeded_tracked_conversation_message_event_instance = SeededTrackedConversationMessageEvent.from_json(json)
# print the JSON string representation of the object
print SeededTrackedConversationMessageEvent.to_json()

# convert the object into a dict
seeded_tracked_conversation_message_event_dict = seeded_tracked_conversation_message_event_instance.to_dict()
# create an instance of SeededTrackedConversationMessageEvent from a dict
seeded_tracked_conversation_message_event_from_dict = SeededTrackedConversationMessageEvent.from_dict(seeded_tracked_conversation_message_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


