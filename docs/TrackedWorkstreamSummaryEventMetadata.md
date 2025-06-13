# TrackedWorkstreamSummaryEventMetadata

This is the metadata for the the WorkstreamSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**sentiment** | [**TrackedWorkstreamSummarySentimentMetadata**](TrackedWorkstreamSummarySentimentMetadata.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.tracked_workstream_summary_event_metadata import TrackedWorkstreamSummaryEventMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedWorkstreamSummaryEventMetadata from a JSON string
tracked_workstream_summary_event_metadata_instance = TrackedWorkstreamSummaryEventMetadata.from_json(json)
# print the JSON string representation of the object
print TrackedWorkstreamSummaryEventMetadata.to_json()

# convert the object into a dict
tracked_workstream_summary_event_metadata_dict = tracked_workstream_summary_event_metadata_instance.to_dict()
# create an instance of TrackedWorkstreamSummaryEventMetadata from a dict
tracked_workstream_summary_event_metadata_from_dict = TrackedWorkstreamSummaryEventMetadata.from_dict(tracked_workstream_summary_event_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


