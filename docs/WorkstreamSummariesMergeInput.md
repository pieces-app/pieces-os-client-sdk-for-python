# WorkstreamSummariesMergeInput

Input model for merging multiple workstream summaries into a single new summary.  summaries: these are the summaries that we will be merging together. ranges: given a range / many ranges we will merge all the summaries in a given time tags:(if this is provided we will get all the summaries that have these tags) - consider using a vector search, and then matching the summaries that have these tags. query: (if this is provided we will get all the summaries that match the query(using vector search)) sources: (if this is provided we will get all the summaries that match the sources)  ** if all three are provided we will try our best to take into account all properties (time, topic(tags) and summaries)  how-to: - daily recap: provide a timerange, select a few of your summaries, and add a couple of topic (minimal information is just the summaries or the timeranges.) - topical merging: take the tags, run a vector search, get the tags that include summaries, use the summaries as context for the merging + the original topics that we merged on.   Note: - all summaries, tags, ranges used in the input / aggregated as context will be associated to the 'parent' / merged summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_hierarchical_type** | [**WorkstreamSummaryHierarchicalParentTypeEnum**](WorkstreamSummaryHierarchicalParentTypeEnum.md) |  | 
**query** | **str** | This is a query that will be used to filter the summaries. | [optional] 
**ranges** | [**FlattenedRanges**](FlattenedRanges.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**sources** | [**FlattenedIdentifiedWorkstreamPatternEngineSources**](FlattenedIdentifiedWorkstreamPatternEngineSources.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**tags** | [**FlattenedTags**](FlattenedTags.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_summaries_merge_input import WorkstreamSummariesMergeInput

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSummariesMergeInput from a JSON string
workstream_summaries_merge_input_instance = WorkstreamSummariesMergeInput.from_json(json)
# print the JSON string representation of the object
print(WorkstreamSummariesMergeInput.to_json())

# convert the object into a dict
workstream_summaries_merge_input_dict = workstream_summaries_merge_input_instance.to_dict()
# create an instance of WorkstreamSummariesMergeInput from a dict
workstream_summaries_merge_input_from_dict = WorkstreamSummariesMergeInput.from_dict(workstream_summaries_merge_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


