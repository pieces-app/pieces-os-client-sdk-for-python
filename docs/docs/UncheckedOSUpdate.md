# UncheckedOSUpdate

This is the input body for /os/update/check, just a placeholder for now.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.unchecked_os_update import UncheckedOSUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UncheckedOSUpdate from a JSON string
unchecked_os_update_instance = UncheckedOSUpdate.from_json(json)
# print the JSON string representation of the object
print UncheckedOSUpdate.to_json()

# convert the object into a dict
unchecked_os_update_dict = unchecked_os_update_instance.to_dict()
# create an instance of UncheckedOSUpdate from a dict
unchecked_os_update_form_dict = unchecked_os_update.from_dict(unchecked_os_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


