# Conversations

This is a plural version of a Conversation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[Conversation]**](Conversation.md) |  | 
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an Conversation id. | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from openapi_client.models.conversations import Conversations

# TODO update the JSON string below
json = "{}"
# create an instance of Conversations from a JSON string
conversations_instance = Conversations.from_json(json)
# print the JSON string representation of the object
print Conversations.to_json()

# convert the object into a dict
conversations_dict = conversations_instance.to_dict()
# create an instance of Conversations from a dict
conversations_form_dict = conversations.from_dict(conversations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


