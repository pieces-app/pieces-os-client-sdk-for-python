# ReferencedConversationMessage

This is a DAG-Safe Minimal version of a ConversationMessage.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | 
**reference** | [**FlattenedConversationMessage**](FlattenedConversationMessage.md) |  | [optional] 

## Example

```python
from openapi_client.models.referenced_conversation_message import ReferencedConversationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedConversationMessage from a JSON string
referenced_conversation_message_instance = ReferencedConversationMessage.from_json(json)
# print the JSON string representation of the object
print ReferencedConversationMessage.to_json()

# convert the object into a dict
referenced_conversation_message_dict = referenced_conversation_message_instance.to_dict()
# create an instance of ReferencedConversationMessage from a dict
referenced_conversation_message_form_dict = referenced_conversation_message.from_dict(referenced_conversation_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


