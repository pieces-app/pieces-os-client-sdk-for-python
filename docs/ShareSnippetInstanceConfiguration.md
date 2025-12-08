# ShareSnippetInstanceConfiguration

Configuration for the Share Snippet feature (toggle only).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.share_snippet_instance_configuration import ShareSnippetInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ShareSnippetInstanceConfiguration from a JSON string
share_snippet_instance_configuration_instance = ShareSnippetInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(ShareSnippetInstanceConfiguration.to_json())

# convert the object into a dict
share_snippet_instance_configuration_dict = share_snippet_instance_configuration_instance.to_dict()
# create an instance of ShareSnippetInstanceConfiguration from a dict
share_snippet_instance_configuration_from_dict = ShareSnippetInstanceConfiguration.from_dict(share_snippet_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


