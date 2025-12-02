# PaddleCheckoutAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | 
**country_code** | **str** |  | 
**first_line** | **str** |  | [optional] 
**id** | **str** |  | 
**postal_code** | **str** |  | 
**region** | **str** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.paddle_checkout_address import PaddleCheckoutAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutAddress from a JSON string
paddle_checkout_address_instance = PaddleCheckoutAddress.from_json(json)
# print the JSON string representation of the object
print(PaddleCheckoutAddress.to_json())

# convert the object into a dict
paddle_checkout_address_dict = paddle_checkout_address_instance.to_dict()
# create an instance of PaddleCheckoutAddress from a dict
paddle_checkout_address_from_dict = PaddleCheckoutAddress.from_dict(paddle_checkout_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


