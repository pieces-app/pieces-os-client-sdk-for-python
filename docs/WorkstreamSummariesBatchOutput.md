# WorkstreamSummariesBatchOutput

Output model for batch fetching workstream summaries. Properties: - workstreamSummaries: The successfully fetched workstream summaries (required) - notFound: List of UUIDs that were requested but not found 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_found** | **List[str]** | List of UUIDs that were requested but not found | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**workstream_summaries** | [**WorkstreamSummaries**](WorkstreamSummaries.md) |  | 

## Example

```python
from pieces_os_client.models.workstream_summaries_batch_output import WorkstreamSummariesBatchOutput

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSummariesBatchOutput from a JSON string
workstream_summaries_batch_output_instance = WorkstreamSummariesBatchOutput.from_json(json)
# print the JSON string representation of the object
print(WorkstreamSummariesBatchOutput.to_json())

# convert the object into a dict
workstream_summaries_batch_output_dict = workstream_summaries_batch_output_instance.to_dict()
# create an instance of WorkstreamSummariesBatchOutput from a dict
workstream_summaries_batch_output_from_dict = WorkstreamSummariesBatchOutput.from_dict(workstream_summaries_batch_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


