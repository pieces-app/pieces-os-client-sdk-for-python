# ByteDescriptor

This is a nice microclass to help with managing the size of a File or Fragment in a readable way for UI's

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**value** | **int** |  | 
**readable** | **str** |  | 

## Example

```python
from openapi_client.models.byte_descriptor import ByteDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of ByteDescriptor from a JSON string
byte_descriptor_instance = ByteDescriptor.from_json(json)
# print the JSON string representation of the object
print ByteDescriptor.to_json()

# convert the object into a dict
byte_descriptor_dict = byte_descriptor_instance.to_dict()
# create an instance of ByteDescriptor from a dict
byte_descriptor_form_dict = byte_descriptor.from_dict(byte_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


