# ExternalProviderProfileData

All of these will be optional.  Will support ProfileData from all our social providers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**blog** | **str** |  | [optional] 
**collaborators** | **int** |  | [optional] 
**company** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**disk_usage** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**email_verified** | **bool** |  | [optional] 
**events_url** | **str** |  | [optional] 
**followers** | **int** |  | [optional] 
**followers_url** | **str** |  | [optional] 
**following** | **int** |  | [optional] 
**following_url** | **str** |  | [optional] 
**gists_url** | **str** |  | [optional] 
**gravatar_id** | **str** |  | [optional] 
**hireable** | **bool** |  | [optional] 
**html_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**node_id** | **str** |  | [optional] 
**organizations_url** | **str** |  | [optional] 
**owned_private_repos** | **int** |  | [optional] 
**picture** | **str** |  | [optional] 
**private_gists** | **int** |  | [optional] 
**public_gists** | **int** |  | [optional] 
**public_repos** | **int** |  | [optional] 
**received_events_url** | **str** |  | [optional] 
**repos_url** | **str** |  | [optional] 
**site_admin** | **bool** |  | [optional] 
**starred_url** | **str** |  | [optional] 
**subscriptions_url** | **str** |  | [optional] 
**total_private_repos** | **int** |  | [optional] 
**twitter_username** | **str** |  | [optional] 
**two_factor_authentication** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from pieces_os_client.models.external_provider_profile_data import ExternalProviderProfileData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalProviderProfileData from a JSON string
external_provider_profile_data_instance = ExternalProviderProfileData.from_json(json)
# print the JSON string representation of the object
print(ExternalProviderProfileData.to_json())

# convert the object into a dict
external_provider_profile_data_dict = external_provider_profile_data_instance.to_dict()
# create an instance of ExternalProviderProfileData from a dict
external_provider_profile_data_from_dict = ExternalProviderProfileData.from_dict(external_provider_profile_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


