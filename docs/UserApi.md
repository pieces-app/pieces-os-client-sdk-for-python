# pieces_os_client.UserApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_user**](UserApi.md#clear_user) | **POST** /user/clear | /user/clear
[**refresh_user**](UserApi.md#refresh_user) | **GET** /user/refresh | /user/refresh [GET]
[**select_user**](UserApi.md#select_user) | **POST** /user/select | /user/select [POST]
[**stream_user**](UserApi.md#stream_user) | **GET** /user/stream | /user/stream [WS]
[**stream_user_last_checked_in**](UserApi.md#stream_user_last_checked_in) | **GET** /user/last_checked_in/stream | /user/last_checked_in/stream [WS]
[**update_user**](UserApi.md#update_user) | **POST** /user/update | /user/update [POST]
[**user_access_token**](UserApi.md#user_access_token) | **GET** /user/access_token | &#39;/user/access_token&#39; [GET]
[**user_associate_entity**](UserApi.md#user_associate_entity) | **POST** /user/{user}/entities/associate/{entity} | /user/{user}/entities/associate/{entity} [POST]
[**user_beta_status**](UserApi.md#user_beta_status) | **POST** /user/beta/status | /user/beta/status [POST]
[**user_checkout**](UserApi.md#user_checkout) | **POST** /user/checkout | /user/checkout [POST]
[**user_disassociate_entity**](UserApi.md#user_disassociate_entity) | **POST** /user/{user}/entities/disassociate/{entity} | /user/{user}/entities/disassociate/{entity} [POST]
[**user_has_feature_access**](UserApi.md#user_has_feature_access) | **POST** /user/has_feature_access | /user/has_feature_access [POST]
[**user_manage_subscriptions**](UserApi.md#user_manage_subscriptions) | **POST** /user/manage/subscriptions | /user/manage/subscriptions [POST]
[**user_paddle_refresh**](UserApi.md#user_paddle_refresh) | **GET** /user/paddle/refresh | /user/paddle/refresh [GET]
[**user_providers**](UserApi.md#user_providers) | **GET** /user/providers | Your GET endpoint
[**user_snapshot**](UserApi.md#user_snapshot) | **GET** /user | /user [GET]
[**user_update_vanity**](UserApi.md#user_update_vanity) | **POST** /user/update/vanity | /user/update/vanity [POST]


# **clear_user**
> clear_user()

/user/clear

An endpoint to clear the current user. 

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)

    try:
        # /user/clear
        api_instance.clear_user()
    except Exception as e:
        print("Exception when calling UserApi->clear_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_user**
> UserProfile refresh_user()

/user/refresh [GET]

This will refresh a user.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.user_profile import UserProfile
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)

    try:
        # /user/refresh [GET]
        api_response = api_instance.refresh_user()
        print("The response of UserApi->refresh_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->refresh_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **select_user**
> UserProfile select_user(auth0_user=auth0_user)

/user/select [POST]

This will select the current user.

### Example

* OAuth Authentication (auth0):
* OAuth Authentication (auth0):
* OAuth Authentication (auth0):

```python
import pieces_os_client
from pieces_os_client.models.auth0_user import Auth0User
from pieces_os_client.models.user_profile import UserProfile
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)
    auth0_user = pieces_os_client.Auth0User() # Auth0User |  (optional)

    try:
        # /user/select [POST]
        api_response = api_instance.select_user(auth0_user=auth0_user)
        print("The response of UserApi->select_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->select_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth0_user** | [**Auth0User**](Auth0User.md)|  | [optional] 

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[auth0](../README.md#auth0), [auth0](../README.md#auth0), [auth0](../README.md#auth0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_user**
> UserProfile stream_user()

/user/stream [WS]

Provides a WebSocket connection that streams user data.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.user_profile import UserProfile
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)

    try:
        # /user/stream [WS]
        api_response = api_instance.stream_user()
        print("The response of UserApi->stream_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->stream_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_user_last_checked_in**
> UserLastCheckedInStreamOutput stream_user_last_checked_in()

/user/last_checked_in/stream [WS]

Provides a WebSocket connection that streams user last checked in data including userId, lastCheckedIn timestamp, and needsRefresh flag.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.user_last_checked_in_stream_output import UserLastCheckedInStreamOutput
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)

    try:
        # /user/last_checked_in/stream [WS]
        api_response = api_instance.stream_user_last_checked_in()
        print("The response of UserApi->stream_user_last_checked_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->stream_user_last_checked_in: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserLastCheckedInStreamOutput**](UserLastCheckedInStreamOutput.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserProfile update_user(user_profile=user_profile)

/user/update [POST]

This will update a specific user in the database.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.user_profile import UserProfile
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)
    user_profile = pieces_os_client.UserProfile() # UserProfile |  (optional)

    try:
        # /user/update [POST]
        api_response = api_instance.update_user(user_profile=user_profile)
        print("The response of UserApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_profile** | [**UserProfile**](UserProfile.md)|  | [optional] 

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_access_token**
> str user_access_token()

'/user/access_token' [GET]

This will return a user accessToken for usage w/ this user.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)

    try:
        # '/user/access_token' [GET]
        api_response = api_instance.user_access_token()
        print("The response of UserApi->user_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_access_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This will return the PKCE token. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_associate_entity**
> user_associate_entity(user, entity, entity_associate_to_user_input=entity_associate_to_user_input)

/user/{user}/entities/associate/{entity} [POST]

Creates an association between a User and an Entity.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.entity_associate_to_user_input import EntityAssociateToUserInput
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)
    user = '497f6eca-6276-4993-bfeb-53cbbbba6f08' # str | The id (uuid) for a specific user.
    entity = 'entity_example' # str | This is the uuid of an entity (organization or team).
    entity_associate_to_user_input = pieces_os_client.EntityAssociateToUserInput() # EntityAssociateToUserInput |  (optional)

    try:
        # /user/{user}/entities/associate/{entity} [POST]
        api_instance.user_associate_entity(user, entity, entity_associate_to_user_input=entity_associate_to_user_input)
    except Exception as e:
        print("Exception when calling UserApi->user_associate_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The id (uuid) for a specific user. | 
 **entity** | **str**| This is the uuid of an entity (organization or team). | 
 **entity_associate_to_user_input** | [**EntityAssociateToUserInput**](EntityAssociateToUserInput.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_beta_status**
> UserBetaStatus user_beta_status(user_beta_status=user_beta_status)

/user/beta/status [POST]

This will be an endpoint to give access or remove access immediately from a given user.(isomorphic from the given provider)

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.user_beta_status import UserBetaStatus
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)
    user_beta_status = pieces_os_client.UserBetaStatus() # UserBetaStatus |  (optional)

    try:
        # /user/beta/status [POST]
        api_response = api_instance.user_beta_status(user_beta_status=user_beta_status)
        print("The response of UserApi->user_beta_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_beta_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_beta_status** | [**UserBetaStatus**](UserBetaStatus.md)|  | [optional] 

### Return type

[**UserBetaStatus**](UserBetaStatus.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |
**511** | Authentication Required, This means that you user needs to be authenticated with OS in order to change the beta status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_checkout**
> UserCheckoutOutput user_checkout(user_checkout_input=user_checkout_input)

/user/checkout [POST]

Process user checkout operation. This endpoint is designed to be extensible for future checkout functionality.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.user_checkout_input import UserCheckoutInput
from pieces_os_client.models.user_checkout_output import UserCheckoutOutput
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)
    user_checkout_input = pieces_os_client.UserCheckoutInput() # UserCheckoutInput |  (optional)

    try:
        # /user/checkout [POST]
        api_response = api_instance.user_checkout(user_checkout_input=user_checkout_input)
        print("The response of UserApi->user_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_checkout_input** | [**UserCheckoutInput**](UserCheckoutInput.md)|  | [optional] 

### Return type

[**UserCheckoutOutput**](UserCheckoutOutput.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_disassociate_entity**
> user_disassociate_entity(user, entity)

/user/{user}/entities/disassociate/{entity} [POST]

Removes an association between a User and an Entity.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)
    user = '497f6eca-6276-4993-bfeb-53cbbbba6f08' # str | The id (uuid) for a specific user.
    entity = 'entity_example' # str | This is the uuid of an entity (organization or team).

    try:
        # /user/{user}/entities/disassociate/{entity} [POST]
        api_instance.user_disassociate_entity(user, entity)
    except Exception as e:
        print("Exception when calling UserApi->user_disassociate_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The id (uuid) for a specific user. | 
 **entity** | **str**| This is the uuid of an entity (organization or team). | 

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_has_feature_access**
> HasFeatureAccessOutput user_has_feature_access(has_feature_access_input)

/user/has_feature_access [POST]

Check if the current user has access to a specific feature with optional context.
This endpoint validates feature access based on the user's organization configuration
and optional context-specific requirements. The context is provided as nested optional models:
allowedCloudModels (for cloud model access validation), deniedWorkstreamPatternEngineSource
(for application/source denial checks), deniedWorkstreamPatternEngineWebsite (for website
denial checks), and processing (for processing capability validation).


### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.has_feature_access_input import HasFeatureAccessInput
from pieces_os_client.models.has_feature_access_output import HasFeatureAccessOutput
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)
    has_feature_access_input = pieces_os_client.HasFeatureAccessInput() # HasFeatureAccessInput | Input containing the feature to check and optional context for validation.

    try:
        # /user/has_feature_access [POST]
        api_response = api_instance.user_has_feature_access(has_feature_access_input)
        print("The response of UserApi->user_has_feature_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_has_feature_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **has_feature_access_input** | [**HasFeatureAccessInput**](HasFeatureAccessInput.md)| Input containing the feature to check and optional context for validation. | 

### Return type

[**HasFeatureAccessOutput**](HasFeatureAccessOutput.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request - Invalid input parameters or missing required context for the feature. |  -  |
**401** | Unauthorized - User is not authenticated. |  -  |
**404** | Not Found - User profile not found or feature does not exist. |  -  |
**422** | Unprocessable Entity - Invalid context provided for the requested feature. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_manage_subscriptions**
> UserManageSubscriptionsOutput user_manage_subscriptions(user_manage_subscriptions_input=user_manage_subscriptions_input)

/user/manage/subscriptions [POST]

Manage user subscriptions. This endpoint is designed to be extensible for future subscription management functionality.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.user_manage_subscriptions_input import UserManageSubscriptionsInput
from pieces_os_client.models.user_manage_subscriptions_output import UserManageSubscriptionsOutput
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)
    user_manage_subscriptions_input = pieces_os_client.UserManageSubscriptionsInput() # UserManageSubscriptionsInput |  (optional)

    try:
        # /user/manage/subscriptions [POST]
        api_response = api_instance.user_manage_subscriptions(user_manage_subscriptions_input=user_manage_subscriptions_input)
        print("The response of UserApi->user_manage_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_manage_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_manage_subscriptions_input** | [**UserManageSubscriptionsInput**](UserManageSubscriptionsInput.md)|  | [optional] 

### Return type

[**UserManageSubscriptionsOutput**](UserManageSubscriptionsOutput.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_paddle_refresh**
> RefreshedPaddleUser user_paddle_refresh()

/user/paddle/refresh [GET]

Get the latest payment/paddle information from the server and return user profile information.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.refreshed_paddle_user import RefreshedPaddleUser
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)

    try:
        # /user/paddle/refresh [GET]
        api_response = api_instance.user_paddle_refresh()
        print("The response of UserApi->user_paddle_refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_paddle_refresh: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RefreshedPaddleUser**](RefreshedPaddleUser.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_providers**
> ReturnedUserProfile user_providers()

Your GET endpoint

This will retrieve all the users Providers that are connected to this account.

If called locally. we will 501 - because it is not implemented locally yet.

If called in the cloud, we will refresh && get your access tokens to access these providers.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.returned_user_profile import ReturnedUserProfile
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)

    try:
        # Your GET endpoint
        api_response = api_instance.user_providers()
        print("The response of UserApi->user_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ReturnedUserProfile**](ReturnedUserProfile.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_snapshot**
> ReturnedUserProfile user_snapshot()

/user [GET]

This will return a snapshot of the current user. This will return our ReturnUserProfile and the user on that object is just a UserProfile and can potentially be null.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.returned_user_profile import ReturnedUserProfile
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)

    try:
        # /user [GET]
        api_response = api_instance.user_snapshot()
        print("The response of UserApi->user_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_snapshot: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ReturnedUserProfile**](ReturnedUserProfile.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update_vanity**
> UserProfile user_update_vanity(user_profile=user_profile)

/user/update/vanity [POST]

This is a local route to update your vanityname. ie mark.pieces.cloud, where "mark" is the vanityname.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.user_profile import UserProfile
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: application
configuration.api_key['application'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['application'] = 'Bearer'

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.UserApi(api_client)
    user_profile = pieces_os_client.UserProfile() # UserProfile | This will take an update userProfile, with the updated vanity name! (optional)

    try:
        # /user/update/vanity [POST]
        api_response = api_instance.user_update_vanity(user_profile=user_profile)
        print("The response of UserApi->user_update_vanity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_update_vanity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_profile** | [**UserProfile**](UserProfile.md)| This will take an update userProfile, with the updated vanity name! | [optional] 

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | The original dns record was not found, please wait for cloud connectivity to fully connect. |  -  |
**409** | Conflict, This means that we were unable to update the username because it was already taken. |  -  |
**500** | Unable to create a username. Internal Server Error. |  -  |
**511** | Network Authentication Required, Cannot Update the Vanityname of the user because the user is either not signed in or in not connected to the cloud. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

