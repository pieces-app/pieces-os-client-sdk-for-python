# FlattenedWorkstreamSummaryToWorkstreamSummaryAssociation

This is a DAG-Safe minimal representation of a workstream summary association  Association table for summary-to-summary relationships supporting both flexible relationships and hierarchical parent-child queries  note: this is done with light weight properties at the top level for fast queries  x,y: light weight string references  (optional) parent,child: direct UUID references for efficient hierarchical queries(NOTE is child is defined then so is parent and vise versa) note: parent and child can ONLY ever be x or y

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child** | **str** |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**id** | **str** |  | 
**parent** | **str** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**x** | **str** |  | 
**y** | **str** |  | 

## Example

```python
from pieces_os_client.models.flattened_workstream_summary_to_workstream_summary_association import FlattenedWorkstreamSummaryToWorkstreamSummaryAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedWorkstreamSummaryToWorkstreamSummaryAssociation from a JSON string
flattened_workstream_summary_to_workstream_summary_association_instance = FlattenedWorkstreamSummaryToWorkstreamSummaryAssociation.from_json(json)
# print the JSON string representation of the object
print(FlattenedWorkstreamSummaryToWorkstreamSummaryAssociation.to_json())

# convert the object into a dict
flattened_workstream_summary_to_workstream_summary_association_dict = flattened_workstream_summary_to_workstream_summary_association_instance.to_dict()
# create an instance of FlattenedWorkstreamSummaryToWorkstreamSummaryAssociation from a dict
flattened_workstream_summary_to_workstream_summary_association_from_dict = FlattenedWorkstreamSummaryToWorkstreamSummaryAssociation.from_dict(flattened_workstream_summary_to_workstream_summary_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


