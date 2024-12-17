# WorkstreamPatternEngineSource

This is a specific model for a given WPE qdrant source.  note: application is optional b/c we may want a network sorce in the future TODO: think about adding an enum or something that will delimit the type of processor(vision/filewatcher/network/audio)  TODO: in the future we can add tabs/filepaths to this model here. TODO: Enum for source/processor ? i.e. WorkstreamPatternEngineProcessorEnum.VISION, WorkstreamPatternEngineProcessorEnum.NETWORK, WorkstreamPatternEngineProcessorEnum.FILE_IO, WorkstreamPatternEngineProcessorEnum.AUDIO, etc.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is the name of the window(foreground window)/application.(this will always be present) | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_pattern_engine_source import WorkstreamPatternEngineSource

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamPatternEngineSource from a JSON string
workstream_pattern_engine_source_instance = WorkstreamPatternEngineSource.from_json(json)
# print the JSON string representation of the object
print WorkstreamPatternEngineSource.to_json()

# convert the object into a dict
workstream_pattern_engine_source_dict = workstream_pattern_engine_source_instance.to_dict()
# create an instance of WorkstreamPatternEngineSource from a dict
workstream_pattern_engine_source_from_dict = WorkstreamPatternEngineSource.from_dict(workstream_pattern_engine_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


