# SearchedAnchorPoints

This is the plural Model used to return many SearchedAnchorPoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[SearchedAnchorPoint]**](SearchedAnchorPoint.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_anchor_points import SearchedAnchorPoints

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedAnchorPoints from a JSON string
searched_anchor_points_instance = SearchedAnchorPoints.from_json(json)
# print the JSON string representation of the object
print(SearchedAnchorPoints.to_json())

# convert the object into a dict
searched_anchor_points_dict = searched_anchor_points_instance.to_dict()
# create an instance of SearchedAnchorPoints from a dict
searched_anchor_points_from_dict = SearchedAnchorPoints.from_dict(searched_anchor_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


