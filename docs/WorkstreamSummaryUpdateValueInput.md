# WorkstreamSummaryUpdateValueInput

This is the input model for updating the textual value of a WorkstreamSummary.  optionally you may pass in the annotation, or we will get the annotation that is the summary prioritizing the summary that is the updated the most recently.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotation** | [**ReferencedAnnotation**](ReferencedAnnotation.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**value** | **str** |  | 
**workstream_summary** | [**ReferencedWorkstreamSummary**](ReferencedWorkstreamSummary.md) |  | 

## Example

```python
from pieces_os_client.models.workstream_summary_update_value_input import WorkstreamSummaryUpdateValueInput

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSummaryUpdateValueInput from a JSON string
workstream_summary_update_value_input_instance = WorkstreamSummaryUpdateValueInput.from_json(json)
# print the JSON string representation of the object
print(WorkstreamSummaryUpdateValueInput.to_json())

# convert the object into a dict
workstream_summary_update_value_input_dict = workstream_summary_update_value_input_instance.to_dict()
# create an instance of WorkstreamSummaryUpdateValueInput from a dict
workstream_summary_update_value_input_from_dict = WorkstreamSummaryUpdateValueInput.from_dict(workstream_summary_update_value_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


