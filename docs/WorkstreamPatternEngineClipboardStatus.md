# WorkstreamPatternEngineClipboardStatus

Status information specific to the clipboard processor.  activation: Can be active continuously or for a specific duration deactivation: Can be deactivated continuously or for a specific duration  Note: Either activation or deactivation will be set, both are nullable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation** | [**AnonymousTemporalRange**](AnonymousTemporalRange.md) |  | [optional] 
**deactivation** | [**AnonymousTemporalRange**](AnonymousTemporalRange.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_pattern_engine_clipboard_status import WorkstreamPatternEngineClipboardStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamPatternEngineClipboardStatus from a JSON string
workstream_pattern_engine_clipboard_status_instance = WorkstreamPatternEngineClipboardStatus.from_json(json)
# print the JSON string representation of the object
print(WorkstreamPatternEngineClipboardStatus.to_json())

# convert the object into a dict
workstream_pattern_engine_clipboard_status_dict = workstream_pattern_engine_clipboard_status_instance.to_dict()
# create an instance of WorkstreamPatternEngineClipboardStatus from a dict
workstream_pattern_engine_clipboard_status_from_dict = WorkstreamPatternEngineClipboardStatus.from_dict(workstream_pattern_engine_clipboard_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


