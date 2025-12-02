# HasFeatureAccessAllowedCloudModelsContext

Context for checking if a specific cloud model is allowed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_unique_name** | **str** | The name of the model to check access for.(ie the unique name of the model) | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.has_feature_access_allowed_cloud_models_context import HasFeatureAccessAllowedCloudModelsContext

# TODO update the JSON string below
json = "{}"
# create an instance of HasFeatureAccessAllowedCloudModelsContext from a JSON string
has_feature_access_allowed_cloud_models_context_instance = HasFeatureAccessAllowedCloudModelsContext.from_json(json)
# print the JSON string representation of the object
print(HasFeatureAccessAllowedCloudModelsContext.to_json())

# convert the object into a dict
has_feature_access_allowed_cloud_models_context_dict = has_feature_access_allowed_cloud_models_context_instance.to_dict()
# create an instance of HasFeatureAccessAllowedCloudModelsContext from a dict
has_feature_access_allowed_cloud_models_context_from_dict = HasFeatureAccessAllowedCloudModelsContext.from_dict(has_feature_access_allowed_cloud_models_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


