# ProcessingInstanceConfiguration

Configuration for processing capabilities (LOCAL, CLOUD, BLENDED).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**processing** | [**CapabilitiesEnum**](CapabilitiesEnum.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.processing_instance_configuration import ProcessingInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingInstanceConfiguration from a JSON string
processing_instance_configuration_instance = ProcessingInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(ProcessingInstanceConfiguration.to_json())

# convert the object into a dict
processing_instance_configuration_dict = processing_instance_configuration_instance.to_dict()
# create an instance of ProcessingInstanceConfiguration from a dict
processing_instance_configuration_from_dict = ProcessingInstanceConfiguration.from_dict(processing_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


