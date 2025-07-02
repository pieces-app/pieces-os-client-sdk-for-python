# Subscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** | The id of the subscription | 
**name** | **str** | The name of the subscription | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**user** | [**ReferencedUser**](ReferencedUser.md) |  | 
**next_billing_date** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**paused** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**cancelled** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**active** | **bool** |  | 
**term** | [**SubscriptionTermEnum**](SubscriptionTermEnum.md) |  | 
**quantity** | **int** |  | 
**subscription_id** | **str** |  | 
**product_id** | **str** |  | 
**score** | [**Score**](Score.md) |  | [optional] 
**price_id** | **str** |  | 

## Example

```python
from pieces_os_client.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print Subscription.to_json()

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_from_dict = Subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


