# WorkstreamEventsBatchFetchInput

Input model for batch fetching workstream events. Note: This model accepts an optional list of event UUIDs that will be fetched. The workstreamEvents property is optional to support future functionality such as fetching all events within a given time range or other filtering criteria. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**workstream_events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_events_batch_fetch_input import WorkstreamEventsBatchFetchInput

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamEventsBatchFetchInput from a JSON string
workstream_events_batch_fetch_input_instance = WorkstreamEventsBatchFetchInput.from_json(json)
# print the JSON string representation of the object
print(WorkstreamEventsBatchFetchInput.to_json())

# convert the object into a dict
workstream_events_batch_fetch_input_dict = workstream_events_batch_fetch_input_instance.to_dict()
# create an instance of WorkstreamEventsBatchFetchInput from a dict
workstream_events_batch_fetch_input_from_dict = WorkstreamEventsBatchFetchInput.from_dict(workstream_events_batch_fetch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


