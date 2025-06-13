# TrackedWorkstreamSummarySentimentMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**sentiment** | [**WorkstreamSummarySentimentEnum**](WorkstreamSummarySentimentEnum.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.tracked_workstream_summary_sentiment_metadata import TrackedWorkstreamSummarySentimentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedWorkstreamSummarySentimentMetadata from a JSON string
tracked_workstream_summary_sentiment_metadata_instance = TrackedWorkstreamSummarySentimentMetadata.from_json(json)
# print the JSON string representation of the object
print TrackedWorkstreamSummarySentimentMetadata.to_json()

# convert the object into a dict
tracked_workstream_summary_sentiment_metadata_dict = tracked_workstream_summary_sentiment_metadata_instance.to_dict()
# create an instance of TrackedWorkstreamSummarySentimentMetadata from a dict
tracked_workstream_summary_sentiment_metadata_from_dict = TrackedWorkstreamSummarySentimentMetadata.from_dict(tracked_workstream_summary_sentiment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


