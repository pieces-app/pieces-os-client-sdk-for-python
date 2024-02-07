# ExportedDatabaseFormats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[ExportedDatabaseFormat]**](ExportedDatabaseFormat.md) |  | 

## Example

```python
from openapi_client.models.exported_database_formats import ExportedDatabaseFormats

# TODO update the JSON string below
json = "{}"
# create an instance of ExportedDatabaseFormats from a JSON string
exported_database_formats_instance = ExportedDatabaseFormats.from_json(json)
# print the JSON string representation of the object
print ExportedDatabaseFormats.to_json()

# convert the object into a dict
exported_database_formats_dict = exported_database_formats_instance.to_dict()
# create an instance of ExportedDatabaseFormats from a dict
exported_database_formats_form_dict = exported_database_formats.from_dict(exported_database_formats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


