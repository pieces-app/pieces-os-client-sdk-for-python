# OSPermissions

This will return the permission of this specific operating system w/ relation to given features.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processing** | [**OSProcessingPermissions**](OSProcessingPermissions.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.os_permissions import OSPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of OSPermissions from a JSON string
os_permissions_instance = OSPermissions.from_json(json)
# print the JSON string representation of the object
print(OSPermissions.to_json())

# convert the object into a dict
os_permissions_dict = os_permissions_instance.to_dict()
# create an instance of OSPermissions from a dict
os_permissions_from_dict = OSPermissions.from_dict(os_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


