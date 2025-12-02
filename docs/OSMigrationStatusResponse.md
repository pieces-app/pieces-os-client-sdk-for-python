# OSMigrationStatusResponse

Response class for migration status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_migrations** | [**List[OSMigrationInformation]**](OSMigrationInformation.md) | List of active migrations with their information | 
**overall_progress_percentage** | **float** | Overall progress percentage for all migrations | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**status** | [**OSMigrationStatusEnum**](OSMigrationStatusEnum.md) |  | 

## Example

```python
from pieces_os_client.models.os_migration_status_response import OSMigrationStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OSMigrationStatusResponse from a JSON string
os_migration_status_response_instance = OSMigrationStatusResponse.from_json(json)
# print the JSON string representation of the object
print(OSMigrationStatusResponse.to_json())

# convert the object into a dict
os_migration_status_response_dict = os_migration_status_response_instance.to_dict()
# create an instance of OSMigrationStatusResponse from a dict
os_migration_status_response_from_dict = OSMigrationStatusResponse.from_dict(os_migration_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


