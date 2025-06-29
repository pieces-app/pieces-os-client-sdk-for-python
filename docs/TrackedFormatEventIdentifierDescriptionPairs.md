# TrackedFormatEventIdentifierDescriptionPairs

This is a model that allows us to send send over super specific format related events such as copied, deleted, downloaded, etc

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**format_created** | **str** | The key value pair for an asset being created. | [optional] [default to 'UNKNOWN']
**format_copied** | **str** | If a format was copied entirely | [optional] [default to 'UNKNOWN']
**format_partially_copied** | **str** | If a format was copied partially | [optional] [default to 'UNKNOWN']
**format_downloaded** | **str** | If a format was downloaded | [optional] [default to 'UNKNOWN']
**format_deleted** | **str** | If an format was deleted | [optional] [default to 'UNKNOWN']
**format_generic_classification_updated** | **str** | If a generic classification was changed on a format | [optional] [default to 'UNKNOWN']
**format_specific_classification_updated** | **str** | If a specific classification was changed on a format | [optional] [default to 'UNKNOWN']
**format_updated** | **str** | a format was updated, generic update. | [optional] [default to 'UNKNOWN']
**format_inserted** | **str** | a format was inserted | [optional] [default to 'UNKNOWN']
**format_value_edited** | **str** | a format&#39;s value was update ie, the text, etc... | [optional] [default to 'UNKNOWN']

## Example

```python
from pieces_os_client.models.tracked_format_event_identifier_description_pairs import TrackedFormatEventIdentifierDescriptionPairs

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedFormatEventIdentifierDescriptionPairs from a JSON string
tracked_format_event_identifier_description_pairs_instance = TrackedFormatEventIdentifierDescriptionPairs.from_json(json)
# print the JSON string representation of the object
print TrackedFormatEventIdentifierDescriptionPairs.to_json()

# convert the object into a dict
tracked_format_event_identifier_description_pairs_dict = tracked_format_event_identifier_description_pairs_instance.to_dict()
# create an instance of TrackedFormatEventIdentifierDescriptionPairs from a dict
tracked_format_event_identifier_description_pairs_from_dict = TrackedFormatEventIdentifierDescriptionPairs.from_dict(tracked_format_event_identifier_description_pairs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


