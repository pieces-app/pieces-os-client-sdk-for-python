# pieces_os_client.WorkstreamPatternEngineSourceApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workstream_pattern_engine_source_scores_increment**](WorkstreamPatternEngineSourceApi.md#workstream_pattern_engine_source_scores_increment) | **POST** /workstream_pattern_engine/source/{source}/scores/increment | &#39;/workstream_pattern_engine/source/{source}/scores/increment&#39; [POST]
[**workstream_pattern_engine_source_update**](WorkstreamPatternEngineSourceApi.md#workstream_pattern_engine_source_update) | **POST** /workstream_pattern_engine/source/update | /workstream_pattern_engine/source/update [POST]
[**workstream_pattern_engine_sources_specific_source_snapshot**](WorkstreamPatternEngineSourceApi.md#workstream_pattern_engine_sources_specific_source_snapshot) | **GET** /workstream_pattern_engine/source/{source} | /workstream_pattern_engine/source/{source} [GET]


# **workstream_pattern_engine_source_scores_increment**
> workstream_pattern_engine_source_scores_increment(source, seeded_score_increment=seeded_score_increment)

'/workstream_pattern_engine/source/{source}/scores/increment' [POST]

This will take in a SeededScoreIncrement and will increment the material relative to the incoming body.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.seeded_score_increment import SeededScoreIncrement
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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceApi(api_client)
    source = 'source_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSource
    seeded_score_increment = pieces_os_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # '/workstream_pattern_engine/source/{source}/scores/increment' [POST]
        api_instance.workstream_pattern_engine_source_scores_increment(source, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceApi->workstream_pattern_engine_source_scores_increment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| This is a identifier that is used to identify a specific WorkstreamPatternEngineSource | 
 **seeded_score_increment** | [**SeededScoreIncrement**](SeededScoreIncrement.md)|  | [optional] 

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

# **workstream_pattern_engine_source_update**
> IdentifiedWorkstreamPatternEngineSource workstream_pattern_engine_source_update(transferables=transferables, identified_workstream_pattern_engine_source=identified_workstream_pattern_engine_source)

/workstream_pattern_engine/source/update [POST]

This will update a specific workstream pattern engine source.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.identified_workstream_pattern_engine_source import IdentifiedWorkstreamPatternEngineSource
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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    identified_workstream_pattern_engine_source = pieces_os_client.IdentifiedWorkstreamPatternEngineSource() # IdentifiedWorkstreamPatternEngineSource |  (optional)

    try:
        # /workstream_pattern_engine/source/update [POST]
        api_response = api_instance.workstream_pattern_engine_source_update(transferables=transferables, identified_workstream_pattern_engine_source=identified_workstream_pattern_engine_source)
        print("The response of WorkstreamPatternEngineSourceApi->workstream_pattern_engine_source_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceApi->workstream_pattern_engine_source_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **identified_workstream_pattern_engine_source** | [**IdentifiedWorkstreamPatternEngineSource**](IdentifiedWorkstreamPatternEngineSource.md)|  | [optional] 

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

# **workstream_pattern_engine_sources_specific_source_snapshot**
> IdentifiedWorkstreamPatternEngineSource workstream_pattern_engine_sources_specific_source_snapshot(source, transferables=transferables)

/workstream_pattern_engine/source/{source} [GET]

This will get a snapshot of a single workstream pattern engine source.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.identified_workstream_pattern_engine_source import IdentifiedWorkstreamPatternEngineSource
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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceApi(api_client)
    source = 'source_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSource
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /workstream_pattern_engine/source/{source} [GET]
        api_response = api_instance.workstream_pattern_engine_sources_specific_source_snapshot(source, transferables=transferables)
        print("The response of WorkstreamPatternEngineSourceApi->workstream_pattern_engine_sources_specific_source_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceApi->workstream_pattern_engine_sources_specific_source_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| This is a identifier that is used to identify a specific WorkstreamPatternEngineSource | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**IdentifiedWorkstreamPatternEngineSource**](IdentifiedWorkstreamPatternEngineSource.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**410** | Workstream pattern Engine source not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
