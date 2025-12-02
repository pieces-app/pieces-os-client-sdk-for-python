# PaddleCheckoutEvent

Top-level wrapper that discriminates on name or type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**name** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**code** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 
**errors** | [**List[PaddleCheckoutErrorDetail]**](PaddleCheckoutErrorDetail.md) |  | [optional] 
**error** | [**PaddleCheckoutErrorEventError**](PaddleCheckoutErrorEventError.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.paddle_checkout_event import PaddleCheckoutEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutEvent from a JSON string
paddle_checkout_event_instance = PaddleCheckoutEvent.from_json(json)
# print the JSON string representation of the object
print(PaddleCheckoutEvent.to_json())

# convert the object into a dict
paddle_checkout_event_dict = paddle_checkout_event_instance.to_dict()
# create an instance of PaddleCheckoutEvent from a dict
paddle_checkout_event_from_dict = PaddleCheckoutEvent.from_dict(paddle_checkout_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


