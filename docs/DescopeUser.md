# DescopeUser

An object representing all of the properties that are available within a DescopeUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation** | [**Auth0UserAllocationMetadata**](Auth0UserAllocationMetadata.md) |  | [optional] 
**api_keys** | **List[str]** |  | [optional] 
**beta** | [**AnonymousTemporalRange**](AnonymousTemporalRange.md) |  | [optional] 
**cloud_key** | **str** |  | [optional] 
**created_time** | **int** |  | [optional] 
**email** | **str** | i.e brian.powell@pieces.app | 
**family_name** | **str** | i.e Widman | 
**given_name** | **str** | i.e Mark | 
**id** | **str** | This is the user&#39;s global id | 
**is_verified_email** | **bool** |  | [optional] 
**login_ids** | **List[str]** | these are the ids for the social providers ie google/github | [optional] 
**middle_name** | **str** | i.e &#39;&#39; or Donald | [optional] 
**name** | **str** | i.e Mark Widman | [optional] 
**oauth** | **List[str]** | these are all of the registered social providers | [optional] 
**open_ai** | [**Auth0OpenAIUserMetadata**](Auth0OpenAIUserMetadata.md) |  | [optional] 
**phone** | **str** | a users phone number | [optional] 
**picture** | **str** | the url of the users picture | [optional] 
**status** | **str** |  | [optional] 
**subscriptions** | [**UserTeamServiceOrganizationSubscriptions**](UserTeamServiceOrganizationSubscriptions.md) |  | [optional] 
**user_id** | **str** |  | 
**vanity** | **str** |  | [optional] 
**welcome_email** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.descope_user import DescopeUser

# TODO update the JSON string below
json = "{}"
# create an instance of DescopeUser from a JSON string
descope_user_instance = DescopeUser.from_json(json)
# print the JSON string representation of the object
print(DescopeUser.to_json())

# convert the object into a dict
descope_user_dict = descope_user_instance.to_dict()
# create an instance of DescopeUser from a dict
descope_user_from_dict = DescopeUser.from_dict(descope_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


