# SeededAnchorPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | **str** | Cannot create an AnchorPoint w/o a Anchor. | 
**fullpath** | **str** |  | 
**platform** | [**PlatformEnum**](PlatformEnum.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**type** | [**AnchorTypeEnum**](AnchorTypeEnum.md) |  | 
**watch** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_anchor_point import SeededAnchorPoint

# TODO update the JSON string below
json = "{}"
# create an instance of SeededAnchorPoint from a JSON string
seeded_anchor_point_instance = SeededAnchorPoint.from_json(json)
# print the JSON string representation of the object
print(SeededAnchorPoint.to_json())

# convert the object into a dict
seeded_anchor_point_dict = seeded_anchor_point_instance.to_dict()
# create an instance of SeededAnchorPoint from a dict
seeded_anchor_point_from_dict = SeededAnchorPoint.from_dict(seeded_anchor_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


