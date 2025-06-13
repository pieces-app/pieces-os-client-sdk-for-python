# TrackedWorkstreamSummaryEventIdentifierDescriptionPairs

These are all of the available event types that are permitted in an object pair notation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**summary_created** | **str** | The key value pair for a summary being created. | [optional] [default to 'UNKNOWN']

## Example

```python
from pieces_os_client.models.tracked_workstream_summary_event_identifier_description_pairs import TrackedWorkstreamSummaryEventIdentifierDescriptionPairs

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedWorkstreamSummaryEventIdentifierDescriptionPairs from a JSON string
tracked_workstream_summary_event_identifier_description_pairs_instance = TrackedWorkstreamSummaryEventIdentifierDescriptionPairs.from_json(json)
# print the JSON string representation of the object
print TrackedWorkstreamSummaryEventIdentifierDescriptionPairs.to_json()

# convert the object into a dict
tracked_workstream_summary_event_identifier_description_pairs_dict = tracked_workstream_summary_event_identifier_description_pairs_instance.to_dict()
# create an instance of TrackedWorkstreamSummaryEventIdentifierDescriptionPairs from a dict
tracked_workstream_summary_event_identifier_description_pairs_from_dict = TrackedWorkstreamSummaryEventIdentifierDescriptionPairs.from_dict(tracked_workstream_summary_event_identifier_description_pairs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


