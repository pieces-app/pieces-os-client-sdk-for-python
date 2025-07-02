# PaddleCheckoutErrorDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**field** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from pieces_os_client.models.paddle_checkout_error_detail import PaddleCheckoutErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutErrorDetail from a JSON string
paddle_checkout_error_detail_instance = PaddleCheckoutErrorDetail.from_json(json)
# print the JSON string representation of the object
print PaddleCheckoutErrorDetail.to_json()

# convert the object into a dict
paddle_checkout_error_detail_dict = paddle_checkout_error_detail_instance.to_dict()
# create an instance of PaddleCheckoutErrorDetail from a dict
paddle_checkout_error_detail_from_dict = PaddleCheckoutErrorDetail.from_dict(paddle_checkout_error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


