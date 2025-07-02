# PaddleCheckoutTotals


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**subtotal** | **float** |  | 
**tax** | **float** |  | 
**total** | **float** |  | 
**discount** | **float** |  | 
**balance** | **float** |  | 
**credit** | **float** |  | 

## Example

```python
from pieces_os_client.models.paddle_checkout_totals import PaddleCheckoutTotals

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutTotals from a JSON string
paddle_checkout_totals_instance = PaddleCheckoutTotals.from_json(json)
# print the JSON string representation of the object
print PaddleCheckoutTotals.to_json()

# convert the object into a dict
paddle_checkout_totals_dict = paddle_checkout_totals_instance.to_dict()
# create an instance of PaddleCheckoutTotals from a dict
paddle_checkout_totals_from_dict = PaddleCheckoutTotals.from_dict(paddle_checkout_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


