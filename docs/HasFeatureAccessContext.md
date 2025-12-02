# HasFeatureAccessContext

Context for feature access validation. Contains optional nested models for each specific context type. All properties are optional and can be provided based on the feature being checked. Supports multiple context types and can be extended in the future. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_cloud_models** | [**HasFeatureAccessAllowedCloudModelsContext**](HasFeatureAccessAllowedCloudModelsContext.md) |  | [optional] 
**denied_workstream_pattern_engine_source** | [**HasFeatureAccessDeniedWorkstreamPatternEngineSourceContext**](HasFeatureAccessDeniedWorkstreamPatternEngineSourceContext.md) |  | [optional] 
**denied_workstream_pattern_engine_website** | [**HasFeatureAccessDeniedWorkstreamPatternEngineWebsiteContext**](HasFeatureAccessDeniedWorkstreamPatternEngineWebsiteContext.md) |  | [optional] 
**processing** | [**HasFeatureAccessProcessingContext**](HasFeatureAccessProcessingContext.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.has_feature_access_context import HasFeatureAccessContext

# TODO update the JSON string below
json = "{}"
# create an instance of HasFeatureAccessContext from a JSON string
has_feature_access_context_instance = HasFeatureAccessContext.from_json(json)
# print the JSON string representation of the object
print(HasFeatureAccessContext.to_json())

# convert the object into a dict
has_feature_access_context_dict = has_feature_access_context_instance.to_dict()
# create an instance of HasFeatureAccessContext from a dict
has_feature_access_context_from_dict = HasFeatureAccessContext.from_dict(has_feature_access_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


