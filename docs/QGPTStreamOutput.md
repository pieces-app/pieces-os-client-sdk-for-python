# QGPTStreamOutput

This is the out for the /qgpt/stream endpoint.  200: success 401: invalid authentication/api key 429: Rate limit/Quota exceeded 500: server had an error 503: the engine is currently overloaded

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_routes** | [**QGPTAgentRoutes**](QGPTAgentRoutes.md) |  | [optional] 
**conversation** | **str** | This is the ID of a predefined persisted conversation, if this is not present we will create a new conversation for the input/output.(in the case of a question) | 
**error_message** | **str** | optional error message is the status code is NOT 200 | [optional] 
**extracted** | [**QGPTStreamedOutputExtractedMaterials**](QGPTStreamedOutputExtractedMaterials.md) |  | [optional] 
**intermediate_messages** | [**QGPTStreamedOutputIntermediateMessages**](QGPTStreamedOutputIntermediateMessages.md) |  | [optional] 
**migration** | [**MigrationProgress**](MigrationProgress.md) |  | [optional] 
**prompt_context_materials** | [**QGPTStreamedOutputPromptContextMaterials**](QGPTStreamedOutputPromptContextMaterials.md) |  | [optional] 
**question** | [**QGPTQuestionOutput**](QGPTQuestionOutput.md) |  | [optional] 
**relevance** | [**QGPTRelevanceOutput**](QGPTRelevanceOutput.md) |  | [optional] 
**request** | **str** | This is the id used to represent the stream of response. this will always be present. We will use the value passed inby the client, or we will generate one. | [optional] 
**status** | [**QGPTStreamEnum**](QGPTStreamEnum.md) |  | [optional] 
**status_code** | **float** | This will be provided | [optional] 

## Example

```python
from pieces_os_client.models.qgpt_stream_output import QGPTStreamOutput

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTStreamOutput from a JSON string
qgpt_stream_output_instance = QGPTStreamOutput.from_json(json)
# print the JSON string representation of the object
print(QGPTStreamOutput.to_json())

# convert the object into a dict
qgpt_stream_output_dict = qgpt_stream_output_instance.to_dict()
# create an instance of QGPTStreamOutput from a dict
qgpt_stream_output_from_dict = QGPTStreamOutput.from_dict(qgpt_stream_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


