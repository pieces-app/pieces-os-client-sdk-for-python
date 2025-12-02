# OllamaDeployment

A deployment will be used in 4 cases: 1. used to describe an installation in progress 2. used to describe an update in progress 3. used to say what deployment will be needed to upgrade to. 4. used to say what the current version of ollama is present on the machine.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**percentage** | **float** | Optionally if the update is in progress you will recieve a download percent(from 0-100). | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**status** | [**OllamaDeploymentStatusEnum**](OllamaDeploymentStatusEnum.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**user_managed** | **bool** | Optionally set, specifically in the case where an update is required, and a user need to take manual action. | [optional] 
**version** | **str** |  | 

## Example

```python
from pieces_os_client.models.ollama_deployment import OllamaDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of OllamaDeployment from a JSON string
ollama_deployment_instance = OllamaDeployment.from_json(json)
# print the JSON string representation of the object
print(OllamaDeployment.to_json())

# convert the object into a dict
ollama_deployment_dict = ollama_deployment_instance.to_dict()
# create an instance of OllamaDeployment from a dict
ollama_deployment_from_dict = OllamaDeployment.from_dict(ollama_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


