# PKCE

An object representing all of the properties involved in a PKCE Authentication Flow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth0** | [**Auth0**](Auth0.md) |  | [optional] 
**challenge** | [**ChallengedPKCE**](ChallengedPKCE.md) |  | [optional] 
**result** | [**ResultedPKCE**](ResultedPKCE.md) |  | [optional] 
**revocation** | [**RevokedPKCE**](RevokedPKCE.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**seed** | [**SeededPKCE**](SeededPKCE.md) |  | [optional] 
**token** | [**TokenizedPKCE**](TokenizedPKCE.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.pkce import PKCE

# TODO update the JSON string below
json = "{}"
# create an instance of PKCE from a JSON string
pkce_instance = PKCE.from_json(json)
# print the JSON string representation of the object
print PKCE.to_json()

# convert the object into a dict
pkce_dict = pkce_instance.to_dict()
# create an instance of PKCE from a dict
pkce_from_dict = PKCE.from_dict(pkce_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


