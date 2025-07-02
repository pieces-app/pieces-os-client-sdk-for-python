# UserManageSubscriptionsInput

Input model for the user manage subscriptions endpoint. This is a generic model that can be extended in the future.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.user_manage_subscriptions_input import UserManageSubscriptionsInput

# TODO update the JSON string below
json = "{}"
# create an instance of UserManageSubscriptionsInput from a JSON string
user_manage_subscriptions_input_instance = UserManageSubscriptionsInput.from_json(json)
# print the JSON string representation of the object
print UserManageSubscriptionsInput.to_json()

# convert the object into a dict
user_manage_subscriptions_input_dict = user_manage_subscriptions_input_instance.to_dict()
# create an instance of UserManageSubscriptionsInput from a dict
user_manage_subscriptions_input_from_dict = UserManageSubscriptionsInput.from_dict(user_manage_subscriptions_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


