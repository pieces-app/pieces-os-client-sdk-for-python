# UpdateAllocationCloudInstanceConfiguration

Configuration for the Update Allocation Cloud feature (toggle only).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.update_allocation_cloud_instance_configuration import UpdateAllocationCloudInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAllocationCloudInstanceConfiguration from a JSON string
update_allocation_cloud_instance_configuration_instance = UpdateAllocationCloudInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(UpdateAllocationCloudInstanceConfiguration.to_json())

# convert the object into a dict
update_allocation_cloud_instance_configuration_dict = update_allocation_cloud_instance_configuration_instance.to_dict()
# create an instance of UpdateAllocationCloudInstanceConfiguration from a dict
update_allocation_cloud_instance_configuration_from_dict = UpdateAllocationCloudInstanceConfiguration.from_dict(update_allocation_cloud_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


