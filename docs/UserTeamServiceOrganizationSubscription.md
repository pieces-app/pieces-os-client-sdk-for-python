# UserTeamServiceOrganizationSubscription

This is the descope user subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | 
**canceled_at** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**created_at** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**name** | **str** |  | 
**nextbilled_at** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**paused_at** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**price_id** | **str** |  | 
**product_id** | **str** |  | 
**quantity** | **int** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**subscription_id** | **str** |  | 
**term** | [**SubscriptionTermEnum**](SubscriptionTermEnum.md) |  | 

## Example

```python
from pieces_os_client.models.user_team_service_organization_subscription import UserTeamServiceOrganizationSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of UserTeamServiceOrganizationSubscription from a JSON string
user_team_service_organization_subscription_instance = UserTeamServiceOrganizationSubscription.from_json(json)
# print the JSON string representation of the object
print(UserTeamServiceOrganizationSubscription.to_json())

# convert the object into a dict
user_team_service_organization_subscription_dict = user_team_service_organization_subscription_instance.to_dict()
# create an instance of UserTeamServiceOrganizationSubscription from a dict
user_team_service_organization_subscription_from_dict = UserTeamServiceOrganizationSubscription.from_dict(user_team_service_organization_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


