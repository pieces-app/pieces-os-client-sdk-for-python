# InstanceConfigurationAllowedModel

Represents a single allowed model with its unique identifier and optional usage notes.  unique: this is the unique model name used to identify the model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom** | **bool** | This will let us know if this is a custom, fine tuned model imported by the user, or is a custom model from an organization. | [optional] 
**foundation** | [**ModelFoundationEnum**](ModelFoundationEnum.md) |  | [optional] 
**max_tokens** | [**ModelMaxTokens**](ModelMaxTokens.md) |  | [optional] 
**name** | **str** | This is an Optional Name of the Model. | [optional] 
**provider** | [**ExternalMLProviderEnum**](ExternalMLProviderEnum.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**type** | [**ModelTypeEnum**](ModelTypeEnum.md) |  | [optional] 
**unique** | **str** | This is the unique model name used to identify the model. | 
**version** | **str** | this is a version of the model. | [optional] 

## Example

```python
from pieces_os_client.models.instance_configuration_allowed_model import InstanceConfigurationAllowedModel

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceConfigurationAllowedModel from a JSON string
instance_configuration_allowed_model_instance = InstanceConfigurationAllowedModel.from_json(json)
# print the JSON string representation of the object
print(InstanceConfigurationAllowedModel.to_json())

# convert the object into a dict
instance_configuration_allowed_model_dict = instance_configuration_allowed_model_instance.to_dict()
# create an instance of InstanceConfigurationAllowedModel from a dict
instance_configuration_allowed_model_from_dict = InstanceConfigurationAllowedModel.from_dict(instance_configuration_allowed_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


