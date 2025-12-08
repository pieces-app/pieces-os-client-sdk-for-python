# RefreshedPaddleUser

Output model for the user paddle refresh endpoint. Contains user profile and can be extended with additional paddle-related properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**user** | [**UserProfile**](UserProfile.md) |  | 

## Example

```python
from pieces_os_client.models.refreshed_paddle_user import RefreshedPaddleUser

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshedPaddleUser from a JSON string
refreshed_paddle_user_instance = RefreshedPaddleUser.from_json(json)
# print the JSON string representation of the object
print(RefreshedPaddleUser.to_json())

# convert the object into a dict
refreshed_paddle_user_dict = refreshed_paddle_user_instance.to_dict()
# create an instance of RefreshedPaddleUser from a dict
refreshed_paddle_user_from_dict = RefreshedPaddleUser.from_dict(refreshed_paddle_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


