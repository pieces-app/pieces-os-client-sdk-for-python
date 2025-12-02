# WorkstreamEventTrigger

This is the specific event that represent the Shadow Activity ie the copy/paste ...xyz  NOTE: for native_clipboard, we will just use copy/paste bools(NOTE: paste is not support for now just copy.) so we will only be using copy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_enter** | **bool** |  | [optional] 
**application_leave** | **bool** |  | [optional] 
**application_switch** | **bool** |  | [optional] 
**check_in** | **bool** | this is a sort of check-in event(ie when ever your application is in the forground on there is an interaction) | [optional] 
**copy** | **bool** |  | [optional] 
**file_close** | **bool** |  | [optional] 
**file_open** | **bool** |  | [optional] 
**native_screenshot** | **bool** |  | [optional] 
**paste** | **bool** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**tab_close** | **bool** |  | [optional] 
**tab_enter** | **bool** |  | [optional] 
**tab_leave** | **bool** |  | [optional] 
**tab_open** | **bool** |  | [optional] 
**tab_switch** | **bool** |  | [optional] 
**url_changed** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_event_trigger import WorkstreamEventTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamEventTrigger from a JSON string
workstream_event_trigger_instance = WorkstreamEventTrigger.from_json(json)
# print the JSON string representation of the object
print(WorkstreamEventTrigger.to_json())

# convert the object into a dict
workstream_event_trigger_dict = workstream_event_trigger_instance.to_dict()
# create an instance of WorkstreamEventTrigger from a dict
workstream_event_trigger_from_dict = WorkstreamEventTrigger.from_dict(workstream_event_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


