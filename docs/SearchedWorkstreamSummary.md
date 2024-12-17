# SearchedWorkstreamSummary

This is used for the WorkstreamSummaries searching endpoint  WorkstreamSummary here is only provided if transferables are set to true.  temporal: if this is provided this means that their material matched the input via a timestamp.  TODO will want to consider returning related materials to this material potentially both associated/ and not associated materials ie suggestion: WorkstreamSuggestions  annotations: this is provided if we match a specific annotation on a WorkstreamSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**summary** | [**WorkstreamSummary**](WorkstreamSummary.md) |  | [optional] 
**annotations** | [**SearchedAnnotations**](SearchedAnnotations.md) |  | [optional] 
**exact** | **bool** |  | 
**similarity** | **float** |  | 
**temporal** | **bool** |  | [optional] 
**identifier** | **str** | This is the uuid of the WorkstreamSummary. | 

## Example

```python
from pieces_os_client.models.searched_workstream_summary import SearchedWorkstreamSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedWorkstreamSummary from a JSON string
searched_workstream_summary_instance = SearchedWorkstreamSummary.from_json(json)
# print the JSON string representation of the object
print SearchedWorkstreamSummary.to_json()

# convert the object into a dict
searched_workstream_summary_dict = searched_workstream_summary_instance.to_dict()
# create an instance of SearchedWorkstreamSummary from a dict
searched_workstream_summary_from_dict = SearchedWorkstreamSummary.from_dict(searched_workstream_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


