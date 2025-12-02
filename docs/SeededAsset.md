# SeededAsset

This is seed data that will be come an asset.  discovered: if set to true this seededAsset was discovered using one of our discovery endpoints.  pseudo: if this is an asset that a user did NOT explicitly save.  available: This is a model that is used within our '/assets/draft' endpoint that will emitt a seed with all the available format that one can generate based on the original seed that was passed in. ie if a png was passed in, we may  say that there is a text/code format available. If available formats is passed into the '/assets/create' we will short curcuit certain operations to speed up the process, for instance, if we determine that there is no text within this image then there is no sense in running ocr. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**Application**](Application.md) |  | 
**available** | [**AvailableFormats**](AvailableFormats.md) |  | [optional] 
**demo** | **bool** | This will let us know if this asset was generated as a &#39;demo&#39; snippet | [optional] 
**discovered** | **bool** |  | [optional] 
**enrichment** | [**SeededAssetEnrichment**](SeededAssetEnrichment.md) |  | [optional] 
**format** | [**SeededFormat**](SeededFormat.md) |  | 
**metadata** | [**SeededAssetMetadata**](SeededAssetMetadata.md) |  | [optional] 
**pseudo** | **bool** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_asset import SeededAsset

# TODO update the JSON string below
json = "{}"
# create an instance of SeededAsset from a JSON string
seeded_asset_instance = SeededAsset.from_json(json)
# print the JSON string representation of the object
print(SeededAsset.to_json())

# convert the object into a dict
seeded_asset_dict = seeded_asset_instance.to_dict()
# create an instance of SeededAsset from a dict
seeded_asset_from_dict = SeededAsset.from_dict(seeded_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


