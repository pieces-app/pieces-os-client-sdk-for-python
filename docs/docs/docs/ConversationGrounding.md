# ConversationGrounding

This is the context used for grounding the ml models with reguard to a conversation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 

## Example

```python
from openapi_client.models.conversation_grounding import ConversationGrounding

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationGrounding from a JSON string
conversation_grounding_instance = ConversationGrounding.from_json(json)
# print the JSON string representation of the object
print ConversationGrounding.to_json()

# convert the object into a dict
conversation_grounding_dict = conversation_grounding_instance.to_dict()
# create an instance of ConversationGrounding from a dict
conversation_grounding_form_dict = conversation_grounding.from_dict(conversation_grounding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


