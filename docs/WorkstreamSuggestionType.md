# WorkstreamSuggestionType

This is used to map the types of the iterable to given booleans of their respective material types

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **bool** |  | [optional] 
**summary** | **bool** |  | [optional] 
**asset** | **bool** |  | [optional] 
**tag** | **bool** |  | [optional] 
**website** | **bool** |  | [optional] 
**anchor** | **bool** |  | [optional] 
**conversation** | **bool** |  | [optional] 
**person** | **bool** |  | [optional] 
**seed** | **bool** |  | [optional] 
**seeds** | **bool** |  | [optional] 
**summaries** | **bool** |  | [optional] 
**assets** | **bool** |  | [optional] 
**tags** | **bool** |  | [optional] 
**websites** | **bool** |  | [optional] 
**anchors** | **bool** |  | [optional] 
**conversations** | **bool** |  | [optional] 
**persons** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_suggestion_type import WorkstreamSuggestionType

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSuggestionType from a JSON string
workstream_suggestion_type_instance = WorkstreamSuggestionType.from_json(json)
# print the JSON string representation of the object
print WorkstreamSuggestionType.to_json()

# convert the object into a dict
workstream_suggestion_type_dict = workstream_suggestion_type_instance.to_dict()
# create an instance of WorkstreamSuggestionType from a dict
workstream_suggestion_type_from_dict = WorkstreamSuggestionType.from_dict(workstream_suggestion_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


