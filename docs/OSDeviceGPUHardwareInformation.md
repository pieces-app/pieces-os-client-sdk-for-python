# OSDeviceGPUHardwareInformation

This will let us know specific hardware information related to the GPU.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**name** | **str** |  | [optional] 
**memory** | **float** |  | [optional] 
**capabilities** | [**OSDeviceGPUHardwareCapabilitiesInformation**](OSDeviceGPUHardwareCapabilitiesInformation.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.os_device_gpu_hardware_information import OSDeviceGPUHardwareInformation

# TODO update the JSON string below
json = "{}"
# create an instance of OSDeviceGPUHardwareInformation from a JSON string
os_device_gpu_hardware_information_instance = OSDeviceGPUHardwareInformation.from_json(json)
# print the JSON string representation of the object
print OSDeviceGPUHardwareInformation.to_json()

# convert the object into a dict
os_device_gpu_hardware_information_dict = os_device_gpu_hardware_information_instance.to_dict()
# create an instance of OSDeviceGPUHardwareInformation from a dict
os_device_gpu_hardware_information_from_dict = OSDeviceGPUHardwareInformation.from_dict(os_device_gpu_hardware_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


