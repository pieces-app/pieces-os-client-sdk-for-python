# QGPTRepromptInput

Query is your followup question.  Conversation is a list of the back and fourth with the qgpt bot. where the first entry in the array was the last message sent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | optional application id | [optional] 
**conversation** | [**QGPTConversation**](QGPTConversation.md) |  | 
**model** | **str** | optional model id | [optional] 
**pipeline** | [**QGPTPromptPipeline**](QGPTPromptPipeline.md) |  | [optional] 
**query** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.qgpt_reprompt_input import QGPTRepromptInput

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTRepromptInput from a JSON string
qgpt_reprompt_input_instance = QGPTRepromptInput.from_json(json)
# print the JSON string representation of the object
print QGPTRepromptInput.to_json()

# convert the object into a dict
qgpt_reprompt_input_dict = qgpt_reprompt_input_instance.to_dict()
# create an instance of QGPTRepromptInput from a dict
qgpt_reprompt_input_from_dict = QGPTRepromptInput.from_dict(qgpt_reprompt_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


