# ReturnedUserProfile

This is a modle strictly for the purpose that when calling '/user' and other user related endpoints the UserProfile could potentially be null, so we needed a model to do that.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**user** | [**UserProfile**](UserProfile.md) |  | [optional] 

## Example

```python
from openapi_client.models.returned_user_profile import ReturnedUserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnedUserProfile from a JSON string
returned_user_profile_instance = ReturnedUserProfile.from_json(json)
# print the JSON string representation of the object
print ReturnedUserProfile.to_json()

# convert the object into a dict
returned_user_profile_dict = returned_user_profile_instance.to_dict()
# create an instance of ReturnedUserProfile from a dict
returned_user_profile_form_dict = returned_user_profile.from_dict(returned_user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


