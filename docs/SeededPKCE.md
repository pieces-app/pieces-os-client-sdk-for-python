# SeededPKCE

A model that initialized a PKCE Authentication Flow.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_parameters** | [**SeededPKCEADDITIONALPARAMETERS**](SeededPKCEADDITIONALPARAMETERS.md) |  | [optional] 
**audience** | **str** | The unique identifier of the target API you want to access. i.e. https://pieces.us.auth0.com/api/v2/ | [optional] 
**client_id** | **str** | Your application&#39;s Client ID. | 
**code_challenge** | **str** | Generated challenge from the code_verifier. | 
**code_challenge_method** | **str** | Method used to generate the challenge. The PKCE spec defines two methods, S256 and plain, however, Auth0 supports only S256 since the latter is discouraged. | 
**domain** | **str** | https://auth.pieces.services/authorize | [optional] 
**invitation** | **str** |  | [optional] 
**nonce** | **str** | A local key that is held as the comparator to state, thus they should be the same. | 
**organization** | **str** |  | [optional] 
**prompt** | **str** |  To initiate a silent authentication request, use prompt&#x3D;none (see Remarks for more info). | [optional] 
**redirect_uri** | **str** | http://localhost:8080/authentication/response | [optional] 
**response_mode** | **str** |  | [optional] 
**response_type** | **str** | Indicates to Auth0 which OAuth 2.0 Flow you want to perform. Use code for Authorization Code Grant (PKCE) Flow. | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**scope** | **List[str]** | The scopes which you want to request authorization for. These must be separated by a space. You can request any of the standard OpenID Connect (OIDC) scopes about users, such as profile and email, custom claims that must conform to a namespaced format, or any scopes supported by the target API (for example, read:contacts). Include offline_access to get a Refresh Token. | 
**screen_hint** | **str** | Provides a hint to Auth0 as to what flow should be displayed. The default behavior is to show a login page but you can override this by passing &#39;signup&#39; to show the signup page instead. | [optional] 
**state** | **str** | An opaque value the clients adds to the initial request that Auth0 includes when redirecting the back to the client. This value must be used by the client to prevent CSRF attacks. | 

## Example

```python
from pieces_os_client.models.seeded_pkce import SeededPKCE

# TODO update the JSON string below
json = "{}"
# create an instance of SeededPKCE from a JSON string
seeded_pkce_instance = SeededPKCE.from_json(json)
# print the JSON string representation of the object
print SeededPKCE.to_json()

# convert the object into a dict
seeded_pkce_dict = seeded_pkce_instance.to_dict()
# create an instance of SeededPKCE from a dict
seeded_pkce_from_dict = SeededPKCE.from_dict(seeded_pkce_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


