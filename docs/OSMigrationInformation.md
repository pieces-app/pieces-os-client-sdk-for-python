# OSMigrationInformation

Information about a specific migration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_collection** | **str** | Current collection being processed (optional) | [optional] 
**error_count** | **int** | Number of errors encountered (optional) | [optional] 
**estimated_time_remaining** | **int** | Estimated time remaining in seconds (optional) | [optional] 
**id** | **str** | Unique identifier for the migration | 
**name** | **str** | Name of the migration | 
**phase** | **str** | Current phase of the migration | 
**processed_documents** | **int** | Number of documents processed (optional) | [optional] 
**progress_percentage** | **float** | Progress percentage for this specific migration | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**status** | [**OSMigrationStatusEnum**](OSMigrationStatusEnum.md) |  | 
**total_documents** | **int** | Total number of documents to process (optional) | [optional] 

## Example

```python
from pieces_os_client.models.os_migration_information import OSMigrationInformation

# TODO update the JSON string below
json = "{}"
# create an instance of OSMigrationInformation from a JSON string
os_migration_information_instance = OSMigrationInformation.from_json(json)
# print the JSON string representation of the object
print(OSMigrationInformation.to_json())

# convert the object into a dict
os_migration_information_dict = os_migration_information_instance.to_dict()
# create an instance of OSMigrationInformation from a dict
os_migration_information_from_dict = OSMigrationInformation.from_dict(os_migration_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


