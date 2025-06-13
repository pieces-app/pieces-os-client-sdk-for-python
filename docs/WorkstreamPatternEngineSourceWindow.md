# WorkstreamPatternEngineSourceWindow

This is the source window for the workstream pattern engine  NOTE: website <> source window displays a many to many relationship, however is a 1 to 1 relationship with logic built in to ensure that this remains a 1 to one relationship. Please take a look at the the workstreamEvent creation(specifically when creating a website <> source window relationship), as well as the associate for a website <> a source window, This will ensure that we only ever have a single website, this will update the website if the time stamp if we are seeing the website again and as well update the source windows name as well if this is different so that is is only ever possible to have a website<>sourceWindow where a website can only ever have 1 source window.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** | The id of the source window | 
**name** | **str** | The name of the source window | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**score** | [**Score**](Score.md) |  | [optional] 
**workstream_events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 
**tags** | [**FlattenedTags**](FlattenedTags.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_pattern_engine_source_window import WorkstreamPatternEngineSourceWindow

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamPatternEngineSourceWindow from a JSON string
workstream_pattern_engine_source_window_instance = WorkstreamPatternEngineSourceWindow.from_json(json)
# print the JSON string representation of the object
print WorkstreamPatternEngineSourceWindow.to_json()

# convert the object into a dict
workstream_pattern_engine_source_window_dict = workstream_pattern_engine_source_window_instance.to_dict()
# create an instance of WorkstreamPatternEngineSourceWindow from a dict
workstream_pattern_engine_source_window_from_dict = WorkstreamPatternEngineSourceWindow.from_dict(workstream_pattern_engine_source_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


