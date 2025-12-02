# MigrationProgress

This is a model used to communicate the status of a migration in progress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_size** | **int** |  | 
**current_batch** | **int** |  | 
**current_stage** | **str** |  | 
**elapsed_milliseconds** | **int** |  | 
**estimated_time_remaining** | **int** |  | [optional] 
**percent_complete** | **float** |  | 
**processed_items** | **int** |  | 
**readable** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**status** | [**MigrationStatusEnum**](MigrationStatusEnum.md) |  | 
**total_items** | **int** |  | 

## Example

```python
from pieces_os_client.models.migration_progress import MigrationProgress

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationProgress from a JSON string
migration_progress_instance = MigrationProgress.from_json(json)
# print the JSON string representation of the object
print(MigrationProgress.to_json())

# convert the object into a dict
migration_progress_dict = migration_progress_instance.to_dict()
# create an instance of MigrationProgress from a dict
migration_progress_from_dict = MigrationProgress.from_dict(migration_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


