# SeededTrackedWorkstreamSummaryEvent

This is a pre-created(seed) TrackedWorkstreamSummaryEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**identifier_description_pair** | [**TrackedWorkstreamSummaryEventIdentifierDescriptionPairs**](TrackedWorkstreamSummaryEventIdentifierDescriptionPairs.md) |  | 
**summary** | [**ReferencedWorkstreamSummary**](ReferencedWorkstreamSummary.md) |  | 
**metadata** | [**TrackedWorkstreamSummaryEventMetadata**](TrackedWorkstreamSummaryEventMetadata.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_tracked_workstream_summary_event import SeededTrackedWorkstreamSummaryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SeededTrackedWorkstreamSummaryEvent from a JSON string
seeded_tracked_workstream_summary_event_instance = SeededTrackedWorkstreamSummaryEvent.from_json(json)
# print the JSON string representation of the object
print SeededTrackedWorkstreamSummaryEvent.to_json()

# convert the object into a dict
seeded_tracked_workstream_summary_event_dict = seeded_tracked_workstream_summary_event_instance.to_dict()
# create an instance of SeededTrackedWorkstreamSummaryEvent from a dict
seeded_tracked_workstream_summary_event_from_dict = SeededTrackedWorkstreamSummaryEvent.from_dict(seeded_tracked_workstream_summary_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


