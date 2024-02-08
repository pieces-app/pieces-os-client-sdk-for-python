# SegmentedTechnicalLanguage

This is the output model for '/machine_learning/text/technical_language/parsers/segmentation'  This will have an iterable of the segmented Technical language text/code

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[SegmentedTechnicalLanguageFragment]**](SegmentedTechnicalLanguageFragment.md) |  | 

## Example

```python
from openapi_client.models.segmented_technical_language import SegmentedTechnicalLanguage

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentedTechnicalLanguage from a JSON string
segmented_technical_language_instance = SegmentedTechnicalLanguage.from_json(json)
# print the JSON string representation of the object
print SegmentedTechnicalLanguage.to_json()

# convert the object into a dict
segmented_technical_language_dict = segmented_technical_language_instance.to_dict()
# create an instance of SegmentedTechnicalLanguage from a dict
segmented_technical_language_form_dict = segmented_technical_language.from_dict(segmented_technical_language_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


