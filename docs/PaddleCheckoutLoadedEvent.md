# PaddleCheckoutLoadedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PaddleCheckoutLoadedEventData**](PaddleCheckoutLoadedEventData.md) |  | 
**name** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.paddle_checkout_loaded_event import PaddleCheckoutLoadedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PaddleCheckoutLoadedEvent from a JSON string
paddle_checkout_loaded_event_instance = PaddleCheckoutLoadedEvent.from_json(json)
# print the JSON string representation of the object
print(PaddleCheckoutLoadedEvent.to_json())

# convert the object into a dict
paddle_checkout_loaded_event_dict = paddle_checkout_loaded_event_instance.to_dict()
# create an instance of PaddleCheckoutLoadedEvent from a dict
paddle_checkout_loaded_event_from_dict = PaddleCheckoutLoadedEvent.from_dict(paddle_checkout_loaded_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


