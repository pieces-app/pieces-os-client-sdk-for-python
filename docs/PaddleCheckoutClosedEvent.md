# PaddleCheckoutClosedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaddleCheckoutLoadedEventData**](PaddleCheckoutLoadedEventData.md) |  | 
**name** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.paddle_checkout_closed_event import PaddleCheckoutClosedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutClosedEvent from a JSON string
paddle_checkout_closed_event_instance = PaddleCheckoutClosedEvent.from_json(json)
# print the JSON string representation of the object
print(PaddleCheckoutClosedEvent.to_json())

# convert the object into a dict
paddle_checkout_closed_event_dict = paddle_checkout_closed_event_instance.to_dict()
# create an instance of PaddleCheckoutClosedEvent from a dict
paddle_checkout_closed_event_from_dict = PaddleCheckoutClosedEvent.from_dict(paddle_checkout_closed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


