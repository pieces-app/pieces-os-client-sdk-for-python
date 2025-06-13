# TrackedConversationMessageSentimentMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**message** | **str** |  | [optional] 
**sentiment** | [**ConversationMessageSentimentEnum**](ConversationMessageSentimentEnum.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.tracked_conversation_message_sentiment_metadata import TrackedConversationMessageSentimentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedConversationMessageSentimentMetadata from a JSON string
tracked_conversation_message_sentiment_metadata_instance = TrackedConversationMessageSentimentMetadata.from_json(json)
# print the JSON string representation of the object
print TrackedConversationMessageSentimentMetadata.to_json()

# convert the object into a dict
tracked_conversation_message_sentiment_metadata_dict = tracked_conversation_message_sentiment_metadata_instance.to_dict()
# create an instance of TrackedConversationMessageSentimentMetadata from a dict
tracked_conversation_message_sentiment_metadata_from_dict = TrackedConversationMessageSentimentMetadata.from_dict(tracked_conversation_message_sentiment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


