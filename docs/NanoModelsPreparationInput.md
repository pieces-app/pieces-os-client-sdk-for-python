# NanoModelsPreparationInput

This is the input body for the /os/nano_models/prepare endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**tasks** | [**NanoModelsPreparationTasks**](NanoModelsPreparationTasks.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.nano_models_preparation_input import NanoModelsPreparationInput

# TODO update the JSON string below
json = "{}"
# create an instance of NanoModelsPreparationInput from a JSON string
nano_models_preparation_input_instance = NanoModelsPreparationInput.from_json(json)
# print the JSON string representation of the object
print(NanoModelsPreparationInput.to_json())

# convert the object into a dict
nano_models_preparation_input_dict = nano_models_preparation_input_instance.to_dict()
# create an instance of NanoModelsPreparationInput from a dict
nano_models_preparation_input_from_dict = NanoModelsPreparationInput.from_dict(nano_models_preparation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


