# FlattenedShare

This is a dag safe version of the Share.  if user is undefined && access is public then we have an asset that is publicly available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**AccessEnum**](AccessEnum.md) |  | 
**accessors** | [**Accessors**](Accessors.md) |  | 
**asset** | **str** | this is the asset id on the flattened share. | [optional] 
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**distributions** | [**FlattenedDistributions**](FlattenedDistributions.md) |  | [optional] 
**id** | **str** | This references the share it self. | 
**link** | **str** | this is the prebuilt link. | 
**name** | **str** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**short** | **str** | This is a shortened version of our uuid. | 
**user** | **str** | this is the uuid of the user that the share is created for. | [optional] 

## Example

```python
from pieces_os_client.models.flattened_share import FlattenedShare

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedShare from a JSON string
flattened_share_instance = FlattenedShare.from_json(json)
# print the JSON string representation of the object
print(FlattenedShare.to_json())

# convert the object into a dict
flattened_share_dict = flattened_share_instance.to_dict()
# create an instance of FlattenedShare from a dict
flattened_share_from_dict = FlattenedShare.from_dict(flattened_share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


