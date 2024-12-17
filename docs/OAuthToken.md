# OAuthToken

A model representing a returnable response for a OAuthGroup Token

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The Access Token | 
**expires_in** | **int** |  | 
**id_token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**scope** | **str** |  | 
**token_type** | **str** |  | 

## Example

```python
from pieces_os_client.models.o_auth_token import OAuthToken

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthToken from a JSON string
o_auth_token_instance = OAuthToken.from_json(json)
# print the JSON string representation of the object
print OAuthToken.to_json()

# convert the object into a dict
o_auth_token_dict = o_auth_token_instance.to_dict()
# create an instance of OAuthToken from a dict
o_auth_token_from_dict = OAuthToken.from_dict(o_auth_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


