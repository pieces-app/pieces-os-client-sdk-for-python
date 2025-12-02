# DeniedWorkstreamPatternEngineSourcesInstanceConfiguration

Configuration for denied workstream pattern engine sources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denied_sources** | [**InstanceConfigurationDeniedWorkstreamPatternEngineSources**](InstanceConfigurationDeniedWorkstreamPatternEngineSources.md) |  | [optional] 
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.denied_workstream_pattern_engine_sources_instance_configuration import DeniedWorkstreamPatternEngineSourcesInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DeniedWorkstreamPatternEngineSourcesInstanceConfiguration from a JSON string
denied_workstream_pattern_engine_sources_instance_configuration_instance = DeniedWorkstreamPatternEngineSourcesInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(DeniedWorkstreamPatternEngineSourcesInstanceConfiguration.to_json())

# convert the object into a dict
denied_workstream_pattern_engine_sources_instance_configuration_dict = denied_workstream_pattern_engine_sources_instance_configuration_instance.to_dict()
# create an instance of DeniedWorkstreamPatternEngineSourcesInstanceConfiguration from a dict
denied_workstream_pattern_engine_sources_instance_configuration_from_dict = DeniedWorkstreamPatternEngineSourcesInstanceConfiguration.from_dict(denied_workstream_pattern_engine_sources_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


