# AssetFilters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[AssetFilter]**](AssetFilter.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**type** | [**FilterOperationTypeEnum**](FilterOperationTypeEnum.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.asset_filters import AssetFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFilters from a JSON string
asset_filters_instance = AssetFilters.from_json(json)
# print the JSON string representation of the object
print AssetFilters.to_json()

# convert the object into a dict
asset_filters_dict = asset_filters_instance.to_dict()
# create an instance of AssetFilters from a dict
asset_filters_from_dict = AssetFilters.from_dict(asset_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


