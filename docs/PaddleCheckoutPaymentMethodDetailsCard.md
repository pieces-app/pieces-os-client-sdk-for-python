# PaddleCheckoutPaymentMethodDetailsCard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**last4** | **str** |  | 
**expiry_month** | **int** |  | 
**expiry_year** | **int** |  | 

## Example

```python
from pieces_os_client.models.paddle_checkout_payment_method_details_card import PaddleCheckoutPaymentMethodDetailsCard

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutPaymentMethodDetailsCard from a JSON string
paddle_checkout_payment_method_details_card_instance = PaddleCheckoutPaymentMethodDetailsCard.from_json(json)
# print the JSON string representation of the object
print PaddleCheckoutPaymentMethodDetailsCard.to_json()

# convert the object into a dict
paddle_checkout_payment_method_details_card_dict = paddle_checkout_payment_method_details_card_instance.to_dict()
# create an instance of PaddleCheckoutPaymentMethodDetailsCard from a dict
paddle_checkout_payment_method_details_card_from_dict = PaddleCheckoutPaymentMethodDetailsCard.from_dict(paddle_checkout_payment_method_details_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


