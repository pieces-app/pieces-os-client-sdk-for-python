# UncheckedOSServerUpdate

This is the input body for /os/update/check, just a placeholder for now.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.unchecked_os_server_update import UncheckedOSServerUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UncheckedOSServerUpdate from a JSON string
unchecked_os_server_update_instance = UncheckedOSServerUpdate.from_json(json)
# print the JSON string representation of the object
print UncheckedOSServerUpdate.to_json()

# convert the object into a dict
unchecked_os_server_update_dict = unchecked_os_server_update_instance.to_dict()
# create an instance of UncheckedOSServerUpdate from a dict
unchecked_os_server_update_from_dict = UncheckedOSServerUpdate.from_dict(unchecked_os_server_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


