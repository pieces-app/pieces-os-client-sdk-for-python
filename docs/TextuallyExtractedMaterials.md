# TextuallyExtractedMaterials

This is a plural of an Extraction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[TextuallyExtractedMaterial]**](TextuallyExtractedMaterial.md) |  | 

## Example

```python
from pieces_os_client.models.textually_extracted_materials import TextuallyExtractedMaterials

# TODO update the JSON string below
json = "{}"
# create an instance of TextuallyExtractedMaterials from a JSON string
textually_extracted_materials_instance = TextuallyExtractedMaterials.from_json(json)
# print the JSON string representation of the object
print TextuallyExtractedMaterials.to_json()

# convert the object into a dict
textually_extracted_materials_dict = textually_extracted_materials_instance.to_dict()
# create an instance of TextuallyExtractedMaterials from a dict
textually_extracted_materials_from_dict = TextuallyExtractedMaterials.from_dict(textually_extracted_materials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


