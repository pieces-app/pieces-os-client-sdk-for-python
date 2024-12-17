# ReferencedAnchorPoint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**reference** | [**FlattenedAnchorPoint**](FlattenedAnchorPoint.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.referenced_anchor_point import ReferencedAnchorPoint

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedAnchorPoint from a JSON string
referenced_anchor_point_instance = ReferencedAnchorPoint.from_json(json)
# print the JSON string representation of the object
print ReferencedAnchorPoint.to_json()

# convert the object into a dict
referenced_anchor_point_dict = referenced_anchor_point_instance.to_dict()
# create an instance of ReferencedAnchorPoint from a dict
referenced_anchor_point_from_dict = ReferencedAnchorPoint.from_dict(referenced_anchor_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


