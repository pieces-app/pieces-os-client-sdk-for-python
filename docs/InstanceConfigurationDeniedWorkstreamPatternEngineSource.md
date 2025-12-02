# InstanceConfigurationDeniedWorkstreamPatternEngineSource

Represents a single denied workstream pattern engine source.  application: this is the application name that will be used to check executable and application detected

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | This is the application name that will be used to check executable and application detected. | [optional] 
**bundle_identifiers** | **List[str]** | this is the bundle identifier of the application ie, com.pieces.os, ... | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.instance_configuration_denied_workstream_pattern_engine_source import InstanceConfigurationDeniedWorkstreamPatternEngineSource

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceConfigurationDeniedWorkstreamPatternEngineSource from a JSON string
instance_configuration_denied_workstream_pattern_engine_source_instance = InstanceConfigurationDeniedWorkstreamPatternEngineSource.from_json(json)
# print the JSON string representation of the object
print(InstanceConfigurationDeniedWorkstreamPatternEngineSource.to_json())

# convert the object into a dict
instance_configuration_denied_workstream_pattern_engine_source_dict = instance_configuration_denied_workstream_pattern_engine_source_instance.to_dict()
# create an instance of InstanceConfigurationDeniedWorkstreamPatternEngineSource from a dict
instance_configuration_denied_workstream_pattern_engine_source_from_dict = InstanceConfigurationDeniedWorkstreamPatternEngineSource.from_dict(instance_configuration_denied_workstream_pattern_engine_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


