# Hint

This is a hint that is attached to an asset, used for suggested_queries, and hints given via the qgpt flow.

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
from pieces_os_client.models.hint import Hint

# TODO update the JSON string below
json = "{}"
# create an instance of Hint from a JSON string
hint_instance = Hint.from_json(json)
# print the JSON string representation of the object
print Hint.to_json()

# convert the object into a dict
hint_dict = hint_instance.to_dict()
# create an instance of Hint from a dict
hint_from_dict = Hint.from_dict(hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


