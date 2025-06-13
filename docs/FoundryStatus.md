# FoundryStatus

This will get used in the Websocket and in the get request for Foundry Note:  - updating (nullable) will be used in the case an update is underway  - installing (nullable) will be used in the case an installation is underway  - updateRequired (nullable) will be used in the case an update is required  - installation (nullable) will be provided in the case Foundry is installed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**updating** | [**FoundryDeployment**](FoundryDeployment.md) |  | [optional] 
**installing** | [**FoundryDeployment**](FoundryDeployment.md) |  | [optional] 
**update_required** | [**FoundryDeployment**](FoundryDeployment.md) |  | [optional] 
**installation** | [**FoundryDeployment**](FoundryDeployment.md) |  | [optional] 
**recommendation** | [**FoundryRecommendation**](FoundryRecommendation.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.foundry_status import FoundryStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FoundryStatus from a JSON string
foundry_status_instance = FoundryStatus.from_json(json)
# print the JSON string representation of the object
print FoundryStatus.to_json()

# convert the object into a dict
foundry_status_dict = foundry_status_instance.to_dict()
# create an instance of FoundryStatus from a dict
foundry_status_from_dict = FoundryStatus.from_dict(foundry_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


