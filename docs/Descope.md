# Descope

An object representing all of the properties that are available within a Descope PKCE Flow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** |  | [optional] 
**o_auth** | [**OAuthGroup**](OAuthGroup.md) |  | 
**redirects** | [**Auth0Redirects**](Auth0Redirects.md) |  | 
**user** | [**DescopeUser**](DescopeUser.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.descope import Descope

# TODO update the JSON string below
json = "{}"
# create an instance of Descope from a JSON string
descope_instance = Descope.from_json(json)
# print the JSON string representation of the object
print(Descope.to_json())

# convert the object into a dict
descope_dict = descope_instance.to_dict()
# create an instance of Descope from a dict
descope_from_dict = Descope.from_dict(descope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


