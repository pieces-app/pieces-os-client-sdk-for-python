# LanguageServerProtocolLocation

modeled after this (https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#location)  uri: is jsut a file path  range: here is the location of where this item is within the file.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**uri** | **str** |  | 
**range** | [**LanguageServerProtocolLocationRange**](LanguageServerProtocolLocationRange.md) |  | 

## Example

```python
from pieces_os_client.models.language_server_protocol_location import LanguageServerProtocolLocation

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageServerProtocolLocation from a JSON string
language_server_protocol_location_instance = LanguageServerProtocolLocation.from_json(json)
# print the JSON string representation of the object
print LanguageServerProtocolLocation.to_json()

# convert the object into a dict
language_server_protocol_location_dict = language_server_protocol_location_instance.to_dict()
# create an instance of LanguageServerProtocolLocation from a dict
language_server_protocol_location_from_dict = LanguageServerProtocolLocation.from_dict(language_server_protocol_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


