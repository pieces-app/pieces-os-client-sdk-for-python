# SegmentedTechnicalLanguageFragment

This is the output iterable model for '/machine_learning/text/technical_language/parsers/segmentation'  specific is optional here, however you can pass in classify: true to get the specific classificaiton in the case the generic is code.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**generic** | [**ClassificationGenericEnum**](ClassificationGenericEnum.md) |  | 
**specific** | [**ClassificationSpecificEnum**](ClassificationSpecificEnum.md) |  | [optional] 
**fragment** | [**FragmentFormat**](FragmentFormat.md) |  | 

## Example

```python
from openapi_client.models.segmented_technical_language_fragment import SegmentedTechnicalLanguageFragment

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentedTechnicalLanguageFragment from a JSON string
segmented_technical_language_fragment_instance = SegmentedTechnicalLanguageFragment.from_json(json)
# print the JSON string representation of the object
print SegmentedTechnicalLanguageFragment.to_json()

# convert the object into a dict
segmented_technical_language_fragment_dict = segmented_technical_language_fragment_instance.to_dict()
# create an instance of SegmentedTechnicalLanguageFragment from a dict
segmented_technical_language_fragment_form_dict = segmented_technical_language_fragment.from_dict(segmented_technical_language_fragment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


