# WorkstreamSummariesMergeOutput

Output model for merging multiple workstream summaries, containing the newly created merged summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**summary** | [**ReferencedWorkstreamSummary**](ReferencedWorkstreamSummary.md) |  | 

## Example

```python
from pieces_os_client.models.workstream_summaries_merge_output import WorkstreamSummariesMergeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSummariesMergeOutput from a JSON string
workstream_summaries_merge_output_instance = WorkstreamSummariesMergeOutput.from_json(json)
# print the JSON string representation of the object
print(WorkstreamSummariesMergeOutput.to_json())

# convert the object into a dict
workstream_summaries_merge_output_dict = workstream_summaries_merge_output_instance.to_dict()
# create an instance of WorkstreamSummariesMergeOutput from a dict
workstream_summaries_merge_output_from_dict = WorkstreamSummariesMergeOutput.from_dict(workstream_summaries_merge_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


