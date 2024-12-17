# Auth0User



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked_for** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**email_verified** | **bool** | Indicates whether the user has verified their email address. Mapped from email_verified -&gt; emailVerified. | [optional] 
**family_name** | **str** | User&#39;s family name. | [optional] 
**given_name** | **str** | User&#39;s given name.  | [optional] 
**guardian_authenticators** | **List[str]** |  | [optional] 
**identities** | [**List[Auth0Identity]**](Auth0Identity.md) | Contains info retrieved from the identity provider with which the user originally authenticates. | [optional] 
**last_ip** | **str** |  | [optional] 
**last_login** | **datetime** |  | [optional] 
**locale** | **str** |  | [optional] 
**logins_count** | **int** |  | [optional] 
**name** | **str** |  User&#39;s full name. | [optional] 
**nickname** | **str** | User&#39;s nickname.  | [optional] 
**picture** | **str** | mapped from picture.URL pointing to the user&#39;s profile picture.  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user_id** | **str** |  | [optional] 
**user_metadata** | [**Auth0UserMetadata**](Auth0UserMetadata.md) |  | [optional] 
**username** | **str** |  (unique) User&#39;s username.   | [optional] 

## Example

```python
from pieces_os_client.models.auth0_user import Auth0User

# TODO update the JSON string below
json = "{}"
# create an instance of Auth0User from a JSON string
auth0_user_instance = Auth0User.from_json(json)
# print the JSON string representation of the object
print Auth0User.to_json()

# convert the object into a dict
auth0_user_dict = auth0_user_instance.to_dict()
# create an instance of Auth0User from a dict
auth0_user_from_dict = Auth0User.from_dict(auth0_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


