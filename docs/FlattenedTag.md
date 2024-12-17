# FlattenedTag

This is a Flattened Version of a Tag.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**category** | [**TagCategoryEnum**](TagCategoryEnum.md) |  | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**id** | **str** |  | 
**interactions** | **int** | This is an optional value that will keep track of the number of times this has been interacted with. | [optional] 
**mechanisms** | [**Dict[str, MechanismEnum]**](MechanismEnum.md) | This is a Map&lt;String, MechanismEnum&gt; where the the key is an asset id. | [optional] 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**relationship** | [**Relationship**](Relationship.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**text** | **str** |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 

## Example

```python
from pieces_os_client.models.flattened_tag import FlattenedTag

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedTag from a JSON string
flattened_tag_instance = FlattenedTag.from_json(json)
# print the JSON string representation of the object
print FlattenedTag.to_json()

# convert the object into a dict
flattened_tag_dict = flattened_tag_instance.to_dict()
# create an instance of FlattenedTag from a dict
flattened_tag_from_dict = FlattenedTag.from_dict(flattened_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


