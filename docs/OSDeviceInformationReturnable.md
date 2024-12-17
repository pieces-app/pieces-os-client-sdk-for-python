# OSDeviceInformationReturnable

This is the returnable model for the /os/device/information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**dependencies** | [**OSDeviceDependenciesInformation**](OSDeviceDependenciesInformation.md) |  | [optional] 
**name** | **str** | this is the name of the device | [optional] 
**version** | **str** | this is the version of the device | [optional] 
**hardware** | [**OSDeviceHardwareInformation**](OSDeviceHardwareInformation.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.os_device_information_returnable import OSDeviceInformationReturnable

# TODO update the JSON string below
json = "{}"
# create an instance of OSDeviceInformationReturnable from a JSON string
os_device_information_returnable_instance = OSDeviceInformationReturnable.from_json(json)
# print the JSON string representation of the object
print OSDeviceInformationReturnable.to_json()

# convert the object into a dict
os_device_information_returnable_dict = os_device_information_returnable_instance.to_dict()
# create an instance of OSDeviceInformationReturnable from a dict
os_device_information_returnable_from_dict = OSDeviceInformationReturnable.from_dict(os_device_information_returnable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


