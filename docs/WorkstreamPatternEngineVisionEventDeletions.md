# WorkstreamPatternEngineVisionEventDeletions

note: recomended to use the search option here(where you can pass in workstream. note: \"scope\" here will run a search with the given scope and then remove these events.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**FlattenedWorkstreamPatternEngineVisionEvents**](FlattenedWorkstreamPatternEngineVisionEvents.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**search_scope** | [**SearchInput**](SearchInput.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_pattern_engine_vision_event_deletions import WorkstreamPatternEngineVisionEventDeletions

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamPatternEngineVisionEventDeletions from a JSON string
workstream_pattern_engine_vision_event_deletions_instance = WorkstreamPatternEngineVisionEventDeletions.from_json(json)
# print the JSON string representation of the object
print WorkstreamPatternEngineVisionEventDeletions.to_json()

# convert the object into a dict
workstream_pattern_engine_vision_event_deletions_dict = workstream_pattern_engine_vision_event_deletions_instance.to_dict()
# create an instance of WorkstreamPatternEngineVisionEventDeletions from a dict
workstream_pattern_engine_vision_event_deletions_from_dict = WorkstreamPatternEngineVisionEventDeletions.from_dict(workstream_pattern_engine_vision_event_deletions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


