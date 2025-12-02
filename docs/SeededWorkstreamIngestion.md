# SeededWorkstreamIngestion

This is used as the input in the Context ingestion endpoint for the feed.  This will take in a required seed, this will get created as an internal WorkstreamEvent until we determine internally that this event is relevant and will then attach it to a WorkstreamSummary and it will get moved over to a WorkstreamEvent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**SeededWorkstreamEvent**](SeededWorkstreamEvent.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_workstream_ingestion import SeededWorkstreamIngestion

# TODO update the JSON string below
json = "{}"
# create an instance of SeededWorkstreamIngestion from a JSON string
seeded_workstream_ingestion_instance = SeededWorkstreamIngestion.from_json(json)
# print the JSON string representation of the object
print(SeededWorkstreamIngestion.to_json())

# convert the object into a dict
seeded_workstream_ingestion_dict = seeded_workstream_ingestion_instance.to_dict()
# create an instance of SeededWorkstreamIngestion from a dict
seeded_workstream_ingestion_from_dict = SeededWorkstreamIngestion.from_dict(seeded_workstream_ingestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


