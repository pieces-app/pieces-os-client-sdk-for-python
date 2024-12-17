# LanguageServerProtocolLocationRangePosition

modeled after this (https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#position)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character** | **int** |  | 
**line** | **int** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.language_server_protocol_location_range_position import LanguageServerProtocolLocationRangePosition

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageServerProtocolLocationRangePosition from a JSON string
language_server_protocol_location_range_position_instance = LanguageServerProtocolLocationRangePosition.from_json(json)
# print the JSON string representation of the object
print LanguageServerProtocolLocationRangePosition.to_json()

# convert the object into a dict
language_server_protocol_location_range_position_dict = language_server_protocol_location_range_position_instance.to_dict()
# create an instance of LanguageServerProtocolLocationRangePosition from a dict
language_server_protocol_location_range_position_from_dict = LanguageServerProtocolLocationRangePosition.from_dict(language_server_protocol_location_range_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


