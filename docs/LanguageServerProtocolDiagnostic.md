# LanguageServerProtocolDiagnostic

TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**range** | [**LanguageServerProtocolLocationRange**](LanguageServerProtocolLocationRange.md) |  | 
**severity** | [**LanguageServerProtocolSeverityEnum**](LanguageServerProtocolSeverityEnum.md) |  | [optional] 
**code** | [**LanguageServerProtocolCode**](LanguageServerProtocolCode.md) |  | [optional] 
**code_description** | [**LanguageServerProtocolCodeDescription**](LanguageServerProtocolCodeDescription.md) |  | [optional] 
**source** | **str** |  | [optional] 
**message** | **str** |  | 

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
language_server_protocol_diagnostic_form_dict = language_server_protocol_diagnostic.from_dict(language_server_protocol_diagnostic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


