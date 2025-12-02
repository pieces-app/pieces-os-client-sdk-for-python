# UserCheckoutOutput

Output model for the user checkout endpoint. Contains user reference and can be extended with additional properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**user** | [**ReferencedUser**](ReferencedUser.md) |  | 

## Example

```python
from pieces_os_client.models.user_checkout_output import UserCheckoutOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UserCheckoutOutput from a JSON string
user_checkout_output_instance = UserCheckoutOutput.from_json(json)
# print the JSON string representation of the object
print(UserCheckoutOutput.to_json())

# convert the object into a dict
user_checkout_output_dict = user_checkout_output_instance.to_dict()
# create an instance of UserCheckoutOutput from a dict
user_checkout_output_from_dict = UserCheckoutOutput.from_dict(user_checkout_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


