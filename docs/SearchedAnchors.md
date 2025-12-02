# SearchedAnchors

This is the plural Model used to return many SearchedAnchor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[SearchedAnchor]**](SearchedAnchor.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_anchors import SearchedAnchors

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedAnchors from a JSON string
searched_anchors_instance = SearchedAnchors.from_json(json)
# print the JSON string representation of the object
print(SearchedAnchors.to_json())

# convert the object into a dict
searched_anchors_dict = searched_anchors_instance.to_dict()
# create an instance of SearchedAnchors from a dict
searched_anchors_from_dict = SearchedAnchors.from_dict(searched_anchors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


