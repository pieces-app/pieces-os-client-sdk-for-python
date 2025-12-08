# ReferencedWorkstreamSummaryToWorkstreamSummaryAssociation

this is a referenced minimal version of a WorkstreamSummaryToWorkstreamSummaryAssociation typically just our uuid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**reference** | [**FlattenedWorkstreamSummaryToWorkstreamSummaryAssociation**](FlattenedWorkstreamSummaryToWorkstreamSummaryAssociation.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.referenced_workstream_summary_to_workstream_summary_association import ReferencedWorkstreamSummaryToWorkstreamSummaryAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedWorkstreamSummaryToWorkstreamSummaryAssociation from a JSON string
referenced_workstream_summary_to_workstream_summary_association_instance = ReferencedWorkstreamSummaryToWorkstreamSummaryAssociation.from_json(json)
# print the JSON string representation of the object
print(ReferencedWorkstreamSummaryToWorkstreamSummaryAssociation.to_json())

# convert the object into a dict
referenced_workstream_summary_to_workstream_summary_association_dict = referenced_workstream_summary_to_workstream_summary_association_instance.to_dict()
# create an instance of ReferencedWorkstreamSummaryToWorkstreamSummaryAssociation from a dict
referenced_workstream_summary_to_workstream_summary_association_from_dict = ReferencedWorkstreamSummaryToWorkstreamSummaryAssociation.from_dict(referenced_workstream_summary_to_workstream_summary_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


