# UserProfile

This is the model for a user logged into Pieces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aesthetics** | [**Aesthetics**](Aesthetics.md) |  | 
**allocation** | [**AllocationCloud**](AllocationCloud.md) |  | [optional] 
**api_keys** | **List[str]** |  | [optional] 
**auth0** | [**Auth0UserMetadata**](Auth0UserMetadata.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**descope** | [**DescopeUserMetadata**](DescopeUserMetadata.md) |  | [optional] 
**email** | **str** |  | [optional] [default to 'user@pieces.app']
**entities** | [**FlattenedEntities**](FlattenedEntities.md) |  | [optional] 
**id** | **str** |  | 
**name** | **str** | This is the name of the User. | [optional] 
**picture** | **str** | mapped from picture.URL pointing to the user&#39;s profile picture.  | [optional] [default to 'https://picsum.photos/200']
**providers** | [**ExternalProviders**](ExternalProviders.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**subscriptions** | [**FlattenedSubscriptions**](FlattenedSubscriptions.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**username** | **str** |  (unique) User&#39;s username.   | [optional] 
**vanityname** | **str** |  | [optional] 

## Example

```python
from pieces_os_client.models.user_profile import UserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfile from a JSON string
user_profile_instance = UserProfile.from_json(json)
# print the JSON string representation of the object
print(UserProfile.to_json())

# convert the object into a dict
user_profile_dict = user_profile_instance.to_dict()
# create an instance of UserProfile from a dict
user_profile_from_dict = UserProfile.from_dict(user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


