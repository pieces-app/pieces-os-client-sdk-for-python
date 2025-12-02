# AssetFilterPhrase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotation** | **bool** |  | [optional] 
**content** | **bool** |  | [optional] 
**options** | [**AssetFilterPhraseOptions**](AssetFilterPhraseOptions.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**title** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from pieces_os_client.models.asset_filter_phrase import AssetFilterPhrase

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFilterPhrase from a JSON string
asset_filter_phrase_instance = AssetFilterPhrase.from_json(json)
# print the JSON string representation of the object
print(AssetFilterPhrase.to_json())

# convert the object into a dict
asset_filter_phrase_dict = asset_filter_phrase_instance.to_dict()
# create an instance of AssetFilterPhrase from a dict
asset_filter_phrase_from_dict = AssetFilterPhrase.from_dict(asset_filter_phrase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


