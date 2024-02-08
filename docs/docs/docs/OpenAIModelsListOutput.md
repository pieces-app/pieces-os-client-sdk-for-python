# OpenAIModelsListOutput

This is the output model for the /open_ai/models/list endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**models** | [**SeededModels**](SeededModels.md) |  | 

## Example

```python
from openapi_client.models.open_ai_models_list_output import OpenAIModelsListOutput

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAIModelsListOutput from a JSON string
open_ai_models_list_output_instance = OpenAIModelsListOutput.from_json(json)
# print the JSON string representation of the object
print OpenAIModelsListOutput.to_json()

# convert the object into a dict
open_ai_models_list_output_dict = open_ai_models_list_output_instance.to_dict()
# create an instance of OpenAIModelsListOutput from a dict
open_ai_models_list_output_form_dict = open_ai_models_list_output.from_dict(open_ai_models_list_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


