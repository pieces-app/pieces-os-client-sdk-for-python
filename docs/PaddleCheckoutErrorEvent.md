# PaddleCheckoutErrorEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**name** | **str** |  | 
**data** | **object** |  | 
**error** | [**PaddleCheckoutErrorEventError**](PaddleCheckoutErrorEventError.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.paddle_checkout_error_event import PaddleCheckoutErrorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutErrorEvent from a JSON string
paddle_checkout_error_event_instance = PaddleCheckoutErrorEvent.from_json(json)
# print the JSON string representation of the object
print PaddleCheckoutErrorEvent.to_json()

# convert the object into a dict
paddle_checkout_error_event_dict = paddle_checkout_error_event_instance.to_dict()
# create an instance of PaddleCheckoutErrorEvent from a dict
paddle_checkout_error_event_from_dict = PaddleCheckoutErrorEvent.from_dict(paddle_checkout_error_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


