# pieces_os_client.FoundryApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**foundry_install**](FoundryApi.md#foundry_install) | **POST** /foundry/install | /foundry/install [POST]
[**foundry_install_cancel**](FoundryApi.md#foundry_install_cancel) | **POST** /foundry/install/{identifier}/cancel | /foundry/install/{identifier}/cancel [POST]
[**foundry_install_snapshot**](FoundryApi.md#foundry_install_snapshot) | **GET** /foundry/install/{identifier} | /foundry/install/{identifier} [GET]
[**foundry_installs_snapshot**](FoundryApi.md#foundry_installs_snapshot) | **GET** /foundry/installs | /foundry/installs [GET]
[**foundry_status_check**](FoundryApi.md#foundry_status_check) | **GET** /foundry/status | /foundry/status [GET]
[**foundry_status_check_stream**](FoundryApi.md#foundry_status_check_stream) | **GET** /foundry/status/stream | /foundry/status/stream [WS]
[**foundry_uninstall**](FoundryApi.md#foundry_uninstall) | **POST** /foundry/uninstall | /foundry/uninstall [POST]
[**foundry_update**](FoundryApi.md#foundry_update) | **POST** /foundry/update | /foundry/update [POST]
[**foundry_update_cancel**](FoundryApi.md#foundry_update_cancel) | **POST** /foundry/update/{identifier}/cancel | /foundry/update/{identifier}/cancel [POST]
[**foundry_update_snapshot**](FoundryApi.md#foundry_update_snapshot) | **GET** /foundry/update/{identifier} | /foundry/update/{identifier} [GET]
[**foundry_updates_snapshot**](FoundryApi.md#foundry_updates_snapshot) | **GET** /foundry/updates | /foundry/updates [GET]


# **foundry_install**
> FoundryDeployment foundry_install()

/foundry/install [POST]

This will start the installation for foundry.
NOTE: This will return immediately, use the update status

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.foundry_deployment import FoundryDeployment
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
    api_instance = pieces_os_client.FoundryApi(api_client)

    try:
        # /foundry/install [POST]
        api_response = api_instance.foundry_install()
        print("The response of FoundryApi->foundry_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoundryApi->foundry_install: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FoundryDeployment**](FoundryDeployment.md)

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

# **foundry_install_cancel**
> FoundryDeployment foundry_install_cancel(identifier)

/foundry/install/{identifier}/cancel [POST]

This will cancel a specific installation that is in-progress.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.foundry_deployment import FoundryDeployment
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
    api_instance = pieces_os_client.FoundryApi(api_client)
    identifier = 'identifier_example' # str | This is a identifier that is used to identify a specific generic event.

    try:
        # /foundry/install/{identifier}/cancel [POST]
        api_response = api_instance.foundry_install_cancel(identifier)
        print("The response of FoundryApi->foundry_install_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoundryApi->foundry_install_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| This is a identifier that is used to identify a specific generic event. | 

### Return type

[**FoundryDeployment**](FoundryDeployment.md)

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

# **foundry_install_snapshot**
> FoundryDeployment foundry_install_snapshot(identifier)

/foundry/install/{identifier} [GET]

This will get the status of a given installation

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.foundry_deployment import FoundryDeployment
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
    api_instance = pieces_os_client.FoundryApi(api_client)
    identifier = 'identifier_example' # str | This is a identifier that is used to identify a specific generic event.

    try:
        # /foundry/install/{identifier} [GET]
        api_response = api_instance.foundry_install_snapshot(identifier)
        print("The response of FoundryApi->foundry_install_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoundryApi->foundry_install_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| This is a identifier that is used to identify a specific generic event. | 

### Return type

[**FoundryDeployment**](FoundryDeployment.md)

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

# **foundry_installs_snapshot**
> FoundryDeployments foundry_installs_snapshot()

/foundry/installs [GET]

This will return all the installation in a given session

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.foundry_deployments import FoundryDeployments
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
    api_instance = pieces_os_client.FoundryApi(api_client)

    try:
        # /foundry/installs [GET]
        api_response = api_instance.foundry_installs_snapshot()
        print("The response of FoundryApi->foundry_installs_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoundryApi->foundry_installs_snapshot: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FoundryDeployments**](FoundryDeployments.md)

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

# **foundry_status_check**
> FoundryStatus foundry_status_check()

/foundry/status [GET]

This will get a status on foundry, ie if ollama is installed, if it needs an update, 
if there are installations in progress, or updates in progress

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.foundry_status import FoundryStatus
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
    api_instance = pieces_os_client.FoundryApi(api_client)

    try:
        # /foundry/status [GET]
        api_response = api_instance.foundry_status_check()
        print("The response of FoundryApi->foundry_status_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoundryApi->foundry_status_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FoundryStatus**](FoundryStatus.md)

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

# **foundry_status_check_stream**
> FoundryStatus foundry_status_check_stream()

/foundry/status/stream [WS]

This provides a Websocket connection, that will emit a change on the initial connection and then all realtime updates:
- if an update have started
- if an installation has started
- if foundry has been installed/uninstalled
- if an updated is required for Ollama

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.foundry_status import FoundryStatus
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
    api_instance = pieces_os_client.FoundryApi(api_client)

    try:
        # /foundry/status/stream [WS]
        api_response = api_instance.foundry_status_check_stream()
        print("The response of FoundryApi->foundry_status_check_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoundryApi->foundry_status_check_stream: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FoundryStatus**](FoundryStatus.md)

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

# **foundry_uninstall**
> FoundryDeployment foundry_uninstall(foundry_deployment=foundry_deployment)

/foundry/uninstall [POST]

This will uninstall foundry.

NOTE: the request body is the installation that will be deleted.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.foundry_deployment import FoundryDeployment
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
    api_instance = pieces_os_client.FoundryApi(api_client)
    foundry_deployment = pieces_os_client.FoundryDeployment() # FoundryDeployment |  (optional)

    try:
        # /foundry/uninstall [POST]
        api_response = api_instance.foundry_uninstall(foundry_deployment=foundry_deployment)
        print("The response of FoundryApi->foundry_uninstall:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoundryApi->foundry_uninstall: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foundry_deployment** | [**FoundryDeployment**](FoundryDeployment.md)|  | [optional] 

### Return type

[**FoundryDeployment**](FoundryDeployment.md)

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

# **foundry_update**
> FoundryDeployment foundry_update(foundry_deployment=foundry_deployment)

/foundry/update [POST]

This will start the update for Foundry.
NOTE: This will return immediately, use the Foundry status endpoint to checks it status.
NOTE: This will required a user to pass in deployment that they would like to update to.(only thing required will be version here, and that this is a valid version to update to.)

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.foundry_deployment import FoundryDeployment
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
    api_instance = pieces_os_client.FoundryApi(api_client)
    foundry_deployment = pieces_os_client.FoundryDeployment() # FoundryDeployment |  (optional)

    try:
        # /foundry/update [POST]
        api_response = api_instance.foundry_update(foundry_deployment=foundry_deployment)
        print("The response of FoundryApi->foundry_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoundryApi->foundry_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foundry_deployment** | [**FoundryDeployment**](FoundryDeployment.md)|  | [optional] 

### Return type

[**FoundryDeployment**](FoundryDeployment.md)

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

# **foundry_update_cancel**
> FoundryDeployment foundry_update_cancel(identifier)

/foundry/update/{identifier}/cancel [POST]

This will cancel a specific update that is in-progress.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.foundry_deployment import FoundryDeployment
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
    api_instance = pieces_os_client.FoundryApi(api_client)
    identifier = 'identifier_example' # str | This is a identifier that is used to identify a specific generic event.

    try:
        # /foundry/update/{identifier}/cancel [POST]
        api_response = api_instance.foundry_update_cancel(identifier)
        print("The response of FoundryApi->foundry_update_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoundryApi->foundry_update_cancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| This is a identifier that is used to identify a specific generic event. | 

### Return type

[**FoundryDeployment**](FoundryDeployment.md)

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

# **foundry_update_snapshot**
> FoundryDeployment foundry_update_snapshot(identifier)

/foundry/update/{identifier} [GET]

This will get the status of a given update.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.foundry_deployment import FoundryDeployment
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
    api_instance = pieces_os_client.FoundryApi(api_client)
    identifier = 'identifier_example' # str | This is a identifier that is used to identify a specific generic event.

    try:
        # /foundry/update/{identifier} [GET]
        api_response = api_instance.foundry_update_snapshot(identifier)
        print("The response of FoundryApi->foundry_update_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoundryApi->foundry_update_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| This is a identifier that is used to identify a specific generic event. | 

### Return type

[**FoundryDeployment**](FoundryDeployment.md)

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

# **foundry_updates_snapshot**
> FoundryDeployments foundry_updates_snapshot()

/foundry/updates [GET]

This will return all the attempted updates in a given session

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.foundry_deployments import FoundryDeployments
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
    api_instance = pieces_os_client.FoundryApi(api_client)

    try:
        # /foundry/updates [GET]
        api_response = api_instance.foundry_updates_snapshot()
        print("The response of FoundryApi->foundry_updates_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoundryApi->foundry_updates_snapshot: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FoundryDeployments**](FoundryDeployments.md)

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

