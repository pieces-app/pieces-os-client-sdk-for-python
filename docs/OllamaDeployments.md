# OllamaDeployments

This is the plural model for Deployment of Ollama.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[OllamaDeployment]**](OllamaDeployment.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.ollama_deployments import OllamaDeployments

# TODO update the JSON string below
json = "{}"
# create an instance of OllamaDeployments from a JSON string
ollama_deployments_instance = OllamaDeployments.from_json(json)
# print the JSON string representation of the object
print(OllamaDeployments.to_json())

# convert the object into a dict
ollama_deployments_dict = ollama_deployments_instance.to_dict()
# create an instance of OllamaDeployments from a dict
ollama_deployments_from_dict = OllamaDeployments.from_dict(ollama_deployments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


