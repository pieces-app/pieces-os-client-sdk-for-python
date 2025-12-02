# PaddleCheckoutBillingCycle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **int** |  | 
**interval** | **str** | e.g. &#39;month&#39;, &#39;year&#39; | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.paddle_checkout_billing_cycle import PaddleCheckoutBillingCycle

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutBillingCycle from a JSON string
paddle_checkout_billing_cycle_instance = PaddleCheckoutBillingCycle.from_json(json)
# print the JSON string representation of the object
print(PaddleCheckoutBillingCycle.to_json())

# convert the object into a dict
paddle_checkout_billing_cycle_dict = paddle_checkout_billing_cycle_instance.to_dict()
# create an instance of PaddleCheckoutBillingCycle from a dict
paddle_checkout_billing_cycle_from_dict = PaddleCheckoutBillingCycle.from_dict(paddle_checkout_billing_cycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


