# FoundryDeployment

A deployment will be used in 4 cases: 1. used to describe an installation in progress 2. used to describe an update in progress 3. used to say what deployment will be needed to upgrade to. 4. used to say what the current version of ollama is present on the machine.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | [optional] 
**status** | [**FoundryDeploymentStatusEnum**](FoundryDeploymentStatusEnum.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**percentage** | **float** | Optionally if the update is in progress you will receive a download percent(from 0-100). | [optional] 
**version** | **str** |  | 
**user_managed** | **bool** | Optionally set, specifically in the case where an update is required, and a user need to take manual action. | [optional] 

## Example

```python
from pieces_os_client.models.foundry_deployment import FoundryDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of FoundryDeployment from a JSON string
foundry_deployment_instance = FoundryDeployment.from_json(json)
# print the JSON string representation of the object
print FoundryDeployment.to_json()

# convert the object into a dict
foundry_deployment_dict = foundry_deployment_instance.to_dict()
# create an instance of FoundryDeployment from a dict
foundry_deployment_from_dict = FoundryDeployment.from_dict(foundry_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


