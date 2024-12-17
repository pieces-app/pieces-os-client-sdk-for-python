# WorkstreamEvent

This is a Shadow Activity event:  This is used to for 2 collections the internal Shadow Activity collection and the Shadow Activity Collection.  The Internal Shadow Activity will me just a massive growing and shrinkling persisted list activity event that will endup getting rolled up into Workstream summaries. When we roll up the internalWorkstreamEvent events we will do a ton of filtering and only take the highly relevant events and turn them into WorkstreamEvent (these will be used to create a reference to the workstream summary, so we can know what event were used to generate the summary and vise versa).  A Shadow Activity model is a collection of a ton of small interactions with the plugins (copy/paste/file open/file close/tab changed/...etc events) that will also enable use to know what materials are being used to funnel them into our engine to show highly relevant data according to your given flow.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**Application**](Application.md) |  | 
**context** | [**WorkstreamEventContext**](WorkstreamEventContext.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**id** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**trigger** | [**WorkstreamEventTrigger**](WorkstreamEventTrigger.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 

## Example

```python
from pieces_os_client.models.workstream_event import WorkstreamEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamEvent from a JSON string
workstream_event_instance = WorkstreamEvent.from_json(json)
# print the JSON string representation of the object
print WorkstreamEvent.to_json()

# convert the object into a dict
workstream_event_dict = workstream_event_instance.to_dict()
# create an instance of WorkstreamEvent from a dict
workstream_event_from_dict = WorkstreamEvent.from_dict(workstream_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


