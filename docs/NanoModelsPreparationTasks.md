# NanoModelsPreparationTasks

These are the tasks for the nanoModels prepare endpoint  NOTE: you can mix and match different tasks if true then we will load the models.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.nano_models_preparation_tasks import NanoModelsPreparationTasks

# TODO update the JSON string below
json = "{}"
# create an instance of NanoModelsPreparationTasks from a JSON string
nano_models_preparation_tasks_instance = NanoModelsPreparationTasks.from_json(json)
# print the JSON string representation of the object
print(NanoModelsPreparationTasks.to_json())

# convert the object into a dict
nano_models_preparation_tasks_dict = nano_models_preparation_tasks_instance.to_dict()
# create an instance of NanoModelsPreparationTasks from a dict
nano_models_preparation_tasks_from_dict = NanoModelsPreparationTasks.from_dict(nano_models_preparation_tasks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


