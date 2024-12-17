# WorkstreamPatternEngineVisionCalibration

This model is used for the dimensions of the copilot/feed/xyz window.  if dimensions/captured are null this means we do not have the dimensions for this given window.  TODO: consider adding 5 markers here for the qr codes(ie location of these as wel) NOTE: will want to add type of calibration for this specific dimension(ie copilot/feed/xyz)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captured** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**dimensions** | [**WindowDimensions**](WindowDimensions.md) |  | [optional] 
**foreground** | **str** | This is the name of the window(foreground window).(this will always be present) | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_pattern_engine_vision_calibration import WorkstreamPatternEngineVisionCalibration

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamPatternEngineVisionCalibration from a JSON string
workstream_pattern_engine_vision_calibration_instance = WorkstreamPatternEngineVisionCalibration.from_json(json)
# print the JSON string representation of the object
print WorkstreamPatternEngineVisionCalibration.to_json()

# convert the object into a dict
workstream_pattern_engine_vision_calibration_dict = workstream_pattern_engine_vision_calibration_instance.to_dict()
# create an instance of WorkstreamPatternEngineVisionCalibration from a dict
workstream_pattern_engine_vision_calibration_from_dict = WorkstreamPatternEngineVisionCalibration.from_dict(workstream_pattern_engine_vision_calibration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


