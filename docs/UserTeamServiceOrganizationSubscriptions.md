# UserTeamServiceOrganizationSubscriptions

This is the descope user subscriptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[UserTeamServiceOrganizationSubscription]**](UserTeamServiceOrganizationSubscription.md) | This is the iterable of the descope user subscriptions | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.user_team_service_organization_subscriptions import UserTeamServiceOrganizationSubscriptions

# TODO update the JSON string below
json = "{}"
# create an instance of UserTeamServiceOrganizationSubscriptions from a JSON string
user_team_service_organization_subscriptions_instance = UserTeamServiceOrganizationSubscriptions.from_json(json)
# print the JSON string representation of the object
print(UserTeamServiceOrganizationSubscriptions.to_json())

# convert the object into a dict
user_team_service_organization_subscriptions_dict = user_team_service_organization_subscriptions_instance.to_dict()
# create an instance of UserTeamServiceOrganizationSubscriptions from a dict
user_team_service_organization_subscriptions_from_dict = UserTeamServiceOrganizationSubscriptions.from_dict(user_team_service_organization_subscriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


