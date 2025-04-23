# ApplicationsBulkUpdateCapabilitiesInput

This is an endpoint to bulk update your applications to a specific capabilitiesEnum

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**capabilities** | [**CapabilitiesEnum**](CapabilitiesEnum.md) |  | 

## Example

```python
from pieces_os_client.models.applications_bulk_update_capabilities_input import ApplicationsBulkUpdateCapabilitiesInput

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsBulkUpdateCapabilitiesInput from a JSON string
applications_bulk_update_capabilities_input_instance = ApplicationsBulkUpdateCapabilitiesInput.from_json(json)
# print the JSON string representation of the object
print ApplicationsBulkUpdateCapabilitiesInput.to_json()

# convert the object into a dict
applications_bulk_update_capabilities_input_dict = applications_bulk_update_capabilities_input_instance.to_dict()
# create an instance of ApplicationsBulkUpdateCapabilitiesInput from a dict
applications_bulk_update_capabilities_input_from_dict = ApplicationsBulkUpdateCapabilitiesInput.from_dict(applications_bulk_update_capabilities_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


