# QGPTQuestionInput

This is the body input for the /code_gpt/question.  Note: - each relevant seed, must require at minimum a Seed or an id used from the /code_gpt/relevance endpoint or we will throw an error.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | optional application id | [optional] 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**model** | **str** | optional model id | [optional] 
**pipeline** | [**QGPTPromptPipeline**](QGPTPromptPipeline.md) |  | [optional] 
**query** | **str** | This is the user asked question. | 
**relevant** | [**RelevantQGPTSeeds**](RelevantQGPTSeeds.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**temporal** | [**TemporalRangeGrounding**](TemporalRangeGrounding.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.qgpt_question_input import QGPTQuestionInput

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTQuestionInput from a JSON string
qgpt_question_input_instance = QGPTQuestionInput.from_json(json)
# print the JSON string representation of the object
print QGPTQuestionInput.to_json()

# convert the object into a dict
qgpt_question_input_dict = qgpt_question_input_instance.to_dict()
# create an instance of QGPTQuestionInput from a dict
qgpt_question_input_from_dict = QGPTQuestionInput.from_dict(qgpt_question_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


