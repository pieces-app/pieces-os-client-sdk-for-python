# SearchedWorkstreamSummaries

This is the plural Model used to return many SearchedWorkstreamSummary.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[SearchedWorkstreamSummary]**](SearchedWorkstreamSummary.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_workstream_summaries import SearchedWorkstreamSummaries

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedWorkstreamSummaries from a JSON string
searched_workstream_summaries_instance = SearchedWorkstreamSummaries.from_json(json)
# print the JSON string representation of the object
print SearchedWorkstreamSummaries.to_json()

# convert the object into a dict
searched_workstream_summaries_dict = searched_workstream_summaries_instance.to_dict()
# create an instance of SearchedWorkstreamSummaries from a dict
searched_workstream_summaries_from_dict = SearchedWorkstreamSummaries.from_dict(searched_workstream_summaries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


