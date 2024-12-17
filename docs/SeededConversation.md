# SeededConversation

This is a pre-Conversation object.  This will hold together a conversation. Ie allthe message within a conversation.  All the additional properties on here used on here like(anchors/assets) are used for context that will seed the conversation.  model is a calculated property, and will be the model of the last message sent if applicable.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchors** | [**List[SeededAnchor]**](SeededAnchor.md) |  | [optional] 
**annotations** | [**List[SeededAnnotation]**](SeededAnnotation.md) |  | [optional] 
**application** | [**Application**](Application.md) |  | [optional] 
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**demo** | **bool** | This will let us know if this conversation was generated as a &#39;demo&#39; conversation | [optional] 
**favorited** | **bool** |  | [optional] 
**messages** | [**List[SeededConversationMessage]**](SeededConversationMessage.md) |  | [optional] 
**model** | [**ReferencedModel**](ReferencedModel.md) |  | [optional] 
**name** | **str** | This is a name that is customized. | [optional] 
**pipeline** | [**QGPTPromptPipeline**](QGPTPromptPipeline.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**type** | [**ConversationTypeEnum**](ConversationTypeEnum.md) |  | 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_conversation import SeededConversation

# TODO update the JSON string below
json = "{}"
# create an instance of SeededConversation from a JSON string
seeded_conversation_instance = SeededConversation.from_json(json)
# print the JSON string representation of the object
print SeededConversation.to_json()

# convert the object into a dict
seeded_conversation_dict = seeded_conversation_instance.to_dict()
# create an instance of SeededConversation from a dict
seeded_conversation_from_dict = SeededConversation.from_dict(seeded_conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


