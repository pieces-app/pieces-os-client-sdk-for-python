# TrackedSessionEventIdentifierDescriptionPairs

These are all of the available event types that are permitted in an object pair notation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**session_initialized** | **str** | The key value pair for an application being opened. | [optional] [default to 'UNKNOWN']
**session_local_connection_succeeded** | **str** | There was a successful connection locally | [optional] [default to 'UNKNOWN']
**session_local_connection_failed** | **str** | There was a failed connection locally | [optional] [default to 'UNKNOWN']
**session_inactive** | **str** | If the current application is in the background or not, could also be minimized. | [optional] [default to 'UNKNOWN']
**session_active** | **str** | If the application has been brought to the forground. | [optional] [default to 'UNKNOWN']
**session_terminated** | **str** | If the user has closed the application, thus ending the session. | [optional] [default to 'UNKNOWN']
**session_authenticated_with_sign_in** | **str** | A user has signed into this session with a an external account | [optional] [default to 'UNKNOWN']
**session_unauthenticated_with_sign_out** | **str** | A user has signed out of this session | [optional] [default to 'UNKNOWN']
**session_unauthenticated_with_dismiss** | **str** | A user did not sign into the session with a dismissal | [optional] [default to 'UNKNOWN']
**session_unauthenticated_with_remind** | **str** | A user did not sign into the session with a reminder | [optional] [default to 'UNKNOWN']
**session_onboarding_initialized** | **str** | Onboarding has been initialized for this session | [optional] [default to 'UNKNOWN']
**session_onboarding_completed** | **str** | Onboarding has been completed for this session | [optional] [default to 'UNKNOWN']

## Example

```python
from pieces_os_client.models.tracked_session_event_identifier_description_pairs import TrackedSessionEventIdentifierDescriptionPairs

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedSessionEventIdentifierDescriptionPairs from a JSON string
tracked_session_event_identifier_description_pairs_instance = TrackedSessionEventIdentifierDescriptionPairs.from_json(json)
# print the JSON string representation of the object
print TrackedSessionEventIdentifierDescriptionPairs.to_json()

# convert the object into a dict
tracked_session_event_identifier_description_pairs_dict = tracked_session_event_identifier_description_pairs_instance.to_dict()
# create an instance of TrackedSessionEventIdentifierDescriptionPairs from a dict
tracked_session_event_identifier_description_pairs_from_dict = TrackedSessionEventIdentifierDescriptionPairs.from_dict(tracked_session_event_identifier_description_pairs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


