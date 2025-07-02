# UserCheckoutInput

Input model for the user checkout endpoint. This is a generic model that can be extended in the future.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.user_checkout_input import UserCheckoutInput

# TODO update the JSON string below
json = "{}"
# create an instance of UserCheckoutInput from a JSON string
user_checkout_input_instance = UserCheckoutInput.from_json(json)
# print the JSON string representation of the object
print UserCheckoutInput.to_json()

# convert the object into a dict
user_checkout_input_dict = user_checkout_input_instance.to_dict()
# create an instance of UserCheckoutInput from a dict
user_checkout_input_from_dict = UserCheckoutInput.from_dict(user_checkout_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


