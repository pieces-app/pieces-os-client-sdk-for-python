# PaddleCheckoutUpdatedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaddleCheckoutLoadedEventData**](PaddleCheckoutLoadedEventData.md) |  | 
**name** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.paddle_checkout_updated_event import PaddleCheckoutUpdatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutUpdatedEvent from a JSON string
paddle_checkout_updated_event_instance = PaddleCheckoutUpdatedEvent.from_json(json)
# print the JSON string representation of the object
print(PaddleCheckoutUpdatedEvent.to_json())

# convert the object into a dict
paddle_checkout_updated_event_dict = paddle_checkout_updated_event_instance.to_dict()
# create an instance of PaddleCheckoutUpdatedEvent from a dict
paddle_checkout_updated_event_from_dict = PaddleCheckoutUpdatedEvent.from_dict(paddle_checkout_updated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


