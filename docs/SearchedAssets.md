# SearchedAssets

This is a modle that will return fro mthe search endpoint that will just contain an array of assets!

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exact** | **float** | the number of exact results | 
**iterable** | [**List[SearchedAsset]**](SearchedAsset.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**suggested** | **float** | the number of fuzzy/suggested search results. | 

## Example

```python
from pieces_os_client.models.searched_assets import SearchedAssets

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedAssets from a JSON string
searched_assets_instance = SearchedAssets.from_json(json)
# print the JSON string representation of the object
print(SearchedAssets.to_json())

# convert the object into a dict
searched_assets_dict = searched_assets_instance.to_dict()
# create an instance of SearchedAssets from a dict
searched_assets_from_dict = SearchedAssets.from_dict(searched_assets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


