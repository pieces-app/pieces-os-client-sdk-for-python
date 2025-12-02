# DeepResearchStreamInput

This is the input for the /deep_research/stream endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | **str** | This is the ID of a predefined persisted conversation, if this is not present we will create a new conversation for the input/output.(in the case of a question) | [optional] 
**question** | [**QGPTQuestionInput**](QGPTQuestionInput.md) |  | [optional] 
**relevance** | [**QGPTRelevanceInput**](QGPTRelevanceInput.md) |  | [optional] 
**request** | **str** | This is an optional Id you can use to identify the result from your request. | [optional] 
**reset** | **bool** | This will fully reset all current Activity within the Deep Research stream Flows. | [optional] 
**stop** | **bool** | This will stop the output of the current LLM | [optional] 

## Example

```python
from pieces_os_client.models.deep_research_stream_input import DeepResearchStreamInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeepResearchStreamInput from a JSON string
deep_research_stream_input_instance = DeepResearchStreamInput.from_json(json)
# print the JSON string representation of the object
print(DeepResearchStreamInput.to_json())

# convert the object into a dict
deep_research_stream_input_dict = deep_research_stream_input_instance.to_dict()
# create an instance of DeepResearchStreamInput from a dict
deep_research_stream_input_from_dict = DeepResearchStreamInput.from_dict(deep_research_stream_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


