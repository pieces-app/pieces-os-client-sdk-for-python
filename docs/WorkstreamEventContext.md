# WorkstreamEventContext

This is a free form data object that will enable additional data to be passed into SeededWorkstreamEvent, that corresponds to the event on the WorkstreamEvent.  This is a WIP object.  Need to think if we want to do something like raw:string (that is just a jsonObject) that is stringified, or if we add specific bits of data that we want. and specific fields for each event.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**ide** | [**WorkstreamEventTriggerContextIDE**](WorkstreamEventTriggerContextIDE.md) |  | [optional] 
**browser** | [**WorkstreamEventTriggerContextBrowser**](WorkstreamEventTriggerContextBrowser.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_event_context import WorkstreamEventContext

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamEventContext from a JSON string
workstream_event_context_instance = WorkstreamEventContext.from_json(json)
# print the JSON string representation of the object
print WorkstreamEventContext.to_json()

# convert the object into a dict
workstream_event_context_dict = workstream_event_context_instance.to_dict()
# create an instance of WorkstreamEventContext from a dict
workstream_event_context_from_dict = WorkstreamEventContext.from_dict(workstream_event_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


