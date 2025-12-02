# OSDeviceCPUHardwareInformation

This will let us know specific hardware information related to the CPU.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clock_cycle_speed** | **float** |  | [optional] 
**cores** | **float** |  | [optional] 
**l1_cache** | **float** |  | [optional] 
**l2_cache** | **float** |  | [optional] 
**l3_cache** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**shared_memory** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.os_device_cpu_hardware_information import OSDeviceCPUHardwareInformation

# TODO update the JSON string below
json = "{}"
# create an instance of OSDeviceCPUHardwareInformation from a JSON string
os_device_cpu_hardware_information_instance = OSDeviceCPUHardwareInformation.from_json(json)
# print the JSON string representation of the object
print(OSDeviceCPUHardwareInformation.to_json())

# convert the object into a dict
os_device_cpu_hardware_information_dict = os_device_cpu_hardware_information_instance.to_dict()
# create an instance of OSDeviceCPUHardwareInformation from a dict
os_device_cpu_hardware_information_from_dict = OSDeviceCPUHardwareInformation.from_dict(os_device_cpu_hardware_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


