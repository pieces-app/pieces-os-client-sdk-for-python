# SeededTrackedSessionEvent

A simple model to capture a Tracked Session to be send to the Connection API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**identifier_description_pair** | [**TrackedSessionEventIdentifierDescriptionPairs**](TrackedSessionEventIdentifierDescriptionPairs.md) |  | 

## Example

```python
from openapi_client.models.seeded_tracked_session_event import SeededTrackedSessionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SeededTrackedSessionEvent from a JSON string
seeded_tracked_session_event_instance = SeededTrackedSessionEvent.from_json(json)
# print the JSON string representation of the object
print SeededTrackedSessionEvent.to_json()

# convert the object into a dict
seeded_tracked_session_event_dict = seeded_tracked_session_event_instance.to_dict()
# create an instance of SeededTrackedSessionEvent from a dict
seeded_tracked_session_event_form_dict = seeded_tracked_session_event.from_dict(seeded_tracked_session_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


