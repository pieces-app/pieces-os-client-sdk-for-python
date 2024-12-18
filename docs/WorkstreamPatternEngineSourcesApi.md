# pieces_os_client.WorkstreamPatternEngineSourcesApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workstream_pattern_engine_search_sources**](WorkstreamPatternEngineSourcesApi.md#workstream_pattern_engine_search_sources) | **POST** /workstream_pattern_engine/sources/search | /workstream_pattern_engine/sources/search [POST]
[**workstream_pattern_engine_sources_create_new_source**](WorkstreamPatternEngineSourcesApi.md#workstream_pattern_engine_sources_create_new_source) | **POST** /workstream_pattern_engine/sources/create | /workstream_pattern_engine/sources/create [POST]
[**workstream_pattern_engine_sources_delete_specific_source**](WorkstreamPatternEngineSourcesApi.md#workstream_pattern_engine_sources_delete_specific_source) | **POST** /workstream_pattern_engine/sources/{source}/delete | /workstream_pattern_engine/sources/{source}/delete [POST]
[**workstream_pattern_engine_sources_snapshot**](WorkstreamPatternEngineSourcesApi.md#workstream_pattern_engine_sources_snapshot) | **GET** /workstream_pattern_engine/sources | /workstream_pattern_engine/sources [GET]
[**workstream_pattern_engine_sources_stream_identifiers**](WorkstreamPatternEngineSourcesApi.md#workstream_pattern_engine_sources_stream_identifiers) | **GET** /workstream_pattern_engine/sources/stream/identifiers | /workstream_pattern_engine/sources/stream/identifiers [WS]


# **workstream_pattern_engine_search_sources**
> SearchedIdentifiedWorkstreamPatternEngineSources workstream_pattern_engine_search_sources(transferables=transferables, search_input=search_input)

/workstream_pattern_engine/sources/search [POST]

This will search your workstream pattern engine sources

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.search_input import SearchInput
from pieces_os_client.models.searched_identified_workstream_pattern_engine_sources import SearchedIdentifiedWorkstreamPatternEngineSources
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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourcesApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    search_input = pieces_os_client.SearchInput() # SearchInput |  (optional)

    try:
        # /workstream_pattern_engine/sources/search [POST]
        api_response = api_instance.workstream_pattern_engine_search_sources(transferables=transferables, search_input=search_input)
        print("The response of WorkstreamPatternEngineSourcesApi->workstream_pattern_engine_search_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourcesApi->workstream_pattern_engine_search_sources: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **search_input** | [**SearchInput**](SearchInput.md)|  | [optional] 

### Return type

[**SearchedIdentifiedWorkstreamPatternEngineSources**](SearchedIdentifiedWorkstreamPatternEngineSources.md)

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

# **workstream_pattern_engine_sources_create_new_source**
> IdentifiedWorkstreamPatternEngineSource workstream_pattern_engine_sources_create_new_source(transferables=transferables, seeded_workstream_pattern_engine_source=seeded_workstream_pattern_engine_source)

/workstream_pattern_engine/sources/create [POST]

This will create a anchor and attach it to a specific asset(s) This will also ensure the anchor is normalized.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.identified_workstream_pattern_engine_source import IdentifiedWorkstreamPatternEngineSource
from pieces_os_client.models.seeded_workstream_pattern_engine_source import SeededWorkstreamPatternEngineSource
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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourcesApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    seeded_workstream_pattern_engine_source = pieces_os_client.SeededWorkstreamPatternEngineSource() # SeededWorkstreamPatternEngineSource |  (optional)

    try:
        # /workstream_pattern_engine/sources/create [POST]
        api_response = api_instance.workstream_pattern_engine_sources_create_new_source(transferables=transferables, seeded_workstream_pattern_engine_source=seeded_workstream_pattern_engine_source)
        print("The response of WorkstreamPatternEngineSourcesApi->workstream_pattern_engine_sources_create_new_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourcesApi->workstream_pattern_engine_sources_create_new_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **seeded_workstream_pattern_engine_source** | [**SeededWorkstreamPatternEngineSource**](SeededWorkstreamPatternEngineSource.md)|  | [optional] 

### Return type

[**IdentifiedWorkstreamPatternEngineSource**](IdentifiedWorkstreamPatternEngineSource.md)

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

# **workstream_pattern_engine_sources_delete_specific_source**
> workstream_pattern_engine_sources_delete_specific_source(source)

/workstream_pattern_engine/sources/{source}/delete [POST]

This will delete a specific workstream pattern engine source!

### Example

* Api Key Authentication (application):
```python
import time
import os
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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourcesApi(api_client)
    source = 'source_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSource

    try:
        # /workstream_pattern_engine/sources/{source}/delete [POST]
        api_instance.workstream_pattern_engine_sources_delete_specific_source(source)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourcesApi->workstream_pattern_engine_sources_delete_specific_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| This is a identifier that is used to identify a specific WorkstreamPatternEngineSource | 

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

# **workstream_pattern_engine_sources_snapshot**
> IdentifiedWorkstreamPatternEngineSources workstream_pattern_engine_sources_snapshot(transferables=transferables)

/workstream_pattern_engine/sources [GET]

This will get a snapshot of all your anchors.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.identified_workstream_pattern_engine_sources import IdentifiedWorkstreamPatternEngineSources
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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourcesApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /workstream_pattern_engine/sources [GET]
        api_response = api_instance.workstream_pattern_engine_sources_snapshot(transferables=transferables)
        print("The response of WorkstreamPatternEngineSourcesApi->workstream_pattern_engine_sources_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourcesApi->workstream_pattern_engine_sources_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**IdentifiedWorkstreamPatternEngineSources**](IdentifiedWorkstreamPatternEngineSources.md)

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

# **workstream_pattern_engine_sources_stream_identifiers**
> StreamedIdentifiers workstream_pattern_engine_sources_stream_identifiers()

/workstream_pattern_engine/sources/stream/identifiers [WS]

Provides a WebSocket connection that emits changes to your workstream-pattern-engine soures identifiers (UUIDs).

### Example

* Api Key Authentication (application):
```python
import time
import os
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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourcesApi(api_client)

    try:
        # /workstream_pattern_engine/sources/stream/identifiers [WS]
        api_response = api_instance.workstream_pattern_engine_sources_stream_identifiers()
        print("The response of WorkstreamPatternEngineSourcesApi->workstream_pattern_engine_sources_stream_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourcesApi->workstream_pattern_engine_sources_stream_identifiers: %s\n" % e)
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

