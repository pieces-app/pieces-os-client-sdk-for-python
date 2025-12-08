# HasFeatureAccessDeniedWorkstreamPatternEngineWebsiteContext

Context for checking if a specific website is denied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**website** | **str** | The website URL to check. | 

## Example

```python
from pieces_os_client.models.has_feature_access_denied_workstream_pattern_engine_website_context import HasFeatureAccessDeniedWorkstreamPatternEngineWebsiteContext

# TODO update the JSON string below
json = "{}"
# create an instance of HasFeatureAccessDeniedWorkstreamPatternEngineWebsiteContext from a JSON string
has_feature_access_denied_workstream_pattern_engine_website_context_instance = HasFeatureAccessDeniedWorkstreamPatternEngineWebsiteContext.from_json(json)
# print the JSON string representation of the object
print(HasFeatureAccessDeniedWorkstreamPatternEngineWebsiteContext.to_json())

# convert the object into a dict
has_feature_access_denied_workstream_pattern_engine_website_context_dict = has_feature_access_denied_workstream_pattern_engine_website_context_instance.to_dict()
# create an instance of HasFeatureAccessDeniedWorkstreamPatternEngineWebsiteContext from a dict
has_feature_access_denied_workstream_pattern_engine_website_context_from_dict = HasFeatureAccessDeniedWorkstreamPatternEngineWebsiteContext.from_dict(has_feature_access_denied_workstream_pattern_engine_website_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


