# PaddleCheckoutProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**id** | **str** |  | 
**image_url** | **str** |  | 
**name** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.paddle_checkout_product import PaddleCheckoutProduct

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutProduct from a JSON string
paddle_checkout_product_instance = PaddleCheckoutProduct.from_json(json)
# print the JSON string representation of the object
print(PaddleCheckoutProduct.to_json())

# convert the object into a dict
paddle_checkout_product_dict = paddle_checkout_product_instance.to_dict()
# create an instance of PaddleCheckoutProduct from a dict
paddle_checkout_product_from_dict = PaddleCheckoutProduct.from_dict(paddle_checkout_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


