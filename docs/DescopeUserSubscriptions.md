# DescopeUserSubscriptions

This is the descope user subscriptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[DescopeUserSubscription]**](DescopeUserSubscription.md) | This is the iterable of the descope user subscriptions | 

## Example

```python
from pieces_os_client.models.descope_user_subscriptions import DescopeUserSubscriptions

# TODO update the JSON string below
json = "{}"
# create an instance of DescopeUserSubscriptions from a JSON string
descope_user_subscriptions_instance = DescopeUserSubscriptions.from_json(json)
# print the JSON string representation of the object
print DescopeUserSubscriptions.to_json()

# convert the object into a dict
descope_user_subscriptions_dict = descope_user_subscriptions_instance.to_dict()
# create an instance of DescopeUserSubscriptions from a dict
descope_user_subscriptions_from_dict = DescopeUserSubscriptions.from_dict(descope_user_subscriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


