# WorkstreamEventTriggerContextBrowser

This is the given context for the browser,  a client can pass through many of the same tab if they would like,  note: however please try to only side 3 unique website/anchors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**tabs** | [**BrowserTabs**](BrowserTabs.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_event_trigger_context_browser import WorkstreamEventTriggerContextBrowser

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamEventTriggerContextBrowser from a JSON string
workstream_event_trigger_context_browser_instance = WorkstreamEventTriggerContextBrowser.from_json(json)
# print the JSON string representation of the object
print WorkstreamEventTriggerContextBrowser.to_json()

# convert the object into a dict
workstream_event_trigger_context_browser_dict = workstream_event_trigger_context_browser_instance.to_dict()
# create an instance of WorkstreamEventTriggerContextBrowser from a dict
workstream_event_trigger_context_browser_from_dict = WorkstreamEventTriggerContextBrowser.from_dict(workstream_event_trigger_context_browser_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


