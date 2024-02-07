# SearchedAsset

This is a modle that will represent a searched asset!

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**asset** | [**Asset**](Asset.md) |  | [optional] 
**exact** | **bool** |  | 
**score** | **float** |  | 
**match** | [**SearchedMatchEnum**](SearchedMatchEnum.md) |  | 
**identifier** | **str** | This is the uuid of the asset. | 
**pseudo** | **bool** | If this is a pseudo asset that was also returned. | [optional] 

## Example

```python
from openapi_client.models.searched_asset import SearchedAsset

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedAsset from a JSON string
searched_asset_instance = SearchedAsset.from_json(json)
# print the JSON string representation of the object
print SearchedAsset.to_json()

# convert the object into a dict
searched_asset_dict = searched_asset_instance.to_dict()
# create an instance of SearchedAsset from a dict
searched_asset_form_dict = searched_asset.from_dict(searched_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


