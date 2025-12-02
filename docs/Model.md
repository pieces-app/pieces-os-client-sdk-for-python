# Model

This is a Machine Learning Model, that will give readable information about the Machine Learning Model Used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes** | [**ByteDescriptor**](ByteDescriptor.md) |  | [optional] 
**capabilities** | [**ModelCapabilities**](ModelCapabilities.md) |  | [optional] 
**cloud** | **bool** | This will inform the user if this was a model that is hosted in the cloud | 
**cpu** | **bool** | This is an optional bool that is optimized for CPU usage. | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**custom** | **bool** | This will let us know if this is a custom, fine tuned model imported by the user, or is a custom model from an organization. | [optional] 
**denied** | **bool** | This will let us know if this model is denied for use by the user. ONLY static Pieces default models can be denied. | [optional] 
**description** | **str** | An Optional Description of the model itself. | [optional] 
**downloaded** | **bool** | This is an optional bool to let us know if this model has been downloaded locally. | [optional] 
**downloading** | **bool** | This is a calculated property, that will say if this is currently downloading. | [optional] 
**foundation** | [**ModelFoundationEnum**](ModelFoundationEnum.md) |  | [optional] 
**id** | **str** | uuid  | 
**loaded** | **bool** | This is a boolean that represents if the model is loaded into memory.(this is not persisted, and is calculated on the fly.) | [optional] 
**max_tokens** | [**ModelMaxTokens**](ModelMaxTokens.md) |  | [optional] 
**name** | **str** | This is an Optional Name of the Model. | 
**organization** | [**ReferencedEntity**](ReferencedEntity.md) |  | [optional] 
**parameters** | **float** | This is the number of parameters in terms of billions. | [optional] 
**provider** | [**ExternalMLProviderEnum**](ExternalMLProviderEnum.md) |  | [optional] 
**quantization** | **str** | quantization is a string like: q8f16_0,  q4f16_1, etc... | [optional] 
**ram** | [**ByteDescriptor**](ByteDescriptor.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**type** | [**ModelTypeEnum**](ModelTypeEnum.md) |  | 
**unique** | **str** | This is the unique model name used to load the model. | [optional] 
**usage** | [**ModelUsageEnum**](ModelUsageEnum.md) |  | 
**version** | **str** | this is a version of the model. | 

## Example

```python
from pieces_os_client.models.model import Model

# TODO update the JSON string below
json = "{}"
# create an instance of Model from a JSON string
model_instance = Model.from_json(json)
# print the JSON string representation of the object
print(Model.to_json())

# convert the object into a dict
model_dict = model_instance.to_dict()
# create an instance of Model from a dict
model_from_dict = Model.from_dict(model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


