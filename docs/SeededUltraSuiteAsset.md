# SeededUltraSuiteAsset

A SeededUEAsset is the minimum data sent from UE required to create an asset within Pieces.  Fragment & file are both optional properties however we will throw an internal error if both fragment and file are passed through or if both are undefined.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**ext** | [**ClassificationSpecificEnum**](ClassificationSpecificEnum.md) |  | [optional] 
**format** | [**SeededFormat**](SeededFormat.md) |  | 
**name** | **str** | (optional) name is the name of the file | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_ultra_suite_asset import SeededUltraSuiteAsset

# TODO update the JSON string below
json = "{}"
# create an instance of SeededUltraSuiteAsset from a JSON string
seeded_ultra_suite_asset_instance = SeededUltraSuiteAsset.from_json(json)
# print the JSON string representation of the object
print SeededUltraSuiteAsset.to_json()

# convert the object into a dict
seeded_ultra_suite_asset_dict = seeded_ultra_suite_asset_instance.to_dict()
# create an instance of SeededUltraSuiteAsset from a dict
seeded_ultra_suite_asset_from_dict = SeededUltraSuiteAsset.from_dict(seeded_ultra_suite_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


