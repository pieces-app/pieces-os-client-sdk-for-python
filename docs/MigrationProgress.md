# MigrationProgress

This is a model used to communicate the status of a migration in progress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**total_items** | **int** |  | 
**processed_items** | **int** |  | 
**current_batch** | **int** |  | 
**batch_size** | **int** |  | 
**percent_complete** | **float** |  | 
**elapsed_milliseconds** | **int** |  | 
**current_stage** | **str** |  | 
**readable** | **str** |  | 
**estimated_time_remaining** | **int** |  | [optional] 
**status** | [**MigrationStatusEnum**](MigrationStatusEnum.md) |  | 

## Example

```python
from pieces_os_client.models.migration_progress import MigrationProgress

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationProgress from a JSON string
migration_progress_instance = MigrationProgress.from_json(json)
# print the JSON string representation of the object
print MigrationProgress.to_json()

# convert the object into a dict
migration_progress_dict = migration_progress_instance.to_dict()
# create an instance of MigrationProgress from a dict
migration_progress_from_dict = MigrationProgress.from_dict(migration_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


