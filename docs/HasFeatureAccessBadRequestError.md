# HasFeatureAccessBadRequestError

Error response for bad request (400) when invalid input parameters or missing required context for the feature.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code indicating the type of validation error. | 
**message** | **str** | Error message describing the validation failure. | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.has_feature_access_bad_request_error import HasFeatureAccessBadRequestError

# TODO update the JSON string below
json = "{}"
# create an instance of HasFeatureAccessBadRequestError from a JSON string
has_feature_access_bad_request_error_instance = HasFeatureAccessBadRequestError.from_json(json)
# print the JSON string representation of the object
print(HasFeatureAccessBadRequestError.to_json())

# convert the object into a dict
has_feature_access_bad_request_error_dict = has_feature_access_bad_request_error_instance.to_dict()
# create an instance of HasFeatureAccessBadRequestError from a dict
has_feature_access_bad_request_error_from_dict = HasFeatureAccessBadRequestError.from_dict(has_feature_access_bad_request_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


