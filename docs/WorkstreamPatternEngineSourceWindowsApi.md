# pieces_os_client.WorkstreamPatternEngineSourceWindowsApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workstream_pattern_engine_source_window_create_new_source_window**](WorkstreamPatternEngineSourceWindowsApi.md#workstream_pattern_engine_source_window_create_new_source_window) | **POST** /workstream_pattern_engine/source_windows/create | /workstream_pattern_engine/source_windows/create [POST]
[**workstream_pattern_engine_source_window_delete_specific_source_window**](WorkstreamPatternEngineSourceWindowsApi.md#workstream_pattern_engine_source_window_delete_specific_source_window) | **POST** /workstream_pattern_engine/source_windows/{source_window}/delete | /workstream_pattern_engine/source_windows/{source_window}/delete [POST]
[**workstream_pattern_engine_source_windows_search**](WorkstreamPatternEngineSourceWindowsApi.md#workstream_pattern_engine_source_windows_search) | **POST** /workstream_pattern_engine/source_windows/search | /workstream_pattern_engine/source_windows/search [POST]
[**workstream_pattern_engine_source_windows_snapshot**](WorkstreamPatternEngineSourceWindowsApi.md#workstream_pattern_engine_source_windows_snapshot) | **GET** /workstream_pattern_engine/source_windows | /workstream_pattern_engine/source_windows [GET]
[**workstream_pattern_engine_source_windows_stream_identifiers**](WorkstreamPatternEngineSourceWindowsApi.md#workstream_pattern_engine_source_windows_stream_identifiers) | **GET** /workstream_pattern_engine/source_windows/stream/identifiers | /workstream_pattern_engine/source_windows/stream/identifiers [WS]


# **workstream_pattern_engine_source_window_create_new_source_window**
> WorkstreamPatternEngineSourceWindow workstream_pattern_engine_source_window_create_new_source_window(transferables=transferables, seeded_workstream_pattern_engine_source_window=seeded_workstream_pattern_engine_source_window)

/workstream_pattern_engine/source_windows/create [POST]

This will enable us to create a source window for the workstream pattern engine.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.seeded_workstream_pattern_engine_source_window import SeededWorkstreamPatternEngineSourceWindow
from pieces_os_client.models.workstream_pattern_engine_source_window import WorkstreamPatternEngineSourceWindow
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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceWindowsApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    seeded_workstream_pattern_engine_source_window = pieces_os_client.SeededWorkstreamPatternEngineSourceWindow() # SeededWorkstreamPatternEngineSourceWindow |  (optional)

    try:
        # /workstream_pattern_engine/source_windows/create [POST]
        api_response = api_instance.workstream_pattern_engine_source_window_create_new_source_window(transferables=transferables, seeded_workstream_pattern_engine_source_window=seeded_workstream_pattern_engine_source_window)
        print("The response of WorkstreamPatternEngineSourceWindowsApi->workstream_pattern_engine_source_window_create_new_source_window:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceWindowsApi->workstream_pattern_engine_source_window_create_new_source_window: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **seeded_workstream_pattern_engine_source_window** | [**SeededWorkstreamPatternEngineSourceWindow**](SeededWorkstreamPatternEngineSourceWindow.md)|  | [optional] 

### Return type

[**WorkstreamPatternEngineSourceWindow**](WorkstreamPatternEngineSourceWindow.md)

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

# **workstream_pattern_engine_source_window_delete_specific_source_window**
> workstream_pattern_engine_source_window_delete_specific_source_window(source_window)

/workstream_pattern_engine/source_windows/{source_window}/delete [POST]

This will enable us to delete a source window from the workstream pattern engine.

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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceWindowsApi(api_client)
    source_window = 'source_window_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow

    try:
        # /workstream_pattern_engine/source_windows/{source_window}/delete [POST]
        api_instance.workstream_pattern_engine_source_window_delete_specific_source_window(source_window)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceWindowsApi->workstream_pattern_engine_source_window_delete_specific_source_window: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_window** | **str**| This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow | 

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

# **workstream_pattern_engine_source_windows_search**
> SearchedWorkstreamPatternEngineSourceWindows workstream_pattern_engine_source_windows_search(search_input=search_input)

/workstream_pattern_engine/source_windows/search [POST]

This will enable us to search for source windows for the workstream pattern engine.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.search_input import SearchInput
from pieces_os_client.models.searched_workstream_pattern_engine_source_windows import SearchedWorkstreamPatternEngineSourceWindows
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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceWindowsApi(api_client)
    search_input = pieces_os_client.SearchInput() # SearchInput |  (optional)

    try:
        # /workstream_pattern_engine/source_windows/search [POST]
        api_response = api_instance.workstream_pattern_engine_source_windows_search(search_input=search_input)
        print("The response of WorkstreamPatternEngineSourceWindowsApi->workstream_pattern_engine_source_windows_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceWindowsApi->workstream_pattern_engine_source_windows_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_input** | [**SearchInput**](SearchInput.md)|  | [optional] 

### Return type

[**SearchedWorkstreamPatternEngineSourceWindows**](SearchedWorkstreamPatternEngineSourceWindows.md)

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

# **workstream_pattern_engine_source_windows_snapshot**
> WorkstreamPatternEngineSourceWindows workstream_pattern_engine_source_windows_snapshot(transferables=transferables)

/workstream_pattern_engine/source_windows [GET]

This will enable us to snapshot the source windows for the workstream pattern engine.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.workstream_pattern_engine_source_windows import WorkstreamPatternEngineSourceWindows
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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceWindowsApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /workstream_pattern_engine/source_windows [GET]
        api_response = api_instance.workstream_pattern_engine_source_windows_snapshot(transferables=transferables)
        print("The response of WorkstreamPatternEngineSourceWindowsApi->workstream_pattern_engine_source_windows_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceWindowsApi->workstream_pattern_engine_source_windows_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**WorkstreamPatternEngineSourceWindows**](WorkstreamPatternEngineSourceWindows.md)

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

# **workstream_pattern_engine_source_windows_stream_identifiers**
> StreamedIdentifiers workstream_pattern_engine_source_windows_stream_identifiers()

/workstream_pattern_engine/source_windows/stream/identifiers [WS]

This will enable us to stream the identifiers for the workstream pattern engine source windows.

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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceWindowsApi(api_client)

    try:
        # /workstream_pattern_engine/source_windows/stream/identifiers [WS]
        api_response = api_instance.workstream_pattern_engine_source_windows_stream_identifiers()
        print("The response of WorkstreamPatternEngineSourceWindowsApi->workstream_pattern_engine_source_windows_stream_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceWindowsApi->workstream_pattern_engine_source_windows_stream_identifiers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StreamedIdentifiers**](StreamedIdentifiers.md)

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

