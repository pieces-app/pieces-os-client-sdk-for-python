# FlattenedHint

This is the flattened version of a hint. Ensure that you DO NOT reference the Asset here as you can create an infinite loop within the packaging.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**id** | **str** |  | 
**mechanisms** | [**Dict[str, MechanismEnum]**](MechanismEnum.md) | This is a Map&lt;String, MechanismEnum&gt; where the the key is an asset id. | [optional] 
**model** | [**ReferencedModel**](ReferencedModel.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**text** | **str** | This is the text of the hint. | 
**type** | [**HintTypeEnum**](HintTypeEnum.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 

## Example

```python
from pieces_os_client.models.flattened_hint import FlattenedHint

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedHint from a JSON string
flattened_hint_instance = FlattenedHint.from_json(json)
# print the JSON string representation of the object
print(FlattenedHint.to_json())

# convert the object into a dict
flattened_hint_dict = flattened_hint_instance.to_dict()
# create an instance of FlattenedHint from a dict
flattened_hint_from_dict = FlattenedHint.from_dict(flattened_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


