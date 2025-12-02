# WorkstreamPatternEngineVisionEventsMetadata

This is specific model that will return the size of the WPE in bytes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes** | [**ByteDescriptor**](ByteDescriptor.md) |  | 
**newest** | [**WorkstreamPatternEngineVisionEvent**](WorkstreamPatternEngineVisionEvent.md) |  | [optional] 
**oldest** | [**WorkstreamPatternEngineVisionEvent**](WorkstreamPatternEngineVisionEvent.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**total** | **int** | This is the total number of events. | 

## Example

```python
from pieces_os_client.models.workstream_pattern_engine_vision_events_metadata import WorkstreamPatternEngineVisionEventsMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamPatternEngineVisionEventsMetadata from a JSON string
workstream_pattern_engine_vision_events_metadata_instance = WorkstreamPatternEngineVisionEventsMetadata.from_json(json)
# print the JSON string representation of the object
print(WorkstreamPatternEngineVisionEventsMetadata.to_json())

# convert the object into a dict
workstream_pattern_engine_vision_events_metadata_dict = workstream_pattern_engine_vision_events_metadata_instance.to_dict()
# create an instance of WorkstreamPatternEngineVisionEventsMetadata from a dict
workstream_pattern_engine_vision_events_metadata_from_dict = WorkstreamPatternEngineVisionEventsMetadata.from_dict(workstream_pattern_engine_vision_events_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


