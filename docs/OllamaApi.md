# pieces_os_client.OllamaApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ollama_install**](OllamaApi.md#ollama_install) | **POST** /ollama/install | /ollama/install [POST]
[**ollama_install_cancel**](OllamaApi.md#ollama_install_cancel) | **POST** /ollama/install/{identifier}/cancel | /ollama/install/{identifier}/cancel [POST]
[**ollama_install_snapshot**](OllamaApi.md#ollama_install_snapshot) | **GET** /ollama/install/{identifier} | /ollama/install/{identifier} [GET]
[**ollama_installs_snapshot**](OllamaApi.md#ollama_installs_snapshot) | **GET** /ollama/installs | /ollama/installs [GET]
[**ollama_status_check**](OllamaApi.md#ollama_status_check) | **GET** /ollama/status | /ollama/status [GET]
[**ollama_status_check_stream**](OllamaApi.md#ollama_status_check_stream) | **GET** /ollama/status/stream | /ollama/status/stream [WS]
[**ollama_uninstall**](OllamaApi.md#ollama_uninstall) | **POST** /ollama/uninstall | /ollama/uninstall [POST]
[**ollama_update**](OllamaApi.md#ollama_update) | **POST** /ollama/update | /ollama/update [POST]
[**ollama_update_cancel**](OllamaApi.md#ollama_update_cancel) | **POST** /ollama/update/{identifier}/cancel | /ollama/update/{identifier}/cancel [POST]
[**ollama_update_snapshot**](OllamaApi.md#ollama_update_snapshot) | **GET** /ollama/update/{identifier} | /ollama/update/{identifier} [GET]
[**ollama_updates_snapshot**](OllamaApi.md#ollama_updates_snapshot) | **GET** /ollama/updates | /ollama/updates [GET]


# **ollama_install**
> OllamaDeployment ollama_install()

/ollama/install [POST]

This will start the installation for ollama. NOTE: This will return immediately, use the update status

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.ollama_deployment import OllamaDeployment
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
    api_instance = pieces_os_client.OllamaApi(api_client)

    try:
        # /ollama/install [POST]
        api_response = api_instance.ollama_install()
        print("The response of OllamaApi->ollama_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OllamaApi->ollama_install: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**OllamaDeployment**](OllamaDeployment.md)

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

# **ollama_install_cancel**
> OllamaDeployment ollama_install_cancel(identifier)

/ollama/install/{identifier}/cancel [POST]

This will cancel a specific installation that is in-progress.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.ollama_deployment import OllamaDeployment
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
    api_instance = pieces_os_client.OllamaApi(api_client)
    identifier = 'identifier_example' # str | This is a identifier that is used to identify a specific generic event.

    try:
        # /ollama/install/{identifier}/cancel [POST]
        api_response = api_instance.ollama_install_cancel(identifier)
        print("The response of OllamaApi->ollama_install_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OllamaApi->ollama_install_cancel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| This is a identifier that is used to identify a specific generic event. | 

### Return type

[**OllamaDeployment**](OllamaDeployment.md)

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

# **ollama_install_snapshot**
> OllamaDeployment ollama_install_snapshot(identifier)

/ollama/install/{identifier} [GET]

This will get the status of a given installation

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.ollama_deployment import OllamaDeployment
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
    api_instance = pieces_os_client.OllamaApi(api_client)
    identifier = 'identifier_example' # str | This is a identifier that is used to identify a specific generic event.

    try:
        # /ollama/install/{identifier} [GET]
        api_response = api_instance.ollama_install_snapshot(identifier)
        print("The response of OllamaApi->ollama_install_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OllamaApi->ollama_install_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| This is a identifier that is used to identify a specific generic event. | 

### Return type

[**OllamaDeployment**](OllamaDeployment.md)

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

# **ollama_installs_snapshot**
> OllamaDeployments ollama_installs_snapshot()

/ollama/installs [GET]

This will return all the installation in a given session

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.ollama_deployments import OllamaDeployments
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
    api_instance = pieces_os_client.OllamaApi(api_client)

    try:
        # /ollama/installs [GET]
        api_response = api_instance.ollama_installs_snapshot()
        print("The response of OllamaApi->ollama_installs_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OllamaApi->ollama_installs_snapshot: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**OllamaDeployments**](OllamaDeployments.md)

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

# **ollama_status_check**
> OllamaStatus ollama_status_check()

/ollama/status [GET]

This will get a status on Ollama, ie if ollama is installed, if it needs an update,  if there are installations in progress, or updates in progress

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.ollama_status import OllamaStatus
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
    api_instance = pieces_os_client.OllamaApi(api_client)

    try:
        # /ollama/status [GET]
        api_response = api_instance.ollama_status_check()
        print("The response of OllamaApi->ollama_status_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OllamaApi->ollama_status_check: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**OllamaStatus**](OllamaStatus.md)

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

# **ollama_status_check_stream**
> OllamaStatus ollama_status_check_stream()

/ollama/status/stream [WS]

This provides a Websocket connection, that will emit a change on the initial connection and then all realtime updates: - if an update have started - if an installation has started - if Ollama has been installed/uninstalled - if an updated is required for Ollama

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.ollama_status import OllamaStatus
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
    api_instance = pieces_os_client.OllamaApi(api_client)

    try:
        # /ollama/status/stream [WS]
        api_response = api_instance.ollama_status_check_stream()
        print("The response of OllamaApi->ollama_status_check_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OllamaApi->ollama_status_check_stream: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**OllamaStatus**](OllamaStatus.md)

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

# **ollama_uninstall**
> OllamaDeployment ollama_uninstall(ollama_deployment=ollama_deployment)

/ollama/uninstall [POST]

This will uninstall Ollama.  NOTE: the request body is the installation that will be deleted.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.ollama_deployment import OllamaDeployment
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
    api_instance = pieces_os_client.OllamaApi(api_client)
    ollama_deployment = pieces_os_client.OllamaDeployment() # OllamaDeployment |  (optional)

    try:
        # /ollama/uninstall [POST]
        api_response = api_instance.ollama_uninstall(ollama_deployment=ollama_deployment)
        print("The response of OllamaApi->ollama_uninstall:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OllamaApi->ollama_uninstall: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ollama_deployment** | [**OllamaDeployment**](OllamaDeployment.md)|  | [optional] 

### Return type

[**OllamaDeployment**](OllamaDeployment.md)

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

# **ollama_update**
> OllamaDeployment ollama_update(ollama_deployment=ollama_deployment)

/ollama/update [POST]

This will start the update for ollama. NOTE: This will return immediately, use the ollama status endpoint to checks it status. NOTE: This will required a user to pass in deployment that they would like to update to.(only thing required will be version here, and that this is a valid version to update to.)

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.ollama_deployment import OllamaDeployment
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
    api_instance = pieces_os_client.OllamaApi(api_client)
    ollama_deployment = pieces_os_client.OllamaDeployment() # OllamaDeployment |  (optional)

    try:
        # /ollama/update [POST]
        api_response = api_instance.ollama_update(ollama_deployment=ollama_deployment)
        print("The response of OllamaApi->ollama_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OllamaApi->ollama_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ollama_deployment** | [**OllamaDeployment**](OllamaDeployment.md)|  | [optional] 

### Return type

[**OllamaDeployment**](OllamaDeployment.md)

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

# **ollama_update_cancel**
> OllamaDeployment ollama_update_cancel(identifier)

/ollama/update/{identifier}/cancel [POST]

This will cancel a specific update that is in-progress.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.ollama_deployment import OllamaDeployment
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
    api_instance = pieces_os_client.OllamaApi(api_client)
    identifier = 'identifier_example' # str | This is a identifier that is used to identify a specific generic event.

    try:
        # /ollama/update/{identifier}/cancel [POST]
        api_response = api_instance.ollama_update_cancel(identifier)
        print("The response of OllamaApi->ollama_update_cancel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OllamaApi->ollama_update_cancel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| This is a identifier that is used to identify a specific generic event. | 

### Return type

[**OllamaDeployment**](OllamaDeployment.md)

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

# **ollama_update_snapshot**
> OllamaDeployment ollama_update_snapshot(identifier)

/ollama/update/{identifier} [GET]

This will get the status of a given update.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.ollama_deployment import OllamaDeployment
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
    api_instance = pieces_os_client.OllamaApi(api_client)
    identifier = 'identifier_example' # str | This is a identifier that is used to identify a specific generic event.

    try:
        # /ollama/update/{identifier} [GET]
        api_response = api_instance.ollama_update_snapshot(identifier)
        print("The response of OllamaApi->ollama_update_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OllamaApi->ollama_update_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| This is a identifier that is used to identify a specific generic event. | 

### Return type

[**OllamaDeployment**](OllamaDeployment.md)

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

# **ollama_updates_snapshot**
> OllamaDeployments ollama_updates_snapshot()

/ollama/updates [GET]

This will return all the attempted updates in a given session

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.ollama_deployments import OllamaDeployments
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
    api_instance = pieces_os_client.OllamaApi(api_client)

    try:
        # /ollama/updates [GET]
        api_response = api_instance.ollama_updates_snapshot()
        print("The response of OllamaApi->ollama_updates_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OllamaApi->ollama_updates_snapshot: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**OllamaDeployments**](OllamaDeployments.md)

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

