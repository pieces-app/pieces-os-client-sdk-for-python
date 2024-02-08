# ConversationSummarizeOutput

This is the output model for \"/conversation/{conversation}/summarize

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**conversation** | [**ReferencedConversation**](ReferencedConversation.md) |  | 
**annotation** | [**ReferencedAnnotation**](ReferencedAnnotation.md) |  | 

## Example

```python
from openapi_client.models.conversation_summarize_output import ConversationSummarizeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationSummarizeOutput from a JSON string
conversation_summarize_output_instance = ConversationSummarizeOutput.from_json(json)
# print the JSON string representation of the object
print ConversationSummarizeOutput.to_json()

# convert the object into a dict
conversation_summarize_output_dict = conversation_summarize_output_instance.to_dict()
# create an instance of ConversationSummarizeOutput from a dict
conversation_summarize_output_form_dict = conversation_summarize_output.from_dict(conversation_summarize_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


