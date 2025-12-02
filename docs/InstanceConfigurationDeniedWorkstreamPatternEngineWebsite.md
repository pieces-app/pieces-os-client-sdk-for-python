# InstanceConfigurationDeniedWorkstreamPatternEngineWebsite

Represents a single denied workstream pattern engine website.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**url** | **str** | This is the URL of the denied website. | 

## Example

```python
from pieces_os_client.models.instance_configuration_denied_workstream_pattern_engine_website import InstanceConfigurationDeniedWorkstreamPatternEngineWebsite

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceConfigurationDeniedWorkstreamPatternEngineWebsite from a JSON string
instance_configuration_denied_workstream_pattern_engine_website_instance = InstanceConfigurationDeniedWorkstreamPatternEngineWebsite.from_json(json)
# print the JSON string representation of the object
print(InstanceConfigurationDeniedWorkstreamPatternEngineWebsite.to_json())

# convert the object into a dict
instance_configuration_denied_workstream_pattern_engine_website_dict = instance_configuration_denied_workstream_pattern_engine_website_instance.to_dict()
# create an instance of InstanceConfigurationDeniedWorkstreamPatternEngineWebsite from a dict
instance_configuration_denied_workstream_pattern_engine_website_from_dict = InstanceConfigurationDeniedWorkstreamPatternEngineWebsite.from_dict(instance_configuration_denied_workstream_pattern_engine_website_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


