# PaddleCheckoutItem

One line-item in the checkout. billing_cycle or trial_period may be null.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**price_id** | **str** |  | 
**product** | [**PaddleCheckoutProduct**](PaddleCheckoutProduct.md) |  | 
**billing_cycle** | [**PaddleCheckoutBillingCycle**](PaddleCheckoutBillingCycle.md) |  | [optional] 
**trial_period** | **int** |  | [optional] 
**quantity** | **int** |  | 
**totals** | [**PaddleCheckoutTotals**](PaddleCheckoutTotals.md) |  | 
**recurring_totals** | [**PaddleCheckoutTotals**](PaddleCheckoutTotals.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.paddle_checkout_item import PaddleCheckoutItem

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutItem from a JSON string
paddle_checkout_item_instance = PaddleCheckoutItem.from_json(json)
# print the JSON string representation of the object
print PaddleCheckoutItem.to_json()

# convert the object into a dict
paddle_checkout_item_dict = paddle_checkout_item_instance.to_dict()
# create an instance of PaddleCheckoutItem from a dict
paddle_checkout_item_from_dict = PaddleCheckoutItem.from_dict(paddle_checkout_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


