# FlattenedAnchorPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | [**ReferencedAnchor**](ReferencedAnchor.md) |  | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**fullpath** | **str** | This is the text of the path. | 
**id** | **str** |  | 
**platform** | [**PlatformEnum**](PlatformEnum.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**verified** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_anchor_point import FlattenedAnchorPoint

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedAnchorPoint from a JSON string
flattened_anchor_point_instance = FlattenedAnchorPoint.from_json(json)
# print the JSON string representation of the object
print(FlattenedAnchorPoint.to_json())

# convert the object into a dict
flattened_anchor_point_dict = flattened_anchor_point_instance.to_dict()
# create an instance of FlattenedAnchorPoint from a dict
flattened_anchor_point_from_dict = FlattenedAnchorPoint.from_dict(flattened_anchor_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


