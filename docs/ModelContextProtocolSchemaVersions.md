# ModelContextProtocolSchemaVersions

This is the request body that will return all the support schemas

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[ModelContextProtocolSchemaVersion]**](ModelContextProtocolSchemaVersion.md) | This is a singular version for MCP | 

## Example

```python
from pieces_os_client.models.model_context_protocol_schema_versions import ModelContextProtocolSchemaVersions

# TODO update the JSON string below
json = "{}"
# create an instance of ModelContextProtocolSchemaVersions from a JSON string
model_context_protocol_schema_versions_instance = ModelContextProtocolSchemaVersions.from_json(json)
# print the JSON string representation of the object
print ModelContextProtocolSchemaVersions.to_json()

# convert the object into a dict
model_context_protocol_schema_versions_dict = model_context_protocol_schema_versions_instance.to_dict()
# create an instance of ModelContextProtocolSchemaVersions from a dict
model_context_protocol_schema_versions_from_dict = ModelContextProtocolSchemaVersions.from_dict(model_context_protocol_schema_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


