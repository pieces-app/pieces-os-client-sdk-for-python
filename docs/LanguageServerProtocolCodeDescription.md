# LanguageServerProtocolCodeDescription

modeled off of (https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#codeDescription)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.language_server_protocol_code_description import LanguageServerProtocolCodeDescription

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageServerProtocolCodeDescription from a JSON string
language_server_protocol_code_description_instance = LanguageServerProtocolCodeDescription.from_json(json)
# print the JSON string representation of the object
print(LanguageServerProtocolCodeDescription.to_json())

# convert the object into a dict
language_server_protocol_code_description_dict = language_server_protocol_code_description_instance.to_dict()
# create an instance of LanguageServerProtocolCodeDescription from a dict
language_server_protocol_code_description_from_dict = LanguageServerProtocolCodeDescription.from_dict(language_server_protocol_code_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


