# WorkstreamPatternEngineVisionEventTextualValue

note: we could add a summarize property. TODO: might need an extracted bool to say to aggregate the extracted

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extracted** | [**TextuallyExtractedMaterial**](TextuallyExtractedMaterial.md) |  | [optional] 
**ocr** | [**TransferableString**](TransferableString.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_pattern_engine_vision_event_textual_value import WorkstreamPatternEngineVisionEventTextualValue

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamPatternEngineVisionEventTextualValue from a JSON string
workstream_pattern_engine_vision_event_textual_value_instance = WorkstreamPatternEngineVisionEventTextualValue.from_json(json)
# print the JSON string representation of the object
print WorkstreamPatternEngineVisionEventTextualValue.to_json()

# convert the object into a dict
workstream_pattern_engine_vision_event_textual_value_dict = workstream_pattern_engine_vision_event_textual_value_instance.to_dict()
# create an instance of WorkstreamPatternEngineVisionEventTextualValue from a dict
workstream_pattern_engine_vision_event_textual_value_from_dict = WorkstreamPatternEngineVisionEventTextualValue.from_dict(workstream_pattern_engine_vision_event_textual_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


