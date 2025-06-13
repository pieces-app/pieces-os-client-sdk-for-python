# ModelContextProtocolSchemaVersion

This is a singular schema version for MCP

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**version** | **str** |  | 
**entry_endpoint** | **str** | this is the endpoint that the use should use to configure the server. | 

## Example

```python
from pieces_os_client.models.model_context_protocol_schema_version import ModelContextProtocolSchemaVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContextProtocolSchemaVersion from a JSON string
model_context_protocol_schema_version_instance = ModelContextProtocolSchemaVersion.from_json(json)
# print the JSON string representation of the object
print ModelContextProtocolSchemaVersion.to_json()

# convert the object into a dict
model_context_protocol_schema_version_dict = model_context_protocol_schema_version_instance.to_dict()
# create an instance of ModelContextProtocolSchemaVersion from a dict
model_context_protocol_schema_version_from_dict = ModelContextProtocolSchemaVersion.from_dict(model_context_protocol_schema_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


