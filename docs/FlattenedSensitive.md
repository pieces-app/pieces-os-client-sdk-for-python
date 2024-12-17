# FlattenedSensitive

This is a dereferenced representation of a sensitive pieces of data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**ReferencedAsset**](ReferencedAsset.md) |  | 
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
from pieces_os_client.models.flattened_sensitive import FlattenedSensitive

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedSensitive from a JSON string
flattened_sensitive_instance = FlattenedSensitive.from_json(json)
# print the JSON string representation of the object
print FlattenedSensitive.to_json()

# convert the object into a dict
flattened_sensitive_dict = flattened_sensitive_instance.to_dict()
# create an instance of FlattenedSensitive from a dict
flattened_sensitive_from_dict = FlattenedSensitive.from_dict(flattened_sensitive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


