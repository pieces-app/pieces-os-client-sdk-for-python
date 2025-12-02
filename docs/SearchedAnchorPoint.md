# SearchedAnchorPoint

This is used for the AnchorPoints searching endpoint.  point here is only provided if transferables are set to true.  temporal: if this is provided this means that their material matched the input via a timestamp.  TODO will want to consider returning related materials to this material potentially both associated/ and not associated materials ie suggestion: WorkstreamSuggestions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exact** | **bool** |  | 
**identifier** | **str** | This is the uuid of the anchorPoint. | 
**point** | [**AnchorPoint**](AnchorPoint.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**similarity** | **float** |  | 
**temporal** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_anchor_point import SearchedAnchorPoint

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedAnchorPoint from a JSON string
searched_anchor_point_instance = SearchedAnchorPoint.from_json(json)
# print the JSON string representation of the object
print(SearchedAnchorPoint.to_json())

# convert the object into a dict
searched_anchor_point_dict = searched_anchor_point_instance.to_dict()
# create an instance of SearchedAnchorPoint from a dict
searched_anchor_point_from_dict = SearchedAnchorPoint.from_dict(searched_anchor_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


