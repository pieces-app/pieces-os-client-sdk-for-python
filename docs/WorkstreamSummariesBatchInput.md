# WorkstreamSummariesBatchInput

Input model for batch fetching workstream summaries. Note: This model accepts an optional list of summary UUIDs that will be fetched. The workstreamSummaries property is optional to support future functionality such as fetching all summaries within a given time range or other filtering criteria. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**workstream_summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_summaries_batch_input import WorkstreamSummariesBatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSummariesBatchInput from a JSON string
workstream_summaries_batch_input_instance = WorkstreamSummariesBatchInput.from_json(json)
# print the JSON string representation of the object
print(WorkstreamSummariesBatchInput.to_json())

# convert the object into a dict
workstream_summaries_batch_input_dict = workstream_summaries_batch_input_instance.to_dict()
# create an instance of WorkstreamSummariesBatchInput from a dict
workstream_summaries_batch_input_from_dict = WorkstreamSummariesBatchInput.from_dict(workstream_summaries_batch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


