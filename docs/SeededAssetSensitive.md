# SeededAssetSensitive

This is the seededAssetSensitive, this does not have an id yet as we will add it on the server side.  can optionally pass in our mechanism here, as the default will be manual unless specified.  This is different that hte SeededSensitive as this is pre-before the asset has been created.(but added when the asset is created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**SensitiveCategoryEnum**](SensitiveCategoryEnum.md) |  | 
**description** | **str** |  | 
**mechanism** | [**MechanismEnum**](MechanismEnum.md) |  | [optional] 
**metadata** | [**SensitiveMetadata**](SensitiveMetadata.md) |  | [optional] 
**name** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**severity** | [**SensitiveSeverityEnum**](SensitiveSeverityEnum.md) |  | 
**text** | **str** | this is the string representative of the sensative piece of data. | 

## Example

```python
from pieces_os_client.models.seeded_asset_sensitive import SeededAssetSensitive

# TODO update the JSON string below
json = "{}"
# create an instance of SeededAssetSensitive from a JSON string
seeded_asset_sensitive_instance = SeededAssetSensitive.from_json(json)
# print the JSON string representation of the object
print(SeededAssetSensitive.to_json())

# convert the object into a dict
seeded_asset_sensitive_dict = seeded_asset_sensitive_instance.to_dict()
# create an instance of SeededAssetSensitive from a dict
seeded_asset_sensitive_from_dict = SeededAssetSensitive.from_dict(seeded_asset_sensitive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


