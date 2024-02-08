# TrackedFormatEvent

This is a model that represents a generic event that we may want to track in relation to a format, for example beamed, copied, downloaded, and view. ** Note: This is the model that will get returned by our api, and is. Representative of a full TrackedFormat event. **

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**format** | [**TrackedFormat**](TrackedFormat.md) |  | 
**identifier_description_pair** | [**TrackedFormatEventIdentifierDescriptionPairs**](TrackedFormatEventIdentifierDescriptionPairs.md) |  | 
**metadata** | [**TrackedFormatEventMetadata**](TrackedFormatEventMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.tracked_format_event import TrackedFormatEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedFormatEvent from a JSON string
tracked_format_event_instance = TrackedFormatEvent.from_json(json)
# print the JSON string representation of the object
print TrackedFormatEvent.to_json()

# convert the object into a dict
tracked_format_event_dict = tracked_format_event_instance.to_dict()
# create an instance of TrackedFormatEvent from a dict
tracked_format_event_form_dict = tracked_format_event.from_dict(tracked_format_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


