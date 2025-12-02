# pieces_os_client.WorkstreamPatternEngineSourceWindowApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workstream_pattern_engine_source_window_associate_tag**](WorkstreamPatternEngineSourceWindowApi.md#workstream_pattern_engine_source_window_associate_tag) | **POST** /workstream_pattern_engine/source_window/{source_window}/tags/associate/{tag} | /workstream_pattern_engine/source_window/{source_window}/tags/associate/{tag} [POST]
[**workstream_pattern_engine_source_window_associate_website**](WorkstreamPatternEngineSourceWindowApi.md#workstream_pattern_engine_source_window_associate_website) | **POST** /workstream_pattern_engine/source_window/{source_window}/websites/associate/{website} | /workstream_pattern_engine/source_window/{source_window}/websites/associate/{website} [POST]
[**workstream_pattern_engine_source_window_associate_workstream_event**](WorkstreamPatternEngineSourceWindowApi.md#workstream_pattern_engine_source_window_associate_workstream_event) | **POST** /workstream_pattern_engine/source_window/{source_window}/workstream_events/associate/{workstream_event} | /workstream_pattern_engine/source_window/{source_window}/workstream_events/associate/{workstream_event} [POST]
[**workstream_pattern_engine_source_window_disassociate_tag**](WorkstreamPatternEngineSourceWindowApi.md#workstream_pattern_engine_source_window_disassociate_tag) | **POST** /workstream_pattern_engine/source_window/{source_window}/tags/disassociate/{tag} | /workstream_pattern_engine/source_window/{source_window}/tags/disassociate/{tag} [POST]
[**workstream_pattern_engine_source_window_disassociate_website**](WorkstreamPatternEngineSourceWindowApi.md#workstream_pattern_engine_source_window_disassociate_website) | **POST** /workstream_pattern_engine/source_window/{source_window}/websites/disassociate/{website} | /workstream_pattern_engine/source_window/{source_window}/websites/disassociate/{website} [POST]
[**workstream_pattern_engine_source_window_disassociate_workstream_event**](WorkstreamPatternEngineSourceWindowApi.md#workstream_pattern_engine_source_window_disassociate_workstream_event) | **POST** /workstream_pattern_engine/source_window/{source_window}/workstream_events/disassociate/{workstream_event} | /workstream_pattern_engine/source_window/{source_window}/workstream_events/disassociate/{workstream_event} [POST]
[**workstream_pattern_engine_source_window_scores_increment**](WorkstreamPatternEngineSourceWindowApi.md#workstream_pattern_engine_source_window_scores_increment) | **POST** /workstream_pattern_engine/source_window/{source_window}/scores/increment | /workstream_pattern_engine/source_window/{source_window}/scores/increment [POST]
[**workstream_pattern_engine_source_window_specific_source_window_snapshot**](WorkstreamPatternEngineSourceWindowApi.md#workstream_pattern_engine_source_window_specific_source_window_snapshot) | **GET** /workstream_pattern_engine/source_window/{source_window} | /workstream_pattern_engine/source_window/{source_window} [GET]
[**workstream_pattern_engine_source_window_update**](WorkstreamPatternEngineSourceWindowApi.md#workstream_pattern_engine_source_window_update) | **POST** /workstream_pattern_engine/source_window/update | /workstream_pattern_engine/source_window/update [POST]


# **workstream_pattern_engine_source_window_associate_tag**
> workstream_pattern_engine_source_window_associate_tag(source_window, tag)

/workstream_pattern_engine/source_window/{source_window}/tags/associate/{tag} [POST]

This will enable us to associate a tag with a source window.

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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceWindowApi(api_client)
    source_window = 'source_window_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow
    tag = 'tag_example' # str | tag id

    try:
        # /workstream_pattern_engine/source_window/{source_window}/tags/associate/{tag} [POST]
        api_instance.workstream_pattern_engine_source_window_associate_tag(source_window, tag)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceWindowApi->workstream_pattern_engine_source_window_associate_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_window** | **str**| This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow | 
 **tag** | **str**| tag id | 

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

# **workstream_pattern_engine_source_window_associate_website**
> workstream_pattern_engine_source_window_associate_website(source_window, website)

/workstream_pattern_engine/source_window/{source_window}/websites/associate/{website} [POST]

This will enable us to associate a website with a source window.

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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceWindowApi(api_client)
    source_window = 'source_window_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow
    website = 'website_example' # str | website id

    try:
        # /workstream_pattern_engine/source_window/{source_window}/websites/associate/{website} [POST]
        api_instance.workstream_pattern_engine_source_window_associate_website(source_window, website)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceWindowApi->workstream_pattern_engine_source_window_associate_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_window** | **str**| This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow | 
 **website** | **str**| website id | 

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

# **workstream_pattern_engine_source_window_associate_workstream_event**
> workstream_pattern_engine_source_window_associate_workstream_event(source_window, workstream_event)

/workstream_pattern_engine/source_window/{source_window}/workstream_events/associate/{workstream_event} [POST]

This will enable us to associate a workstream event with a source window.

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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceWindowApi(api_client)
    source_window = 'source_window_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.

    try:
        # /workstream_pattern_engine/source_window/{source_window}/workstream_events/associate/{workstream_event} [POST]
        api_instance.workstream_pattern_engine_source_window_associate_workstream_event(source_window, workstream_event)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceWindowApi->workstream_pattern_engine_source_window_associate_workstream_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_window** | **str**| This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow | 
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 

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

# **workstream_pattern_engine_source_window_disassociate_tag**
> workstream_pattern_engine_source_window_disassociate_tag(source_window, tag)

/workstream_pattern_engine/source_window/{source_window}/tags/disassociate/{tag} [POST]

This will enable us to disassociate a tag from a source window.

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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceWindowApi(api_client)
    source_window = 'source_window_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow
    tag = 'tag_example' # str | tag id

    try:
        # /workstream_pattern_engine/source_window/{source_window}/tags/disassociate/{tag} [POST]
        api_instance.workstream_pattern_engine_source_window_disassociate_tag(source_window, tag)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceWindowApi->workstream_pattern_engine_source_window_disassociate_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_window** | **str**| This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow | 
 **tag** | **str**| tag id | 

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

# **workstream_pattern_engine_source_window_disassociate_website**
> workstream_pattern_engine_source_window_disassociate_website(source_window, website)

/workstream_pattern_engine/source_window/{source_window}/websites/disassociate/{website} [POST]

This will enable us to disassociate a website from a source window.

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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceWindowApi(api_client)
    source_window = 'source_window_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow
    website = 'website_example' # str | website id

    try:
        # /workstream_pattern_engine/source_window/{source_window}/websites/disassociate/{website} [POST]
        api_instance.workstream_pattern_engine_source_window_disassociate_website(source_window, website)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceWindowApi->workstream_pattern_engine_source_window_disassociate_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_window** | **str**| This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow | 
 **website** | **str**| website id | 

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

# **workstream_pattern_engine_source_window_disassociate_workstream_event**
> workstream_pattern_engine_source_window_disassociate_workstream_event(source_window, workstream_event)

/workstream_pattern_engine/source_window/{source_window}/workstream_events/disassociate/{workstream_event} [POST]

This will enable us to disassociate a workstream event from a source window.

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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceWindowApi(api_client)
    source_window = 'source_window_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.

    try:
        # /workstream_pattern_engine/source_window/{source_window}/workstream_events/disassociate/{workstream_event} [POST]
        api_instance.workstream_pattern_engine_source_window_disassociate_workstream_event(source_window, workstream_event)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceWindowApi->workstream_pattern_engine_source_window_disassociate_workstream_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_window** | **str**| This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow | 
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 

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

# **workstream_pattern_engine_source_window_scores_increment**
> workstream_pattern_engine_source_window_scores_increment(source_window, seeded_score_increment=seeded_score_increment)

/workstream_pattern_engine/source_window/{source_window}/scores/increment [POST]

This will enable us to increment the scores for the workstream pattern engine source window.

### Example

* Api Key Authentication (application):

```python
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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceWindowApi(api_client)
    source_window = 'source_window_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow
    seeded_score_increment = pieces_os_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # /workstream_pattern_engine/source_window/{source_window}/scores/increment [POST]
        api_instance.workstream_pattern_engine_source_window_scores_increment(source_window, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceWindowApi->workstream_pattern_engine_source_window_scores_increment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_window** | **str**| This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow | 
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

# **workstream_pattern_engine_source_window_specific_source_window_snapshot**
> WorkstreamPatternEngineSourceWindow workstream_pattern_engine_source_window_specific_source_window_snapshot(source_window, transferables=transferables)

/workstream_pattern_engine/source_window/{source_window} [GET]

This will enable us to get a specific source window for the workstream pattern engine.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceWindowApi(api_client)
    source_window = 'source_window_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /workstream_pattern_engine/source_window/{source_window} [GET]
        api_response = api_instance.workstream_pattern_engine_source_window_specific_source_window_snapshot(source_window, transferables=transferables)
        print("The response of WorkstreamPatternEngineSourceWindowApi->workstream_pattern_engine_source_window_specific_source_window_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceWindowApi->workstream_pattern_engine_source_window_specific_source_window_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_window** | **str**| This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**WorkstreamPatternEngineSourceWindow**](WorkstreamPatternEngineSourceWindow.md)

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

# **workstream_pattern_engine_source_window_update**
> WorkstreamPatternEngineSourceWindow workstream_pattern_engine_source_window_update(transferables=transferables, workstream_pattern_engine_source_window=workstream_pattern_engine_source_window)

/workstream_pattern_engine/source_window/update [POST]

This will enable us to update a source window for the workstream pattern engine.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
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
    api_instance = pieces_os_client.WorkstreamPatternEngineSourceWindowApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    workstream_pattern_engine_source_window = pieces_os_client.WorkstreamPatternEngineSourceWindow() # WorkstreamPatternEngineSourceWindow |  (optional)

    try:
        # /workstream_pattern_engine/source_window/update [POST]
        api_response = api_instance.workstream_pattern_engine_source_window_update(transferables=transferables, workstream_pattern_engine_source_window=workstream_pattern_engine_source_window)
        print("The response of WorkstreamPatternEngineSourceWindowApi->workstream_pattern_engine_source_window_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineSourceWindowApi->workstream_pattern_engine_source_window_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **workstream_pattern_engine_source_window** | [**WorkstreamPatternEngineSourceWindow**](WorkstreamPatternEngineSourceWindow.md)|  | [optional] 

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

