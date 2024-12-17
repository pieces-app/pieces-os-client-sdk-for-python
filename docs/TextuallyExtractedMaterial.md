# TextuallyExtractedMaterial

This is an extraction, this was a person/website/anchor that was extracted  this will return the text location where this was found within the extraction.  as well return the material itself that was extracted.  Note: - seeds: will only be extracted people if provided, because the website/anchors will be created if extracted. - basically only thing that is different about the extracted people, if that if we extract a person that was not already saved,   then we will not save them, however if there are related people then we will add them as well.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**match** | [**TextLocation**](TextLocation.md) |  | 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 
**anchors** | [**FlattenedAnchors**](FlattenedAnchors.md) |  | [optional] 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**seeds** | [**Seeds**](Seeds.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.textually_extracted_material import TextuallyExtractedMaterial

# TODO update the JSON string below
json = "{}"
# create an instance of TextuallyExtractedMaterial from a JSON string
textually_extracted_material_instance = TextuallyExtractedMaterial.from_json(json)
# print the JSON string representation of the object
print TextuallyExtractedMaterial.to_json()

# convert the object into a dict
textually_extracted_material_dict = textually_extracted_material_instance.to_dict()
# create an instance of TextuallyExtractedMaterial from a dict
textually_extracted_material_from_dict = TextuallyExtractedMaterial.from_dict(textually_extracted_material_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


