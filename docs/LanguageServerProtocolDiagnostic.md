# LanguageServerProtocolDiagnostic

TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**LanguageServerProtocolCode**](LanguageServerProtocolCode.md) |  | [optional] 
**code_description** | [**LanguageServerProtocolCodeDescription**](LanguageServerProtocolCodeDescription.md) |  | [optional] 
**message** | **str** |  | 
**range** | [**LanguageServerProtocolLocationRange**](LanguageServerProtocolLocationRange.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**severity** | [**LanguageServerProtocolSeverityEnum**](LanguageServerProtocolSeverityEnum.md) |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from pieces_os_client.models.language_server_protocol_diagnostic import LanguageServerProtocolDiagnostic

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageServerProtocolDiagnostic from a JSON string
language_server_protocol_diagnostic_instance = LanguageServerProtocolDiagnostic.from_json(json)
# print the JSON string representation of the object
print LanguageServerProtocolDiagnostic.to_json()

# convert the object into a dict
language_server_protocol_diagnostic_dict = language_server_protocol_diagnostic_instance.to_dict()
# create an instance of LanguageServerProtocolDiagnostic from a dict
language_server_protocol_diagnostic_from_dict = LanguageServerProtocolDiagnostic.from_dict(language_server_protocol_diagnostic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


