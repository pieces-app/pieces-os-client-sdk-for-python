# LanguageServerProtocolLocationRange

modeled after this (https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#range)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | [**LanguageServerProtocolLocationRangePosition**](LanguageServerProtocolLocationRangePosition.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**start** | [**LanguageServerProtocolLocationRangePosition**](LanguageServerProtocolLocationRangePosition.md) |  | 

## Example

```python
from pieces_os_client.models.language_server_protocol_location_range import LanguageServerProtocolLocationRange

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageServerProtocolLocationRange from a JSON string
language_server_protocol_location_range_instance = LanguageServerProtocolLocationRange.from_json(json)
# print the JSON string representation of the object
print(LanguageServerProtocolLocationRange.to_json())

# convert the object into a dict
language_server_protocol_location_range_dict = language_server_protocol_location_range_instance.to_dict()
# create an instance of LanguageServerProtocolLocationRange from a dict
language_server_protocol_location_range_from_dict = LanguageServerProtocolLocationRange.from_dict(language_server_protocol_location_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


