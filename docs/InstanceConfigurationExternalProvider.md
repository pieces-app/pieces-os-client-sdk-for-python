# InstanceConfigurationExternalProvider

Grouping of all external provider-related features.  This includes model customization, processing capabilities, and denied lists for workstream pattern engine.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_cloud_models** | [**AllowedCloudModelsInstanceConfiguration**](AllowedCloudModelsInstanceConfiguration.md) |  | [optional] 
**denied_workstream_pattern_engine_sources** | [**DeniedWorkstreamPatternEngineSourcesInstanceConfiguration**](DeniedWorkstreamPatternEngineSourcesInstanceConfiguration.md) |  | [optional] 
**denied_workstream_pattern_engine_websites** | [**DeniedWorkstreamPatternEngineWebsitesInstanceConfiguration**](DeniedWorkstreamPatternEngineWebsitesInstanceConfiguration.md) |  | [optional] 
**processing** | [**ProcessingInstanceConfiguration**](ProcessingInstanceConfiguration.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.instance_configuration_external_provider import InstanceConfigurationExternalProvider

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceConfigurationExternalProvider from a JSON string
instance_configuration_external_provider_instance = InstanceConfigurationExternalProvider.from_json(json)
# print the JSON string representation of the object
print(InstanceConfigurationExternalProvider.to_json())

# convert the object into a dict
instance_configuration_external_provider_dict = instance_configuration_external_provider_instance.to_dict()
# create an instance of InstanceConfigurationExternalProvider from a dict
instance_configuration_external_provider_from_dict = InstanceConfigurationExternalProvider.from_dict(instance_configuration_external_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


