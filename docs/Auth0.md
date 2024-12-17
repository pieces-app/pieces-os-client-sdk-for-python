# Auth0

An object representing all of the properties that are available within a Auth0 PKCE Flow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** | The Server Audience of your Auth0 Service | 
**client** | **str** | The Client ID for your Auth0 Service | 
**domain** | **str** | The domain of your Auth 0 Service | 
**identity** | [**Auth0Identity**](Auth0Identity.md) |  | [optional] 
**metadata** | [**Auth0UserMetadata**](Auth0UserMetadata.md) |  | [optional] 
**namespace** | **str** | An optional namespace parameter to add an additional namespace | [optional] 
**o_auth** | [**OAuthGroup**](OAuthGroup.md) |  | 
**redirects** | [**Auth0Redirects**](Auth0Redirects.md) |  | 
**user** | [**Auth0User**](Auth0User.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.auth0 import Auth0

# TODO update the JSON string below
json = "{}"
# create an instance of Auth0 from a JSON string
auth0_instance = Auth0.from_json(json)
# print the JSON string representation of the object
print Auth0.to_json()

# convert the object into a dict
auth0_dict = auth0_instance.to_dict()
# create an instance of Auth0 from a dict
auth0_from_dict = Auth0.from_dict(auth0_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


