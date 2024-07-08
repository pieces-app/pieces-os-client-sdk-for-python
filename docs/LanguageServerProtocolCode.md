# LanguageServerProtocolCode

NOTE: this can me a union type here.. (integer | string;) so we need to get a bit creative

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**code_integer** | **int** |  | [optional] 
**code_string** | **str** |  | [optional] 
**raw_json** | **Dict[str, str]** | This is a Map&lt;String, String&gt;, basically just a json object for additional data if int/string will not work | [optional] 

## Example

```python
from pieces_os_client.models.language_server_protocol_code import LanguageServerProtocolCode

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageServerProtocolCode from a JSON string
language_server_protocol_code_instance = LanguageServerProtocolCode.from_json(json)
# print the JSON string representation of the object
print LanguageServerProtocolCode.to_json()

# convert the object into a dict
language_server_protocol_code_dict = language_server_protocol_code_instance.to_dict()
# create an instance of LanguageServerProtocolCode from a dict
language_server_protocol_code_from_dict = LanguageServerProtocolCode.from_dict(language_server_protocol_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


