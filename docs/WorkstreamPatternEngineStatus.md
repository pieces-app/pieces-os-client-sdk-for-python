# WorkstreamPatternEngineStatus

This will return the status for the Workstream pettern engine, specifically the activation/deactivation status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clipboard** | [**WorkstreamPatternEngineClipboardStatus**](WorkstreamPatternEngineClipboardStatus.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**vision** | [**WorkstreamPatternEngineVisionStatus**](WorkstreamPatternEngineVisionStatus.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_pattern_engine_status import WorkstreamPatternEngineStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamPatternEngineStatus from a JSON string
workstream_pattern_engine_status_instance = WorkstreamPatternEngineStatus.from_json(json)
# print the JSON string representation of the object
print(WorkstreamPatternEngineStatus.to_json())

# convert the object into a dict
workstream_pattern_engine_status_dict = workstream_pattern_engine_status_instance.to_dict()
# create an instance of WorkstreamPatternEngineStatus from a dict
workstream_pattern_engine_status_from_dict = WorkstreamPatternEngineStatus.from_dict(workstream_pattern_engine_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


