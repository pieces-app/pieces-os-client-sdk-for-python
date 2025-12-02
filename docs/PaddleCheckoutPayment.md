# PaddleCheckoutPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method_details** | [**PaddleCheckoutPaymentMethodDetails**](PaddleCheckoutPaymentMethodDetails.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.paddle_checkout_payment import PaddleCheckoutPayment

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutPayment from a JSON string
paddle_checkout_payment_instance = PaddleCheckoutPayment.from_json(json)
# print the JSON string representation of the object
print(PaddleCheckoutPayment.to_json())

# convert the object into a dict
paddle_checkout_payment_dict = paddle_checkout_payment_instance.to_dict()
# create an instance of PaddleCheckoutPayment from a dict
paddle_checkout_payment_from_dict = PaddleCheckoutPayment.from_dict(paddle_checkout_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


