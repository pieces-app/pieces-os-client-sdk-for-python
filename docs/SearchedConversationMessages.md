# SearchedConversationMessages

This is the plural Model used to return many SearchedConversationMessage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[SearchedConversationMessage]**](SearchedConversationMessage.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_conversation_messages import SearchedConversationMessages

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedConversationMessages from a JSON string
searched_conversation_messages_instance = SearchedConversationMessages.from_json(json)
# print the JSON string representation of the object
print(SearchedConversationMessages.to_json())

# convert the object into a dict
searched_conversation_messages_dict = searched_conversation_messages_instance.to_dict()
# create an instance of SearchedConversationMessages from a dict
searched_conversation_messages_from_dict = SearchedConversationMessages.from_dict(searched_conversation_messages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


