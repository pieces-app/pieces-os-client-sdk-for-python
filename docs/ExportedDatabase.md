# ExportedDatabase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | **List[int]** |  | [optional] 
**analyses** | **List[int]** |  | 
**anchor_points** | **List[int]** |  | [optional] 
**anchors** | **List[int]** |  | [optional] 
**annotations** | **List[int]** |  | [optional] 
**applications** | **List[int]** |  | 
**assets** | **List[int]** |  | 
**code_analyses** | **List[int]** |  | 
**conversation_messages** | **List[int]** |  | [optional] 
**conversations** | **List[int]** |  | [optional] 
**files** | **List[int]** |  | 
**format_metrics** | **List[int]** |  | 
**formats** | **List[int]** |  | 
**fragments** | **List[int]** |  | 
**hints** | **List[int]** |  | [optional] 
**image_analyses** | **List[int]** |  | 
**message_values** | [**ExportedDatabaseFormats**](ExportedDatabaseFormats.md) |  | [optional] 
**models** | **List[int]** |  | 
**ocr_analyses** | **List[int]** |  | 
**persons** | **List[int]** |  | 
**ranges** | **List[int]** |  | [optional] 
**relationships** | **List[int]** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**sensitives** | **List[int]** |  | 
**tags** | **List[int]** |  | 
**values** | [**ExportedDatabaseFormats**](ExportedDatabaseFormats.md) |  | 
**version** | **str** | This is the version of your os_server or cloud_server that we we exporting from. | 
**websites** | **List[int]** |  | 
**workstream_event_values** | [**ExportedDatabaseFormats**](ExportedDatabaseFormats.md) |  | [optional] 
**workstream_events** | **List[int]** |  | [optional] 
**workstream_pattern_engine_sources** | **List[int]** |  | [optional] 
**workstream_summaries** | **List[int]** |  | [optional] 

## Example

```python
from pieces_os_client.models.exported_database import ExportedDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of ExportedDatabase from a JSON string
exported_database_instance = ExportedDatabase.from_json(json)
# print the JSON string representation of the object
print(ExportedDatabase.to_json())

# convert the object into a dict
exported_database_dict = exported_database_instance.to_dict()
# create an instance of ExportedDatabase from a dict
exported_database_from_dict = ExportedDatabase.from_dict(exported_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


