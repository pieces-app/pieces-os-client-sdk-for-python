# LanguageServerProtocol

TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**diagnostics** | [**LanguageServerProtocolDiagnostics**](LanguageServerProtocolDiagnostics.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.language_server_protocol import LanguageServerProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageServerProtocol from a JSON string
language_server_protocol_instance = LanguageServerProtocol.from_json(json)
# print the JSON string representation of the object
print LanguageServerProtocol.to_json()

# convert the object into a dict
language_server_protocol_dict = language_server_protocol_instance.to_dict()
# create an instance of LanguageServerProtocol from a dict
language_server_protocol_form_dict = language_server_protocol.from_dict(language_server_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


