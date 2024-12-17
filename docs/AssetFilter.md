# AssetFilter

** in the future, consider adding an optional bool's called nextAnd, nextOr which will say that the next filter will be  AND behavor or OR behavior.  \"operations\": here is is an optional property to allow or behavior,(we will only allow 1 level deep of or's), if or is not passed in then it is just simply ignored. If or is passed in then we will be or'd together with the top level filter and considered extras. default behavior for operations is and, however yoour can specifiy OR operations as well.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | [**ClassificationSpecificEnum**](ClassificationSpecificEnum.md) |  | [optional] 
**created** | [**AssetFilterTimestamp**](AssetFilterTimestamp.md) |  | [optional] 
**operations** | [**AssetFilters**](AssetFilters.md) |  | [optional] 
**persons** | **List[str]** |  | [optional] 
**phrase** | [**AssetFilterPhrase**](AssetFilterPhrase.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**updated** | [**AssetFilterTimestamp**](AssetFilterTimestamp.md) |  | [optional] 
**websites** | **List[str]** |  | [optional] 

## Example

```python
from pieces_os_client.models.asset_filter import AssetFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFilter from a JSON string
asset_filter_instance = AssetFilter.from_json(json)
# print the JSON string representation of the object
print AssetFilter.to_json()

# convert the object into a dict
asset_filter_dict = asset_filter_instance.to_dict()
# create an instance of AssetFilter from a dict
asset_filter_from_dict = AssetFilter.from_dict(asset_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


