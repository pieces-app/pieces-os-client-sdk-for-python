# HasFeatureAccessOutput

Result type for feature access validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_use** | **bool** | Can use the specific resource (model/source/website/processing type). Always true if no context provided. | 
**enabled** | **bool** | Feature toggle status (is the feature enabled/disabled). | 
**is_enterprise_user** | **bool** | Whether the user is an enterprise user (has organizations). | 
**reason** | **str** | Optional reason for denial (useful for debugging). | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.has_feature_access_output import HasFeatureAccessOutput

# TODO update the JSON string below
json = "{}"
# create an instance of HasFeatureAccessOutput from a JSON string
has_feature_access_output_instance = HasFeatureAccessOutput.from_json(json)
# print the JSON string representation of the object
print(HasFeatureAccessOutput.to_json())

# convert the object into a dict
has_feature_access_output_dict = has_feature_access_output_instance.to_dict()
# create an instance of HasFeatureAccessOutput from a dict
has_feature_access_output_from_dict = HasFeatureAccessOutput.from_dict(has_feature_access_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


