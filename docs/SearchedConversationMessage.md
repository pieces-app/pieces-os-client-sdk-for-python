# SearchedConversationMessage

This is used for the ConversationMessages searching endpoint && the specific Conversation search && ConversationsSearch  conversation here is only provided if transferables are set to true.  temporal: if this is provided this means that their material matched the input via a timestamp.  TODO will want to consider returning related materials to this material potentially both associated/ and not associated materials ie suggestion: WorkstreamSuggestions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exact** | **bool** |  | 
**identifier** | **str** | This is the uuid of the ConversationMessage. | 
**message** | [**ConversationMessage**](ConversationMessage.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**similarity** | **float** |  | 
**temporal** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_conversation_message import SearchedConversationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedConversationMessage from a JSON string
searched_conversation_message_instance = SearchedConversationMessage.from_json(json)
# print the JSON string representation of the object
print(SearchedConversationMessage.to_json())

# convert the object into a dict
searched_conversation_message_dict = searched_conversation_message_instance.to_dict()
# create an instance of SearchedConversationMessage from a dict
searched_conversation_message_from_dict = SearchedConversationMessage.from_dict(searched_conversation_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


