# AssetFilterTimestamp

if you want a range between you can use from && to.  if you want anything before, use to and NO from.  if you want anything after, use from and NO to.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**between** | **bool** |  | [optional] 
**var_from** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**to** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.asset_filter_timestamp import AssetFilterTimestamp

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFilterTimestamp from a JSON string
asset_filter_timestamp_instance = AssetFilterTimestamp.from_json(json)
# print the JSON string representation of the object
print AssetFilterTimestamp.to_json()

# convert the object into a dict
asset_filter_timestamp_dict = asset_filter_timestamp_instance.to_dict()
# create an instance of AssetFilterTimestamp from a dict
asset_filter_timestamp_from_dict = AssetFilterTimestamp.from_dict(asset_filter_timestamp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


