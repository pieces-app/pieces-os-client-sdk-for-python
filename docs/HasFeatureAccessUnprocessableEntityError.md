# HasFeatureAccessUnprocessableEntityError

Error response for unprocessable entity (422) when invalid context is provided for the requested feature.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_context_type** | **str** | The expected context type for this feature. | 
**feature** | **str** | The feature that was requested. | 
**message** | **str** | Error message describing the context validation failure. | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.has_feature_access_unprocessable_entity_error import HasFeatureAccessUnprocessableEntityError

# TODO update the JSON string below
json = "{}"
# create an instance of HasFeatureAccessUnprocessableEntityError from a JSON string
has_feature_access_unprocessable_entity_error_instance = HasFeatureAccessUnprocessableEntityError.from_json(json)
# print the JSON string representation of the object
print(HasFeatureAccessUnprocessableEntityError.to_json())

# convert the object into a dict
has_feature_access_unprocessable_entity_error_dict = has_feature_access_unprocessable_entity_error_instance.to_dict()
# create an instance of HasFeatureAccessUnprocessableEntityError from a dict
has_feature_access_unprocessable_entity_error_from_dict = HasFeatureAccessUnprocessableEntityError.from_dict(has_feature_access_unprocessable_entity_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


