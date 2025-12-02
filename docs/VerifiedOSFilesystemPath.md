# VerifiedOSFilesystemPath

This will return is the given path was verified/ or it was invalid.  and if it is valid if it is a file/folder  note: file/directory are both null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes** | [**ByteDescriptor**](ByteDescriptor.md) |  | [optional] 
**denied** | **bool** | This means that attempting to access the file was not aloud(ie no permission) | [optional] 
**directory** | **bool** |  | [optional] 
**file** | **bool** |  | [optional] 
**path** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**verified** | **bool** | This means if the path(file/folder) exists on the machine. | 

## Example

```python
from pieces_os_client.models.verified_os_filesystem_path import VerifiedOSFilesystemPath

# TODO update the JSON string below
json = "{}"
# create an instance of VerifiedOSFilesystemPath from a JSON string
verified_os_filesystem_path_instance = VerifiedOSFilesystemPath.from_json(json)
# print the JSON string representation of the object
print(VerifiedOSFilesystemPath.to_json())

# convert the object into a dict
verified_os_filesystem_path_dict = verified_os_filesystem_path_instance.to_dict()
# create an instance of VerifiedOSFilesystemPath from a dict
verified_os_filesystem_path_from_dict = VerifiedOSFilesystemPath.from_dict(verified_os_filesystem_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


