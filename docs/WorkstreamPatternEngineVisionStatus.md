# WorkstreamPatternEngineVisionStatus

activation: can be active for forever w/ continous true, or it can be activated for the next couple hours  deactivation: here can be deactivated for forever w/ continuous true, or it can be deactivated for the next couple hours  Note: one or the other will be set and both are nullable.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**activation** | [**AnonymousTemporalRange**](AnonymousTemporalRange.md) |  | [optional] 
**deactivation** | [**AnonymousTemporalRange**](AnonymousTemporalRange.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_pattern_engine_vision_status import WorkstreamPatternEngineVisionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamPatternEngineVisionStatus from a JSON string
workstream_pattern_engine_vision_status_instance = WorkstreamPatternEngineVisionStatus.from_json(json)
# print the JSON string representation of the object
print WorkstreamPatternEngineVisionStatus.to_json()

# convert the object into a dict
workstream_pattern_engine_vision_status_dict = workstream_pattern_engine_vision_status_instance.to_dict()
# create an instance of WorkstreamPatternEngineVisionStatus from a dict
workstream_pattern_engine_vision_status_from_dict = WorkstreamPatternEngineVisionStatus.from_dict(workstream_pattern_engine_vision_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


