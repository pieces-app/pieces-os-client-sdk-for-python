# WorkstreamPatternEngineVisionMetadata

This will return all the WPE vision specific metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**WorkstreamPatternEngineVisionEventsMetadata**](WorkstreamPatternEngineVisionEventsMetadata.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_pattern_engine_vision_metadata import WorkstreamPatternEngineVisionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamPatternEngineVisionMetadata from a JSON string
workstream_pattern_engine_vision_metadata_instance = WorkstreamPatternEngineVisionMetadata.from_json(json)
# print the JSON string representation of the object
print(WorkstreamPatternEngineVisionMetadata.to_json())

# convert the object into a dict
workstream_pattern_engine_vision_metadata_dict = workstream_pattern_engine_vision_metadata_instance.to_dict()
# create an instance of WorkstreamPatternEngineVisionMetadata from a dict
workstream_pattern_engine_vision_metadata_from_dict = WorkstreamPatternEngineVisionMetadata.from_dict(workstream_pattern_engine_vision_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


