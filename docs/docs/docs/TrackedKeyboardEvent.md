# TrackedKeyboardEvent

This is a model that will hold relavent information in relation to a keyboard(including shortcuts) analytics event (usage).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**description** | **str** | this is a description of the event, optional. | 
**shortcut** | **List[int]** | this is an array of of ascii values that represent numerics on your keyboard. | 

## Example

```python
from openapi_client.models.tracked_keyboard_event import TrackedKeyboardEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedKeyboardEvent from a JSON string
tracked_keyboard_event_instance = TrackedKeyboardEvent.from_json(json)
# print the JSON string representation of the object
print TrackedKeyboardEvent.to_json()

# convert the object into a dict
tracked_keyboard_event_dict = tracked_keyboard_event_instance.to_dict()
# create an instance of TrackedKeyboardEvent from a dict
tracked_keyboard_event_form_dict = tracked_keyboard_event.from_dict(tracked_keyboard_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


