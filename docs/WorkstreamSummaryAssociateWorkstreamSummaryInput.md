# WorkstreamSummaryAssociateWorkstreamSummaryInput

NOTE: this is an optional body provided within the endpoint. This is the input model for associating two WorkstreamSummary objects.  These are optional however if a parent is provided so is a child.  A parent and child can never be the same uuid and the child and the parent can only ever be the uuids that we are associating with the endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child** | **str** | The UUID of the child workstream summary | [optional] 
**parent** | **str** | The UUID of the parent workstream summary | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_summary_associate_workstream_summary_input import WorkstreamSummaryAssociateWorkstreamSummaryInput

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSummaryAssociateWorkstreamSummaryInput from a JSON string
workstream_summary_associate_workstream_summary_input_instance = WorkstreamSummaryAssociateWorkstreamSummaryInput.from_json(json)
# print the JSON string representation of the object
print(WorkstreamSummaryAssociateWorkstreamSummaryInput.to_json())

# convert the object into a dict
workstream_summary_associate_workstream_summary_input_dict = workstream_summary_associate_workstream_summary_input_instance.to_dict()
# create an instance of WorkstreamSummaryAssociateWorkstreamSummaryInput from a dict
workstream_summary_associate_workstream_summary_input_from_dict = WorkstreamSummaryAssociateWorkstreamSummaryInput.from_dict(workstream_summary_associate_workstream_summary_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


