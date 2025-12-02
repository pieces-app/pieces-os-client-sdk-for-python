# PaddleCheckoutPaymentMethodDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**PaddleCheckoutPaymentMethodDetailsCard**](PaddleCheckoutPaymentMethodDetailsCard.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from pieces_os_client.models.paddle_checkout_payment_method_details import PaddleCheckoutPaymentMethodDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutPaymentMethodDetails from a JSON string
paddle_checkout_payment_method_details_instance = PaddleCheckoutPaymentMethodDetails.from_json(json)
# print the JSON string representation of the object
print(PaddleCheckoutPaymentMethodDetails.to_json())

# convert the object into a dict
paddle_checkout_payment_method_details_dict = paddle_checkout_payment_method_details_instance.to_dict()
# create an instance of PaddleCheckoutPaymentMethodDetails from a dict
paddle_checkout_payment_method_details_from_dict = PaddleCheckoutPaymentMethodDetails.from_dict(paddle_checkout_payment_method_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


