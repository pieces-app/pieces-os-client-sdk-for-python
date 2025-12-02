# Sensitive

This is a fully referenced representation of a sensitive pieces of data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**FlattenedAsset**](FlattenedAsset.md) |  | 
**category** | [**SensitiveCategoryEnum**](SensitiveCategoryEnum.md) |  | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**description** | **str** |  | 
**id** | **str** |  | 
**interactions** | **int** | This is an optional value that will keep track of the number of times this has been interacted with. | [optional] 
**mechanism** | [**MechanismEnum**](MechanismEnum.md) |  | 
**metadata** | [**SensitiveMetadata**](SensitiveMetadata.md) |  | [optional] 
**name** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**severity** | [**SensitiveSeverityEnum**](SensitiveSeverityEnum.md) |  | 
**text** | **str** |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 

## Example

```python
from pieces_os_client.models.sensitive import Sensitive

# TODO update the JSON string below
json = "{}"
# create an instance of Sensitive from a JSON string
sensitive_instance = Sensitive.from_json(json)
# print the JSON string representation of the object
print(Sensitive.to_json())

# convert the object into a dict
sensitive_dict = sensitive_instance.to_dict()
# create an instance of Sensitive from a dict
sensitive_from_dict = Sensitive.from_dict(sensitive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


