# TrackedConversationMessageEventIdentifierDescriptionPairs

These are all of the available event types that are permitted in an object pair notation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**message_created** | **str** | The key value pair for an message being created. | [optional] [default to 'UNKNOWN']

## Example

```python
from pieces_os_client.models.tracked_conversation_message_event_identifier_description_pairs import TrackedConversationMessageEventIdentifierDescriptionPairs

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedConversationMessageEventIdentifierDescriptionPairs from a JSON string
tracked_conversation_message_event_identifier_description_pairs_instance = TrackedConversationMessageEventIdentifierDescriptionPairs.from_json(json)
# print the JSON string representation of the object
print TrackedConversationMessageEventIdentifierDescriptionPairs.to_json()

# convert the object into a dict
tracked_conversation_message_event_identifier_description_pairs_dict = tracked_conversation_message_event_identifier_description_pairs_instance.to_dict()
# create an instance of TrackedConversationMessageEventIdentifierDescriptionPairs from a dict
tracked_conversation_message_event_identifier_description_pairs_from_dict = TrackedConversationMessageEventIdentifierDescriptionPairs.from_dict(tracked_conversation_message_event_identifier_description_pairs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


