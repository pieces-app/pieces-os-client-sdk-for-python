# OSDeviceRAMHardwareInformation

This will let us know specific hardware information related to the RAM.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory** | **float** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**speed** | **float** |  | [optional] 
**type** | [**OSDeviceRAMTypeEnum**](OSDeviceRAMTypeEnum.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.os_device_ram_hardware_information import OSDeviceRAMHardwareInformation

# TODO update the JSON string below
json = "{}"
# create an instance of OSDeviceRAMHardwareInformation from a JSON string
os_device_ram_hardware_information_instance = OSDeviceRAMHardwareInformation.from_json(json)
# print the JSON string representation of the object
print(OSDeviceRAMHardwareInformation.to_json())

# convert the object into a dict
os_device_ram_hardware_information_dict = os_device_ram_hardware_information_instance.to_dict()
# create an instance of OSDeviceRAMHardwareInformation from a dict
os_device_ram_hardware_information_from_dict = OSDeviceRAMHardwareInformation.from_dict(os_device_ram_hardware_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


