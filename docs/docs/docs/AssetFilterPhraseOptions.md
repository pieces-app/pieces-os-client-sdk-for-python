# AssetFilterPhraseOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**annotation** | [**AnnotationTypeEnum**](AnnotationTypeEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.asset_filter_phrase_options import AssetFilterPhraseOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFilterPhraseOptions from a JSON string
asset_filter_phrase_options_instance = AssetFilterPhraseOptions.from_json(json)
# print the JSON string representation of the object
print AssetFilterPhraseOptions.to_json()

# convert the object into a dict
asset_filter_phrase_options_dict = asset_filter_phrase_options_instance.to_dict()
# create an instance of AssetFilterPhraseOptions from a dict
asset_filter_phrase_options_form_dict = asset_filter_phrase_options.from_dict(asset_filter_phrase_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


