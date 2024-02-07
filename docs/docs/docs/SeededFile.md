# SeededFile

This is a base model for a File(Seeded).  We will Throw an Error, if the text and the bytes properties are both null && if both the text and bytes properties are both defined. Ensure that you pass either a text or bytes property.  bytes and string are both optionl but, if both are null or both are defined we will throw an error. So You will be required to pass one or the other, NOT both.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**bytes** | [**TransferableBytes**](TransferableBytes.md) |  | [optional] 
**string** | [**TransferableString**](TransferableString.md) |  | [optional] 
**metadata** | [**FileMetadata**](FileMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.seeded_file import SeededFile

# TODO update the JSON string below
json = "{}"
# create an instance of SeededFile from a JSON string
seeded_file_instance = SeededFile.from_json(json)
# print the JSON string representation of the object
print SeededFile.to_json()

# convert the object into a dict
seeded_file_dict = seeded_file_instance.to_dict()
# create an instance of SeededFile from a dict
seeded_file_form_dict = seeded_file.from_dict(seeded_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


