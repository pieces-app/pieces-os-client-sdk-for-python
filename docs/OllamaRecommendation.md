# OllamaRecommendation

This is a model that will let the products know some of our recommendations around Ollama:  for now: will just add a recommendation if the user should even use Ollama or NOT. -- (inference)  inference: IE if we want to recommendation the user to use inference (ie call the model) or not

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inference** | **bool** | This is a bool that will let the client know if we recommend to use ollama for inference or not | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.ollama_recommendation import OllamaRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of OllamaRecommendation from a JSON string
ollama_recommendation_instance = OllamaRecommendation.from_json(json)
# print the JSON string representation of the object
print(OllamaRecommendation.to_json())

# convert the object into a dict
ollama_recommendation_dict = ollama_recommendation_instance.to_dict()
# create an instance of OllamaRecommendation from a dict
ollama_recommendation_from_dict = OllamaRecommendation.from_dict(ollama_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


