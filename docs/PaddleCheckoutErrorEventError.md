# PaddleCheckoutErrorEventError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**code** | **str** |  | 
**detail** | **str** |  | 
**documentation_url** | **str** |  | 

## Example

```python
from pieces_os_client.models.paddle_checkout_error_event_error import PaddleCheckoutErrorEventError

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutErrorEventError from a JSON string
paddle_checkout_error_event_error_instance = PaddleCheckoutErrorEventError.from_json(json)
# print the JSON string representation of the object
print PaddleCheckoutErrorEventError.to_json()

# convert the object into a dict
paddle_checkout_error_event_error_dict = paddle_checkout_error_event_error_instance.to_dict()
# create an instance of PaddleCheckoutErrorEventError from a dict
paddle_checkout_error_event_error_from_dict = PaddleCheckoutErrorEventError.from_dict(paddle_checkout_error_event_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


