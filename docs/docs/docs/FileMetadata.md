# FileMetadata

This is a model for metadata of a file!

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**name** | **str** | This is the name of your file. | [optional] 
**ext** | [**ClassificationSpecificEnum**](ClassificationSpecificEnum.md) |  | [optional] 
**size** | **int** | This is the size(in bytes) | [optional] 

## Example

```python
from openapi_client.models.file_metadata import FileMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FileMetadata from a JSON string
file_metadata_instance = FileMetadata.from_json(json)
# print the JSON string representation of the object
print FileMetadata.to_json()

# convert the object into a dict
file_metadata_dict = file_metadata_instance.to_dict()
# create an instance of FileMetadata from a dict
file_metadata_form_dict = file_metadata.from_dict(file_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


