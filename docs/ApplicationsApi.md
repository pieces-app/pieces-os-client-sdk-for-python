# pieces_os_client.ApplicationsApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_bulk_update_application_capabilities**](ApplicationsApi.md#applications_bulk_update_application_capabilities) | **POST** /applications/update/capabilities | /applications/update/capabilities [POST]
[**applications_external_related**](ApplicationsApi.md#applications_external_related) | **GET** /applications/external/related | /applications/external/related [GET]
[**applications_external_snapshot**](ApplicationsApi.md#applications_external_snapshot) | **GET** /applications/external | /applications/external [GET]
[**applications_register**](ApplicationsApi.md#applications_register) | **POST** /applications/register | /applications/register [POST]
[**applications_session_close**](ApplicationsApi.md#applications_session_close) | **POST** /applications/session/close | /applications/session/close [POST]
[**applications_session_open**](ApplicationsApi.md#applications_session_open) | **POST** /applications/session/open | /applications/session/open [POST]
[**applications_snapshot**](ApplicationsApi.md#applications_snapshot) | **GET** /applications | /applications [GET]
[**applications_stream_identifiers**](ApplicationsApi.md#applications_stream_identifiers) | **GET** /applications/stream/identifiers | /applications/stream/identifiers [WS]


# **applications_bulk_update_application_capabilities**
> Applications applications_bulk_update_application_capabilities(applications_bulk_update_capabilities_input=applications_bulk_update_capabilities_input)

/applications/update/capabilities [POST]

This will bulk update all our applications to have a set of specific capabilities(depending on the input)

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.applications import Applications
from pieces_os_client.models.applications_bulk_update_capabilities_input import ApplicationsBulkUpdateCapabilitiesInput
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)
    applications_bulk_update_capabilities_input = pieces_os_client.ApplicationsBulkUpdateCapabilitiesInput() # ApplicationsBulkUpdateCapabilitiesInput |  (optional)

    try:
        # /applications/update/capabilities [POST]
        api_response = api_instance.applications_bulk_update_application_capabilities(applications_bulk_update_capabilities_input=applications_bulk_update_capabilities_input)
        print("The response of ApplicationsApi->applications_bulk_update_application_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_bulk_update_application_capabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applications_bulk_update_capabilities_input** | [**ApplicationsBulkUpdateCapabilitiesInput**](ApplicationsBulkUpdateCapabilitiesInput.md)|  | [optional] 

### Return type

[**Applications**](Applications.md)

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

# **applications_external_related**
> DetectedExternalApplications applications_external_related()

/applications/external/related [GET]

Retrieves a list of external applications installed on the user's machine that have potential integrations with Pieces, including those not yet installed by the user and those anticipated to be supported in the future.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.detected_external_applications import DetectedExternalApplications
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)

    try:
        # /applications/external/related [GET]
        api_response = api_instance.applications_external_related()
        print("The response of ApplicationsApi->applications_external_related:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_external_related: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DetectedExternalApplications**](DetectedExternalApplications.md)

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

# **applications_external_snapshot**
> DetectedExternalApplications applications_external_snapshot()

/applications/external [GET]

Provides a snapshot of all external applications detected on the user's machine, such as Microsoft Teams classic, Google Chat, Obsidian, etc.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.detected_external_applications import DetectedExternalApplications
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)

    try:
        # /applications/external [GET]
        api_response = api_instance.applications_external_snapshot()
        print("The response of ApplicationsApi->applications_external_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_external_snapshot: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DetectedExternalApplications**](DetectedExternalApplications.md)

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

# **applications_register**
> Application applications_register(application=application)

/applications/register [POST]

Registers a new application within the Pieces ecosystem.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.application import Application
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)
    application = pieces_os_client.Application() # Application | This will accept a application. (optional)

    try:
        # /applications/register [POST]
        api_response = api_instance.applications_register(application=application)
        print("The response of ApplicationsApi->applications_register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | [**Application**](Application.md)| This will accept a application. | [optional] 

### Return type

[**Application**](Application.md)

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

# **applications_session_close**
> Session applications_session_close(body=body)

/applications/session/close [POST]

Closes an active session, identified by a session UUID, marking the end of the user's current interaction with the Pieces application.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.session import Session
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)
    body = 'body_example' # str | This will accept a required session uuid. (optional)

    try:
        # /applications/session/close [POST]
        api_response = api_instance.applications_session_close(body=body)
        print("The response of ApplicationsApi->applications_session_close:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_session_close: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| This will accept a required session uuid. | [optional] 

### Return type

[**Session**](Session.md)

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

# **applications_session_open**
> Session applications_session_open()

/applications/session/open [POST]

Initiates a new session, marking the start of a user's interaction with the Pieces application.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.session import Session
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)

    try:
        # /applications/session/open [POST]
        api_response = api_instance.applications_session_open()
        print("The response of ApplicationsApi->applications_session_open:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_session_open: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Session**](Session.md)

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

# **applications_snapshot**
> Applications applications_snapshot()

/applications [GET]

Retrieves a comprehensive overview of all applications tracked by the Pieces system, including status, version, and engagement metrics.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.applications import Applications
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)

    try:
        # /applications [GET]
        api_response = api_instance.applications_snapshot()
        print("The response of ApplicationsApi->applications_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_snapshot: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Applications**](Applications.md)

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

# **applications_stream_identifiers**
> StreamedIdentifiers applications_stream_identifiers()

/applications/stream/identifiers [WS]

Provides a WebSocket connection that emits changes to your application identifiers (UUIDs).

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.streamed_identifiers import StreamedIdentifiers
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)

    try:
        # /applications/stream/identifiers [WS]
        api_response = api_instance.applications_stream_identifiers()
        print("The response of ApplicationsApi->applications_stream_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_stream_identifiers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StreamedIdentifiers**](StreamedIdentifiers.md)

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

