# WorkstreamIngestion

This is used for a returnable in the contest ingestion endpoint for the Feed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_ingestion import WorkstreamIngestion

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamIngestion from a JSON string
workstream_ingestion_instance = WorkstreamIngestion.from_json(json)
# print the JSON string representation of the object
print WorkstreamIngestion.to_json()

# convert the object into a dict
workstream_ingestion_dict = workstream_ingestion_instance.to_dict()
# create an instance of WorkstreamIngestion from a dict
workstream_ingestion_form_dict = workstream_ingestion.from_dict(workstream_ingestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


