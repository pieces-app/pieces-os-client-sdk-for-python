# pieces_os_client.TunnelApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tunnel_connect**](TunnelApi.md#tunnel_connect) | **POST** /tunnel/connect | /tunnel/connect [POST]
[**tunnel_disconnect**](TunnelApi.md#tunnel_disconnect) | **POST** /tunnel/disconnect | /tunnel/disconnect [POST]
[**tunnel_get_status**](TunnelApi.md#tunnel_get_status) | **GET** /tunnel/status | /tunnel/status [GET]
[**tunnel_refresh**](TunnelApi.md#tunnel_refresh) | **POST** /tunnel/refresh | /tunnel/refresh [POST]


# **tunnel_connect**
> TunnelConnectionOutput tunnel_connect(tunnel_connection_input)

/tunnel/connect [POST]

Establishes a new tunnel connection.


### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.tunnel_connection_input import TunnelConnectionInput
from pieces_os_client.models.tunnel_connection_output import TunnelConnectionOutput
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
    api_instance = pieces_os_client.TunnelApi(api_client)
    tunnel_connection_input = pieces_os_client.TunnelConnectionInput() # TunnelConnectionInput | 

    try:
        # /tunnel/connect [POST]
        api_response = api_instance.tunnel_connect(tunnel_connection_input)
        print("The response of TunnelApi->tunnel_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TunnelApi->tunnel_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tunnel_connection_input** | [**TunnelConnectionInput**](TunnelConnectionInput.md)|  | 

### Return type

[**TunnelConnectionOutput**](TunnelConnectionOutput.md)

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
**511** | Unauthenticated - auth required. |  -  |
**592** | A valid Subscription required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tunnel_disconnect**
> TunnelDisconnectionOutput tunnel_disconnect(tunnel_disconnection_input)

/tunnel/disconnect [POST]

Disconnects tunnel connections.


### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.tunnel_disconnection_input import TunnelDisconnectionInput
from pieces_os_client.models.tunnel_disconnection_output import TunnelDisconnectionOutput
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
    api_instance = pieces_os_client.TunnelApi(api_client)
    tunnel_disconnection_input = pieces_os_client.TunnelDisconnectionInput() # TunnelDisconnectionInput | 

    try:
        # /tunnel/disconnect [POST]
        api_response = api_instance.tunnel_disconnect(tunnel_disconnection_input)
        print("The response of TunnelApi->tunnel_disconnect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TunnelApi->tunnel_disconnect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tunnel_disconnection_input** | [**TunnelDisconnectionInput**](TunnelDisconnectionInput.md)|  | 

### Return type

[**TunnelDisconnectionOutput**](TunnelDisconnectionOutput.md)

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

# **tunnel_get_status**
> TunnelStatus tunnel_get_status()

/tunnel/status [GET]

Retrieves the current status of all tunnels and connections.
This includes active tunnels and version information.


### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.tunnel_status import TunnelStatus
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
    api_instance = pieces_os_client.TunnelApi(api_client)

    try:
        # /tunnel/status [GET]
        api_response = api_instance.tunnel_get_status()
        print("The response of TunnelApi->tunnel_get_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TunnelApi->tunnel_get_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TunnelStatus**](TunnelStatus.md)

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

# **tunnel_refresh**
> TunnelRefreshOutput tunnel_refresh(tunnel_refresh_input)

/tunnel/refresh [POST]

Refreshes tunnel connection(s) to maintain connectivity.

This will also update the users auth_token for the specific connection.


### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.tunnel_refresh_input import TunnelRefreshInput
from pieces_os_client.models.tunnel_refresh_output import TunnelRefreshOutput
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
    api_instance = pieces_os_client.TunnelApi(api_client)
    tunnel_refresh_input = pieces_os_client.TunnelRefreshInput() # TunnelRefreshInput | 

    try:
        # /tunnel/refresh [POST]
        api_response = api_instance.tunnel_refresh(tunnel_refresh_input)
        print("The response of TunnelApi->tunnel_refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TunnelApi->tunnel_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tunnel_refresh_input** | [**TunnelRefreshInput**](TunnelRefreshInput.md)|  | 

### Return type

[**TunnelRefreshOutput**](TunnelRefreshOutput.md)

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
**511** | Unauthenticated - auth required. |  -  |
**592** | A valid Subscription required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

