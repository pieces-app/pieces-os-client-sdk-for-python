# SearchedWorkstreamPatternEngineVisionEvent

This will return a list of the returned events.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**event** | [**WorkstreamPatternEngineVisionEvent**](WorkstreamPatternEngineVisionEvent.md) |  | [optional] 
**exact** | **bool** |  | [optional] 
**similarity** | **float** |  | [optional] 
**temporal** | **bool** |  | [optional] 
**application** | **str** |  | [optional] 
**identifier** | **str** | This is the uuid of the event. | 

## Example

```python
from pieces_os_client.models.searched_workstream_pattern_engine_vision_event import SearchedWorkstreamPatternEngineVisionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedWorkstreamPatternEngineVisionEvent from a JSON string
searched_workstream_pattern_engine_vision_event_instance = SearchedWorkstreamPatternEngineVisionEvent.from_json(json)
# print the JSON string representation of the object
print SearchedWorkstreamPatternEngineVisionEvent.to_json()

# convert the object into a dict
searched_workstream_pattern_engine_vision_event_dict = searched_workstream_pattern_engine_vision_event_instance.to_dict()
# create an instance of SearchedWorkstreamPatternEngineVisionEvent from a dict
searched_workstream_pattern_engine_vision_event_from_dict = SearchedWorkstreamPatternEngineVisionEvent.from_dict(searched_workstream_pattern_engine_vision_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


