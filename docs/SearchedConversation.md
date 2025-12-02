# SearchedConversation

This is used for the Conversations searching endpoint.  conversation here is only provided if transferables are set to true.  temporal: if this is provided this means that their material matched the input via a timestamp.  TODO will want to consider returning related materials to this material potentially both associated/ and not associated materials ie suggestion: WorkstreamSuggestions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**SearchedAnnotations**](SearchedAnnotations.md) |  | [optional] 
**conversation** | [**Conversation**](Conversation.md) |  | [optional] 
**exact** | **bool** |  | 
**identifier** | **str** | This is the uuid of the conversation. | 
**messages** | [**SearchedConversationMessages**](SearchedConversationMessages.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**similarity** | **float** |  | 
**temporal** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_conversation import SearchedConversation

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedConversation from a JSON string
searched_conversation_instance = SearchedConversation.from_json(json)
# print the JSON string representation of the object
print(SearchedConversation.to_json())

# convert the object into a dict
searched_conversation_dict = searched_conversation_instance.to_dict()
# create an instance of SearchedConversation from a dict
searched_conversation_from_dict = SearchedConversation.from_dict(searched_conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


