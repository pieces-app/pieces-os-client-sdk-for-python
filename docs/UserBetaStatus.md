# UserBetaStatus

This is used to either grant or remove a specific provider betastatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**auth0** | [**Auth0UserBetaStatus**](Auth0UserBetaStatus.md) |  | [optional] 
**user** | **str** |  | 

## Example

```python
from pieces_os_client.models.user_beta_status import UserBetaStatus

# TODO update the JSON string below
json = "{}"
# create an instance of UserBetaStatus from a JSON string
user_beta_status_instance = UserBetaStatus.from_json(json)
# print the JSON string representation of the object
print UserBetaStatus.to_json()

# convert the object into a dict
user_beta_status_dict = user_beta_status_instance.to_dict()
# create an instance of UserBetaStatus from a dict
user_beta_status_from_dict = UserBetaStatus.from_dict(user_beta_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


