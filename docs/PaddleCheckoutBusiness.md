# PaddleCheckoutBusiness


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**tax_identifier** | **str** |  | 

## Example

```python
from pieces_os_client.models.paddle_checkout_business import PaddleCheckoutBusiness

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutBusiness from a JSON string
paddle_checkout_business_instance = PaddleCheckoutBusiness.from_json(json)
# print the JSON string representation of the object
print PaddleCheckoutBusiness.to_json()

# convert the object into a dict
paddle_checkout_business_dict = paddle_checkout_business_instance.to_dict()
# create an instance of PaddleCheckoutBusiness from a dict
paddle_checkout_business_from_dict = PaddleCheckoutBusiness.from_dict(paddle_checkout_business_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


