# SeededSubscription

A minimal, creation-focused model for creating a Subscription. Uses string IDs for references.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | 
**cancelled** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**name** | **str** |  | 
**next_billing_date** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**paused** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**price_id** | **str** |  | 
**product_id** | **str** |  | 
**quantity** | **int** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**subscription_id** | **str** |  | 
**term** | [**SubscriptionTermEnum**](SubscriptionTermEnum.md) |  | 
**user** | [**ReferencedUser**](ReferencedUser.md) |  | 

## Example

```python
from pieces_os_client.models.seeded_subscription import SeededSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of SeededSubscription from a JSON string
seeded_subscription_instance = SeededSubscription.from_json(json)
# print the JSON string representation of the object
print(SeededSubscription.to_json())

# convert the object into a dict
seeded_subscription_dict = seeded_subscription_instance.to_dict()
# create an instance of SeededSubscription from a dict
seeded_subscription_from_dict = SeededSubscription.from_dict(seeded_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


