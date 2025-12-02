# DeniedWorkstreamPatternEngineWebsitesInstanceConfiguration

Configuration for denied workstream pattern engine websites.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denied_websites** | [**InstanceConfigurationDeniedWorkstreamPatternEngineWebsites**](InstanceConfigurationDeniedWorkstreamPatternEngineWebsites.md) |  | [optional] 
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.denied_workstream_pattern_engine_websites_instance_configuration import DeniedWorkstreamPatternEngineWebsitesInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DeniedWorkstreamPatternEngineWebsitesInstanceConfiguration from a JSON string
denied_workstream_pattern_engine_websites_instance_configuration_instance = DeniedWorkstreamPatternEngineWebsitesInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(DeniedWorkstreamPatternEngineWebsitesInstanceConfiguration.to_json())

# convert the object into a dict
denied_workstream_pattern_engine_websites_instance_configuration_dict = denied_workstream_pattern_engine_websites_instance_configuration_instance.to_dict()
# create an instance of DeniedWorkstreamPatternEngineWebsitesInstanceConfiguration from a dict
denied_workstream_pattern_engine_websites_instance_configuration_from_dict = DeniedWorkstreamPatternEngineWebsitesInstanceConfiguration.from_dict(denied_workstream_pattern_engine_websites_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


