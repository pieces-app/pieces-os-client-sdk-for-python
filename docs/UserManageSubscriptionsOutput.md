# UserManageSubscriptionsOutput

Output model for the user manage subscriptions endpoint. Contains user reference and can be extended with additional properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**user** | [**ReferencedUser**](ReferencedUser.md) |  | 

## Example

```python
from pieces_os_client.models.user_manage_subscriptions_output import UserManageSubscriptionsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UserManageSubscriptionsOutput from a JSON string
user_manage_subscriptions_output_instance = UserManageSubscriptionsOutput.from_json(json)
# print the JSON string representation of the object
print(UserManageSubscriptionsOutput.to_json())

# convert the object into a dict
user_manage_subscriptions_output_dict = user_manage_subscriptions_output_instance.to_dict()
# create an instance of UserManageSubscriptionsOutput from a dict
user_manage_subscriptions_output_from_dict = UserManageSubscriptionsOutput.from_dict(user_manage_subscriptions_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


