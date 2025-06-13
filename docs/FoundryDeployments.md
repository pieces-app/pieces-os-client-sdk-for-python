# FoundryDeployments

This is the plural model for Deployment of Foundry.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[FoundryDeployment]**](FoundryDeployment.md) |  | 

## Example

```python
from pieces_os_client.models.foundry_deployments import FoundryDeployments

# TODO update the JSON string below
json = "{}"
# create an instance of FoundryDeployments from a JSON string
foundry_deployments_instance = FoundryDeployments.from_json(json)
# print the JSON string representation of the object
print FoundryDeployments.to_json()

# convert the object into a dict
foundry_deployments_dict = foundry_deployments_instance.to_dict()
# create an instance of FoundryDeployments from a dict
foundry_deployments_from_dict = FoundryDeployments.from_dict(foundry_deployments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


