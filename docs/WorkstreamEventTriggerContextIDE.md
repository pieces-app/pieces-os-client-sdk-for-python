# WorkstreamEventTriggerContextIDE

This is the given context for an IDE.  tabs: this here refers to the tabs w/in the IDE.  Modules here are the given repositories  Name: this is the name of a workspace, but not required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modules** | [**ProjectModules**](ProjectModules.md) |  | [optional] 
**name** | **str** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**tabs** | [**IDETabs**](IDETabs.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_event_trigger_context_ide import WorkstreamEventTriggerContextIDE

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamEventTriggerContextIDE from a JSON string
workstream_event_trigger_context_ide_instance = WorkstreamEventTriggerContextIDE.from_json(json)
# print the JSON string representation of the object
print(WorkstreamEventTriggerContextIDE.to_json())

# convert the object into a dict
workstream_event_trigger_context_ide_dict = workstream_event_trigger_context_ide_instance.to_dict()
# create an instance of WorkstreamEventTriggerContextIDE from a dict
workstream_event_trigger_context_ide_from_dict = WorkstreamEventTriggerContextIDE.from_dict(workstream_event_trigger_context_ide_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


