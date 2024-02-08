# openapi_client.Auth0Api

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth0_logout**](Auth0Api.md#auth0_logout) | **GET** /v2/logout | https://auth.pieces.services/v2/logout [GET]
[**authorize_auth0**](Auth0Api.md#authorize_auth0) | **GET** /authorize | https://auth.pieces.services/authorize [GET]
[**exchange_for_auth0_token**](Auth0Api.md#exchange_for_auth0_token) | **POST** /oauth/token | https://auth.pieces.services/oauth/token [POST]
[**get_auth0_user_info**](Auth0Api.md#get_auth0_user_info) | **GET** /userinfo | https://auth.pieces.services/userinfo [GET]


# **auth0_logout**
> str auth0_logout(client_id=client_id, return_to=return_to)

https://auth.pieces.services/v2/logout [GET]

https://auth0.com/docs/api/authentication#logout

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Auth0Api(api_client)
    client_id = 'client_id_example' # str | The client ID of the Auth0 Instance (optional)
    return_to = 'return_to_example' # str | The URL that the logout endpoint will return to (optional)

    try:
        # https://auth.pieces.services/v2/logout [GET]
        api_response = api_instance.auth0_logout(client_id=client_id, return_to=return_to)
        print("The response of Auth0Api->auth0_logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Auth0Api->auth0_logout: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The client ID of the Auth0 Instance | [optional] 
 **return_to** | **str**| The URL that the logout endpoint will return to | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorize_auth0**
> ResultedPKCE authorize_auth0(audience, scope, response_type, client_id, code_challenge_method, code_challenge, response_mode, state=state, redirect_uri=redirect_uri, connection=connection, prompt=prompt)

https://auth.pieces.services/authorize [GET]

An endpoint that is used locally authenticate via a PKCE Flow.  Example https://auth.pieces.services /authorize?audience=https%3A%2F%2Fpieces.us.auth0.com%2Fapi%2Fv2%2F&scope=email+profile+offline_access+openid&response_type=code&client_id=9sW4Pa1LEjX67l6VO14u0207NLYeXnu1&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fpkce%2Fresponse%2Fcode&code_challenge_method=S256&code_challenge=yxRssZxdfBpMigRmDxAety1QU72Bd5WnDUbtlsCZOnk&response_mode=form_post&state=4bd0b9a389b4b229602346c33913b4c3c199628a90011ab3a901302ab62b3832

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.resulted_pkce import ResultedPKCE
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Auth0Api(api_client)
    audience = 'https://pieces.us.auth0.com/api/v2/' # str |  The unique identifier of the target API you want to access.
    scope = ['scope_example'] # List[str] | The scopes which you want to request authorization for. These must be separated by a space. You can request any of the standard OpenID Connect (OIDC) scopes about users, such as profile and email, custom claims that must conform to a namespaced format, or any scopes supported by the target API (for example, read:contacts). Include offline_access to get a Refresh Token.
    response_type = 'code' # str | Indicates to Auth0 which OAuth 2.0 Flow you want to perform. Use code for Authorization Code Grant (PKCE) Flow.
    client_id = '9sW4Pa1LEjX67l6VO14u0207NLYeXnu1' # str | Your application's Client ID.
    code_challenge_method = 'S256' # str | Method used to generate the challenge. The PKCE spec defines two methods, S256 and plain, however, Auth0 supports only S256 since the latter is discouraged.
    code_challenge = 'yxRssZxdfBpMigRmDxAety1QU72Bd5WnDUbtlsCZOnk' # str | Generated challenge from the code_verifier.
    response_mode = 'response_mode_example' # str | 
    state = 'state_example' # str | An opaque value the clients adds to the initial request that Auth0 includes when redirecting the back to the client. This value must be used by the client to prevent CSRF attacks. (optional)
    redirect_uri = 'redirect_uri_example' # str | The URL to which Auth0 will redirect the browser after authorization has been granted by the user. (optional)
    connection = 'connection_example' # str | The name of the connection configured to your application. (optional)
    prompt = 'prompt_example' # str | To initiate a silent authentication request, use prompt=none (see Remarks for more info). (optional)

    try:
        # https://auth.pieces.services/authorize [GET]
        api_response = api_instance.authorize_auth0(audience, scope, response_type, client_id, code_challenge_method, code_challenge, response_mode, state=state, redirect_uri=redirect_uri, connection=connection, prompt=prompt)
        print("The response of Auth0Api->authorize_auth0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Auth0Api->authorize_auth0: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience** | **str**|  The unique identifier of the target API you want to access. | 
 **scope** | [**List[str]**](str.md)| The scopes which you want to request authorization for. These must be separated by a space. You can request any of the standard OpenID Connect (OIDC) scopes about users, such as profile and email, custom claims that must conform to a namespaced format, or any scopes supported by the target API (for example, read:contacts). Include offline_access to get a Refresh Token. | 
 **response_type** | **str**| Indicates to Auth0 which OAuth 2.0 Flow you want to perform. Use code for Authorization Code Grant (PKCE) Flow. | 
 **client_id** | **str**| Your application&#39;s Client ID. | 
 **code_challenge_method** | **str**| Method used to generate the challenge. The PKCE spec defines two methods, S256 and plain, however, Auth0 supports only S256 since the latter is discouraged. | 
 **code_challenge** | **str**| Generated challenge from the code_verifier. | 
 **response_mode** | **str**|  | 
 **state** | **str**| An opaque value the clients adds to the initial request that Auth0 includes when redirecting the back to the client. This value must be used by the client to prevent CSRF attacks. | [optional] 
 **redirect_uri** | **str**| The URL to which Auth0 will redirect the browser after authorization has been granted by the user. | [optional] 
 **connection** | **str**| The name of the connection configured to your application. | [optional] 
 **prompt** | **str**| To initiate a silent authentication request, use prompt&#x3D;none (see Remarks for more info). | [optional] 

### Return type

[**ResultedPKCE**](ResultedPKCE.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-www-form-urlencoded

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_for_auth0_token**
> OAuthToken exchange_for_auth0_token(grant_type, client_id, code, redirect_uri, code_verifier, var_schema=var_schema, audience=audience)

https://auth.pieces.services/oauth/token [POST]

An endpoint to generate a OAuth Token for an authentication flow. 

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.embedded_model_schema import EmbeddedModelSchema
from openapi_client.models.o_auth_token import OAuthToken
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Auth0Api(api_client)
    grant_type = 'grant_type_example' # str | Denotes the flow you are using. For Authorization Code, use authorization_code or refresh_token.
    client_id = 'client_id_example' # str | Your application's Client ID.
    code = 'code_example' # str | The Authorization Code received from the initial /authorize call.
    redirect_uri = 'redirect_uri_example' # str | This is required only if it was set at the GET /authorize endpoint. The values must match.
    code_verifier = 'code_verifier_example' # str | Cryptographically random key that was used to generate the code_challenge passed to /authorize.
    var_schema = openapi_client.EmbeddedModelSchema() # EmbeddedModelSchema |  (optional)
    audience = 'audience_example' # str | The audience domain: i.e. https://pieces.us.auth0.com (optional)

    try:
        # https://auth.pieces.services/oauth/token [POST]
        api_response = api_instance.exchange_for_auth0_token(grant_type, client_id, code, redirect_uri, code_verifier, var_schema=var_schema, audience=audience)
        print("The response of Auth0Api->exchange_for_auth0_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Auth0Api->exchange_for_auth0_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| Denotes the flow you are using. For Authorization Code, use authorization_code or refresh_token. | 
 **client_id** | **str**| Your application&#39;s Client ID. | 
 **code** | **str**| The Authorization Code received from the initial /authorize call. | 
 **redirect_uri** | **str**| This is required only if it was set at the GET /authorize endpoint. The values must match. | 
 **code_verifier** | **str**| Cryptographically random key that was used to generate the code_challenge passed to /authorize. | 
 **var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md)|  | [optional] 
 **audience** | **str**| The audience domain: i.e. https://pieces.us.auth0.com | [optional] 

### Return type

[**OAuthToken**](OAuthToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth0_user_info**
> Auth0User get_auth0_user_info()

https://auth.pieces.services/userinfo [GET]

Get the users info from the Auth0 API

### Example

* OAuth Authentication (auth0):
* OAuth Authentication (auth0):
* OAuth Authentication (auth0):
```python
import time
import os
import openapi_client
from openapi_client.models.auth0_user import Auth0User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Auth0Api(api_client)

    try:
        # https://auth.pieces.services/userinfo [GET]
        api_response = api_instance.get_auth0_user_info()
        print("The response of Auth0Api->get_auth0_user_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Auth0Api->get_auth0_user_info: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Auth0User**](Auth0User.md)

### Authorization

[auth0](../README.md#auth0), [auth0](../README.md#auth0), [auth0](../README.md#auth0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

