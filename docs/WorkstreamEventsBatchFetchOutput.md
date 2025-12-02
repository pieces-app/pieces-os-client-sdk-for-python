# WorkstreamEventsBatchFetchOutput

Output model for batch fetching workstream events. Properties: - workstreamEvents: The successfully fetched workstream events (required) - notFound: List of UUIDs that were requested but not found 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_found** | **List[str]** | List of UUIDs that were requested but not found | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**workstream_events** | [**WorkstreamEvents**](WorkstreamEvents.md) |  | 

## Example

```python
from pieces_os_client.models.workstream_events_batch_fetch_output import WorkstreamEventsBatchFetchOutput

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamEventsBatchFetchOutput from a JSON string
workstream_events_batch_fetch_output_instance = WorkstreamEventsBatchFetchOutput.from_json(json)
# print the JSON string representation of the object
print(WorkstreamEventsBatchFetchOutput.to_json())

# convert the object into a dict
workstream_events_batch_fetch_output_dict = workstream_events_batch_fetch_output_instance.to_dict()
# create an instance of WorkstreamEventsBatchFetchOutput from a dict
workstream_events_batch_fetch_output_from_dict = WorkstreamEventsBatchFetchOutput.from_dict(workstream_events_batch_fetch_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


