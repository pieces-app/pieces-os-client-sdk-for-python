# OSDeviceHardwareInformation

this will let us know specific hardware information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**OSDeviceCPUHardwareInformation**](OSDeviceCPUHardwareInformation.md) |  | [optional] 
**gpu** | [**OSDeviceGPUHardwareInformation**](OSDeviceGPUHardwareInformation.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.os_device_hardware_information import OSDeviceHardwareInformation

# TODO update the JSON string below
json = "{}"
# create an instance of OSDeviceHardwareInformation from a JSON string
os_device_hardware_information_instance = OSDeviceHardwareInformation.from_json(json)
# print the JSON string representation of the object
print OSDeviceHardwareInformation.to_json()

# convert the object into a dict
os_device_hardware_information_dict = os_device_hardware_information_instance.to_dict()
# create an instance of OSDeviceHardwareInformation from a dict
os_device_hardware_information_from_dict = OSDeviceHardwareInformation.from_dict(os_device_hardware_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


