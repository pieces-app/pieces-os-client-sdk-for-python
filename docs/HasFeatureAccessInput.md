# HasFeatureAccessInput

Input model for checking feature access with optional context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**HasFeatureAccessContext**](HasFeatureAccessContext.md) |  | [optional] 
**feature** | [**HasFeatureAccessEnum**](HasFeatureAccessEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.has_feature_access_input import HasFeatureAccessInput

# TODO update the JSON string below
json = "{}"
# create an instance of HasFeatureAccessInput from a JSON string
has_feature_access_input_instance = HasFeatureAccessInput.from_json(json)
# print the JSON string representation of the object
print(HasFeatureAccessInput.to_json())

# convert the object into a dict
has_feature_access_input_dict = has_feature_access_input_instance.to_dict()
# create an instance of HasFeatureAccessInput from a dict
has_feature_access_input_from_dict = HasFeatureAccessInput.from_dict(has_feature_access_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


