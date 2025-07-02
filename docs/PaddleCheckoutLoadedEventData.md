# PaddleCheckoutLoadedEventData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transaction_id** | **str** |  | 
**status** | **str** |  | 
**custom_data** | **object** |  | [optional] 
**currency_code** | **str** |  | 
**customer** | [**PaddleCheckoutCustomer**](PaddleCheckoutCustomer.md) |  | 
**items** | [**List[PaddleCheckoutItem]**](PaddleCheckoutItem.md) |  | 
**totals** | [**PaddleCheckoutTotals**](PaddleCheckoutTotals.md) |  | 
**payment** | [**PaddleCheckoutPayment**](PaddleCheckoutPayment.md) |  | 
**settings** | [**PaddleCheckoutSettings**](PaddleCheckoutSettings.md) |  | 
**recurring_totals** | [**PaddleCheckoutTotals**](PaddleCheckoutTotals.md) |  | 

## Example

```python
from pieces_os_client.models.paddle_checkout_loaded_event_data import PaddleCheckoutLoadedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutLoadedEventData from a JSON string
paddle_checkout_loaded_event_data_instance = PaddleCheckoutLoadedEventData.from_json(json)
# print the JSON string representation of the object
print PaddleCheckoutLoadedEventData.to_json()

# convert the object into a dict
paddle_checkout_loaded_event_data_dict = paddle_checkout_loaded_event_data_instance.to_dict()
# create an instance of PaddleCheckoutLoadedEventData from a dict
paddle_checkout_loaded_event_data_from_dict = PaddleCheckoutLoadedEventData.from_dict(paddle_checkout_loaded_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


