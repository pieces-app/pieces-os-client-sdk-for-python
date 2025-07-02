# PaddleCheckoutWarningEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**name** | **str** |  | 
**code** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 
**errors** | [**List[PaddleCheckoutErrorDetail]**](PaddleCheckoutErrorDetail.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.paddle_checkout_warning_event import PaddleCheckoutWarningEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutWarningEvent from a JSON string
paddle_checkout_warning_event_instance = PaddleCheckoutWarningEvent.from_json(json)
# print the JSON string representation of the object
print PaddleCheckoutWarningEvent.to_json()

# convert the object into a dict
paddle_checkout_warning_event_dict = paddle_checkout_warning_event_instance.to_dict()
# create an instance of PaddleCheckoutWarningEvent from a dict
paddle_checkout_warning_event_from_dict = PaddleCheckoutWarningEvent.from_dict(paddle_checkout_warning_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


