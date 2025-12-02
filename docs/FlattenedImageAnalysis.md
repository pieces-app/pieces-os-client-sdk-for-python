# FlattenedImageAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | **str** | this is a reference to our (parent)analysis | 
**id** | **str** |  | 
**ocr** | [**FlattenedOCRAnalysis**](FlattenedOCRAnalysis.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_image_analysis import FlattenedImageAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedImageAnalysis from a JSON string
flattened_image_analysis_instance = FlattenedImageAnalysis.from_json(json)
# print the JSON string representation of the object
print(FlattenedImageAnalysis.to_json())

# convert the object into a dict
flattened_image_analysis_dict = flattened_image_analysis_instance.to_dict()
# create an instance of FlattenedImageAnalysis from a dict
flattened_image_analysis_from_dict = FlattenedImageAnalysis.from_dict(flattened_image_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


