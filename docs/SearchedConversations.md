# SearchedConversations

This is the plural Model used to return many SearchedConversation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[SearchedConversation]**](SearchedConversation.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_conversations import SearchedConversations

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedConversations from a JSON string
searched_conversations_instance = SearchedConversations.from_json(json)
# print the JSON string representation of the object
print SearchedConversations.to_json()

# convert the object into a dict
searched_conversations_dict = searched_conversations_instance.to_dict()
# create an instance of SearchedConversations from a dict
searched_conversations_from_dict = SearchedConversations.from_dict(searched_conversations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


