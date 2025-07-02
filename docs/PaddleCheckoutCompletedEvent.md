# PaddleCheckoutCompletedEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**name** | **str** |  | 
**data** | [**PaddleCheckoutLoadedEventData**](PaddleCheckoutLoadedEventData.md) |  | 

## Example

```python
from pieces_os_client.models.paddle_checkout_completed_event import PaddleCheckoutCompletedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutCompletedEvent from a JSON string
paddle_checkout_completed_event_instance = PaddleCheckoutCompletedEvent.from_json(json)
# print the JSON string representation of the object
print PaddleCheckoutCompletedEvent.to_json()

# convert the object into a dict
paddle_checkout_completed_event_dict = paddle_checkout_completed_event_instance.to_dict()
# create an instance of PaddleCheckoutCompletedEvent from a dict
paddle_checkout_completed_event_from_dict = PaddleCheckoutCompletedEvent.from_dict(paddle_checkout_completed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


