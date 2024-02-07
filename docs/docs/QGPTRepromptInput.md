# QGPTRepromptInput

Query is your followup question.  Conversation is a list of the back and fourth with the qgpt bot. where the first entry in the array was the last message sent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**query** | **str** |  | 
**conversation** | [**QGPTConversation**](QGPTConversation.md) |  | 
**application** | **str** | optional application id | [optional] 
**model** | **str** | optional model id | [optional] 

## Example

```python
from openapi_client.models.qgpt_reprompt_input import QGPTRepromptInput

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTRepromptInput from a JSON string
qgpt_reprompt_input_instance = QGPTRepromptInput.from_json(json)
# print the JSON string representation of the object
print QGPTRepromptInput.to_json()

# convert the object into a dict
qgpt_reprompt_input_dict = qgpt_reprompt_input_instance.to_dict()
# create an instance of QGPTRepromptInput from a dict
qgpt_reprompt_input_form_dict = qgpt_reprompt_input.from_dict(qgpt_reprompt_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


