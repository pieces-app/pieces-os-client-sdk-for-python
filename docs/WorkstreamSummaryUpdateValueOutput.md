# WorkstreamSummaryUpdateValueOutput

This will return the annotation and the summary from the endpoint  The annotation is the annotation that was updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotation** | [**ReferencedAnnotation**](ReferencedAnnotation.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**workstream_summary** | [**ReferencedWorkstreamSummary**](ReferencedWorkstreamSummary.md) |  | 

## Example

```python
from pieces_os_client.models.workstream_summary_update_value_output import WorkstreamSummaryUpdateValueOutput

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSummaryUpdateValueOutput from a JSON string
workstream_summary_update_value_output_instance = WorkstreamSummaryUpdateValueOutput.from_json(json)
# print the JSON string representation of the object
print(WorkstreamSummaryUpdateValueOutput.to_json())

# convert the object into a dict
workstream_summary_update_value_output_dict = workstream_summary_update_value_output_instance.to_dict()
# create an instance of WorkstreamSummaryUpdateValueOutput from a dict
workstream_summary_update_value_output_from_dict = WorkstreamSummaryUpdateValueOutput.from_dict(workstream_summary_update_value_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


