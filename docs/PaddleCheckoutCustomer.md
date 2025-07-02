# PaddleCheckoutCustomer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**address** | [**PaddleCheckoutAddress**](PaddleCheckoutAddress.md) |  | [optional] 
**business** | [**PaddleCheckoutBusiness**](PaddleCheckoutBusiness.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.paddle_checkout_customer import PaddleCheckoutCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutCustomer from a JSON string
paddle_checkout_customer_instance = PaddleCheckoutCustomer.from_json(json)
# print the JSON string representation of the object
print PaddleCheckoutCustomer.to_json()

# convert the object into a dict
paddle_checkout_customer_dict = paddle_checkout_customer_instance.to_dict()
# create an instance of PaddleCheckoutCustomer from a dict
paddle_checkout_customer_from_dict = PaddleCheckoutCustomer.from_dict(paddle_checkout_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


