# DescopeUserSubscription

This is the descope user subscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**name** | **str** |  | 
**created_at** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**nextbilled_at** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**paused_at** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**canceled_at** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**active** | **bool** |  | 
**term** | [**SubscriptionTermEnum**](SubscriptionTermEnum.md) |  | 
**quantity** | **int** |  | 
**subscription_id** | **str** |  | 
**product_id** | **str** |  | 
**price_id** | **str** |  | 

## Example

```python
from pieces_os_client.models.descope_user_subscription import DescopeUserSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of DescopeUserSubscription from a JSON string
descope_user_subscription_instance = DescopeUserSubscription.from_json(json)
# print the JSON string representation of the object
print DescopeUserSubscription.to_json()

# convert the object into a dict
descope_user_subscription_dict = descope_user_subscription_instance.to_dict()
# create an instance of DescopeUserSubscription from a dict
descope_user_subscription_from_dict = DescopeUserSubscription.from_dict(descope_user_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


