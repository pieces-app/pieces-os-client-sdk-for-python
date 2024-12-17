# SeededWorkstreamEvent

This is a precreated version of a WorkstreamEvent event, this will be used ingested into PiecesOS and PiecesOS will do all the magic to transform this into relevant data show in the workstream feed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**application** | [**Application**](Application.md) |  | 
**trigger** | [**WorkstreamEventTrigger**](WorkstreamEventTrigger.md) |  | 
**context** | [**WorkstreamEventContext**](WorkstreamEventContext.md) |  | [optional] 
**summary** | [**ReferencedWorkstreamSummary**](ReferencedWorkstreamSummary.md) |  | [optional] 
**internal_identifier** | **str** | This is used to override the event identifier, if this was an event that was originally in the internal events collection. | [optional] 

## Example

```python
from pieces_os_client.models.seeded_workstream_event import SeededWorkstreamEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SeededWorkstreamEvent from a JSON string
seeded_workstream_event_instance = SeededWorkstreamEvent.from_json(json)
# print the JSON string representation of the object
print SeededWorkstreamEvent.to_json()

# convert the object into a dict
seeded_workstream_event_dict = seeded_workstream_event_instance.to_dict()
# create an instance of SeededWorkstreamEvent from a dict
seeded_workstream_event_from_dict = SeededWorkstreamEvent.from_dict(seeded_workstream_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


