# HasFeatureAccessDeniedWorkstreamPatternEngineSourceContext

Context for checking if a specific source (application) is denied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | The application name to check. | 
**bundle_identifier** | **str** | Optional bundle identifier for the application. | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.has_feature_access_denied_workstream_pattern_engine_source_context import HasFeatureAccessDeniedWorkstreamPatternEngineSourceContext

# TODO update the JSON string below
json = "{}"
# create an instance of HasFeatureAccessDeniedWorkstreamPatternEngineSourceContext from a JSON string
has_feature_access_denied_workstream_pattern_engine_source_context_instance = HasFeatureAccessDeniedWorkstreamPatternEngineSourceContext.from_json(json)
# print the JSON string representation of the object
print(HasFeatureAccessDeniedWorkstreamPatternEngineSourceContext.to_json())

# convert the object into a dict
has_feature_access_denied_workstream_pattern_engine_source_context_dict = has_feature_access_denied_workstream_pattern_engine_source_context_instance.to_dict()
# create an instance of HasFeatureAccessDeniedWorkstreamPatternEngineSourceContext from a dict
has_feature_access_denied_workstream_pattern_engine_source_context_from_dict = HasFeatureAccessDeniedWorkstreamPatternEngineSourceContext.from_dict(has_feature_access_denied_workstream_pattern_engine_source_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


