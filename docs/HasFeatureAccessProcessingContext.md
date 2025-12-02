# HasFeatureAccessProcessingContext

Context for checking if a specific processing type is allowed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processing** | [**CapabilitiesEnum**](CapabilitiesEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.has_feature_access_processing_context import HasFeatureAccessProcessingContext

# TODO update the JSON string below
json = "{}"
# create an instance of HasFeatureAccessProcessingContext from a JSON string
has_feature_access_processing_context_instance = HasFeatureAccessProcessingContext.from_json(json)
# print the JSON string representation of the object
print(HasFeatureAccessProcessingContext.to_json())

# convert the object into a dict
has_feature_access_processing_context_dict = has_feature_access_processing_context_instance.to_dict()
# create an instance of HasFeatureAccessProcessingContext from a dict
has_feature_access_processing_context_from_dict = HasFeatureAccessProcessingContext.from_dict(has_feature_access_processing_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


