# pieces_os_client.AppletApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stream_applet_version**](AppletApi.md#stream_applet_version) | **GET** /os/applet/version/stream | /os/applet/version/stream [WS]


# **stream_applet_version**
> str stream_applet_version(application, applet_type)

/os/applet/version/stream [WS]

Establishes a WebSocket connection to stream real-time updates for the specified applet version based on application UUID and applet type.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.os_applet_enum import OSAppletEnum
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
    api_instance = pieces_os_client.AppletApi(api_client)
    application = 'application_example' # str | This is a uuid that represents an application
    applet_type = pieces_os_client.OSAppletEnum() # OSAppletEnum | The type of applet to stream version updates for. Must match a valid applet type name.

    try:
        # /os/applet/version/stream [WS]
        api_response = api_instance.stream_applet_version(application, applet_type)
        print("The response of AppletApi->stream_applet_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppletApi->stream_applet_version: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| This is a uuid that represents an application | 
 **applet_type** | [**OSAppletEnum**](.md)| The type of applet to stream version updates for. Must match a valid applet type name. | 

### Return type

**str**

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/websocket, application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WebSocket connection established successfully. |  -  |
**400** | Bad request due to missing or invalid query parameters. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

