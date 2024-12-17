# SearchedAnchor

This is used for the Anchors searching endpoint.  anchor here is only provided if transferables are set to true.  temporal: if this is provided this means that their material matched the input via a timestamp.  TODO will want to consider returning related materials to this material potentially both associated/ and not associated materials ie suggestion: WorkstreamSuggestions  note: if we match a specific anchorPoint we will provide this as well.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**anchor** | [**Anchor**](Anchor.md) |  | [optional] 
**points** | [**SearchedAnchorPoints**](SearchedAnchorPoints.md) |  | [optional] 
**exact** | **bool** |  | 
**similarity** | **float** |  | 
**temporal** | **bool** |  | [optional] 
**identifier** | **str** | This is the uuid of the anchor. | 

## Example

```python
from pieces_os_client.models.searched_anchor import SearchedAnchor

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedAnchor from a JSON string
searched_anchor_instance = SearchedAnchor.from_json(json)
# print the JSON string representation of the object
print SearchedAnchor.to_json()

# convert the object into a dict
searched_anchor_dict = searched_anchor_instance.to_dict()
# create an instance of SearchedAnchor from a dict
searched_anchor_from_dict = SearchedAnchor.from_dict(searched_anchor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


