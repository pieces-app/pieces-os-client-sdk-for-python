# OllamaStatus

This will get used in the Websocket and in the get request for Ollama Note:  - updating (nullable) will be used in the case an update is underway  - installing (nullable) will be used in the case an installation is underway  - updateRequired (nullable) will be used in the case an update is required  - installation (nullable) will be provided in the case Ollama is installed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installation** | [**OllamaDeployment**](OllamaDeployment.md) |  | [optional] 
**installing** | [**OllamaDeployment**](OllamaDeployment.md) |  | [optional] 
**recommendation** | [**OllamaRecommendation**](OllamaRecommendation.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**update_required** | [**OllamaDeployment**](OllamaDeployment.md) |  | [optional] 
**updating** | [**OllamaDeployment**](OllamaDeployment.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.ollama_status import OllamaStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OllamaStatus from a JSON string
ollama_status_instance = OllamaStatus.from_json(json)
# print the JSON string representation of the object
print(OllamaStatus.to_json())

# convert the object into a dict
ollama_status_dict = ollama_status_instance.to_dict()
# create an instance of OllamaStatus from a dict
ollama_status_from_dict = OllamaStatus.from_dict(ollama_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


