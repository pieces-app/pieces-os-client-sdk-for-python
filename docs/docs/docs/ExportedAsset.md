# ExportedAsset

This is a model for a minimum exported version of an asset.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | this is the title of the asset  | 
**description** | **str** | this is the description of the asset | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**raw** | [**FileFormat**](FileFormat.md) |  | 

## Example

```python
from openapi_client.models.exported_asset import ExportedAsset

# TODO update the JSON string below
json = "{}"
# create an instance of ExportedAsset from a JSON string
exported_asset_instance = ExportedAsset.from_json(json)
# print the JSON string representation of the object
print ExportedAsset.to_json()

# convert the object into a dict
exported_asset_dict = exported_asset_instance.to_dict()
# create an instance of ExportedAsset from a dict
exported_asset_form_dict = exported_asset.from_dict(exported_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


