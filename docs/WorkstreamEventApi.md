# pieces_os_client.WorkstreamEventApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workstream_event_associate_anchor**](WorkstreamEventApi.md#workstream_event_associate_anchor) | **POST** /workstream_event/{workstream_event}/anchors/associate/{anchor} | /workstream_event/{workstream_event}/anchors/associate/{anchor} [POST]
[**workstream_event_associate_annotation**](WorkstreamEventApi.md#workstream_event_associate_annotation) | **POST** /workstream_event/{workstream_event}/annotations/associate/{annotation} | /workstream_event/{workstream_event}/annotations/associate/{annotation} [POST]
[**workstream_event_associate_conversation_message**](WorkstreamEventApi.md#workstream_event_associate_conversation_message) | **POST** /workstream_event/{workstream_event}/messages/associate/{message} | /workstream_event/{workstream_event}/messages/associate/{message} [POST]
[**workstream_event_associate_person**](WorkstreamEventApi.md#workstream_event_associate_person) | **POST** /workstream_event/{workstream_event}/persons/associate/{person} | /workstream_event/{workstream_event}/persons/associate/{person} [POST]
[**workstream_event_associate_source_window**](WorkstreamEventApi.md#workstream_event_associate_source_window) | **POST** /workstream_event/{workstream_event}/workstream_pattern_engine/source_windows/associate/{source_window} | /workstream_event/{workstream_event}/workstream_pattern_engine/source_windows/associate/{source_window} [POST]
[**workstream_event_associate_tag**](WorkstreamEventApi.md#workstream_event_associate_tag) | **POST** /workstream_event/{workstream_event}/tags/associate/{tag} | /Workstream_event/{workstream_event}/tags/associate/{tag} [POST]
[**workstream_event_associate_website**](WorkstreamEventApi.md#workstream_event_associate_website) | **POST** /workstream_event/{workstream_event}/websites/associate/{website} | /workstream_event/{workstream_event}/websites/associate/{website} [POST]
[**workstream_event_associate_workstream_pattern_engine_source**](WorkstreamEventApi.md#workstream_event_associate_workstream_pattern_engine_source) | **POST** /workstream_event/{workstream_event}/workstream_pattern_engine/sources/associate/{source} | /workstream_event/{workstream_event}/workstream_pattern_engine/sources/associate/{source} [POST]
[**workstream_event_associate_workstream_summary**](WorkstreamEventApi.md#workstream_event_associate_workstream_summary) | **POST** /workstream_event/{workstream_event}/workstream_summaries/associate/{workstream_summary} | /workstream_event/{workstream_event}/workstream_summaries/associate/{workstream_summary} [POST]
[**workstream_event_disassociate_anchor**](WorkstreamEventApi.md#workstream_event_disassociate_anchor) | **POST** /workstream_event/{workstream_event}/anchors/disassociate/{anchor} | /workstream_event/{workstream_event}/anchors/disassociate/{anchor} [POST]
[**workstream_event_disassociate_annotation**](WorkstreamEventApi.md#workstream_event_disassociate_annotation) | **POST** /workstream_event/{workstream_event}/annotations/disassociate/{annotation} | /workstream_event/{workstream_event}/annotations/disassociate/{annotation} [POST]
[**workstream_event_disassociate_conversation_message**](WorkstreamEventApi.md#workstream_event_disassociate_conversation_message) | **POST** /workstream_event/{workstream_event}/messages/disassociate/{message} | /workstream_event/{workstream_event}/messages/disassociate/{message} [POST]
[**workstream_event_disassociate_person**](WorkstreamEventApi.md#workstream_event_disassociate_person) | **POST** /workstream_event/{workstream_event}/persons/disassociate/{person} | /workstream_event/{workstream_event}/persons/disassociate/{person} [POST]
[**workstream_event_disassociate_source_window**](WorkstreamEventApi.md#workstream_event_disassociate_source_window) | **POST** /workstream_event/{workstream_event}/workstream_pattern_engine/source_windows/disassociate/{source_window} | /workstream_event/{workstream_event}/workstream_pattern_engine/source_windows/disassociate/{source_window} [POST]
[**workstream_event_disassociate_tag**](WorkstreamEventApi.md#workstream_event_disassociate_tag) | **POST** /workstream_event/{workstream_event}/tags/disassociate/{tag} | /workstream_event/{workstream_event}/tags/disassociate/{tag} [POST]
[**workstream_event_disassociate_website**](WorkstreamEventApi.md#workstream_event_disassociate_website) | **POST** /workstream_event/{workstream_event}/websites/disassociate/{website} | /workstream_event/{workstream_event}/websites/disassociate/{website} [POST]
[**workstream_event_disassociate_workstream_pattern_engine_source**](WorkstreamEventApi.md#workstream_event_disassociate_workstream_pattern_engine_source) | **POST** /workstream_event/{workstream_event}/workstream_pattern_engine/sources/disassociate/{source} | /workstream_event/{workstream_event}/workstream_pattern_engine/sources/disassociate/{source} [POST]
[**workstream_event_disassociate_workstream_summary**](WorkstreamEventApi.md#workstream_event_disassociate_workstream_summary) | **POST** /workstream_event/{workstream_event}/workstream_summaries/disassociate/{workstream_summary} | /workstream_event/{workstream_event}/workstream_summaries/disassociate/{workstream_summary} [POST]
[**workstream_event_scores_increment**](WorkstreamEventApi.md#workstream_event_scores_increment) | **POST** /workstream_event/{workstream_event}/scores/increment | &#39;/workstream_event/{workstream_event}/scores/increment&#39; [POST]
[**workstream_event_update**](WorkstreamEventApi.md#workstream_event_update) | **POST** /workstream_event/update | /workstream_event/update [POST]
[**workstream_events_specific_workstream_event_snapshot**](WorkstreamEventApi.md#workstream_events_specific_workstream_event_snapshot) | **GET** /workstream_event/{workstream_event} | /workstream_event/{workstream_event} [GET]


# **workstream_event_associate_anchor**
> workstream_event_associate_anchor(workstream_event, anchor)

/workstream_event/{workstream_event}/anchors/associate/{anchor} [POST]

This will enable us to associate an anchor with a workstream event.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /workstream_event/{workstream_event}/anchors/associate/{anchor} [POST]
        api_instance.workstream_event_associate_anchor(workstream_event, anchor)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_associate_anchor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
 **anchor** | **str**| This is the specific uuid of an anchor. | 

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

# **workstream_event_associate_annotation**
> workstream_event_associate_annotation(workstream_event, annotation)

/workstream_event/{workstream_event}/annotations/associate/{annotation} [POST]

This will enable us to associate an annotation with a workstream event.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    annotation = 'annotation_example' # str | This is a specific annotation uuid.

    try:
        # /workstream_event/{workstream_event}/annotations/associate/{annotation} [POST]
        api_instance.workstream_event_associate_annotation(workstream_event, annotation)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_associate_annotation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
 **annotation** | **str**| This is a specific annotation uuid. | 

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

# **workstream_event_associate_conversation_message**
> workstream_event_associate_conversation_message(workstream_event, message)

/workstream_event/{workstream_event}/messages/associate/{message} [POST]

This will associate a workstream_event with a conversation_message. This will do the same thing as the conversation_message equivalent.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    message = 'message_example' # str | This is the uuid of a message.

    try:
        # /workstream_event/{workstream_event}/messages/associate/{message} [POST]
        api_instance.workstream_event_associate_conversation_message(workstream_event, message)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_associate_conversation_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
 **message** | **str**| This is the uuid of a message. | 

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

# **workstream_event_associate_person**
> workstream_event_associate_person(workstream_event, person)

/workstream_event/{workstream_event}/persons/associate/{person} [POST]

This will enable us to associate a person with a workstream event.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /workstream_event/{workstream_event}/persons/associate/{person} [POST]
        api_instance.workstream_event_associate_person(workstream_event, person)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_associate_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
 **person** | **str**| This is a uuid that represents a person. | 

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

# **workstream_event_associate_source_window**
> workstream_event_associate_source_window(workstream_event, source_window)

/workstream_event/{workstream_event}/workstream_pattern_engine/source_windows/associate/{source_window} [POST]

This will enable us to associate a source window with a workstream event.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    source_window = 'source_window_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow

    try:
        # /workstream_event/{workstream_event}/workstream_pattern_engine/source_windows/associate/{source_window} [POST]
        api_instance.workstream_event_associate_source_window(workstream_event, source_window)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_associate_source_window: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
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

# **workstream_event_associate_tag**
> workstream_event_associate_tag(workstream_event, tag)

/Workstream_event/{workstream_event}/tags/associate/{tag} [POST]

This will associate a workstream_event with a tag. This will do the same thing as the tag equivalent.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    tag = 'tag_example' # str | tag id

    try:
        # /Workstream_event/{workstream_event}/tags/associate/{tag} [POST]
        api_instance.workstream_event_associate_tag(workstream_event, tag)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_associate_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
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

# **workstream_event_associate_website**
> workstream_event_associate_website(workstream_event, website)

/workstream_event/{workstream_event}/websites/associate/{website} [POST]

This will enable us to associate a website with a workstream event.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    website = 'website_example' # str | website id

    try:
        # /workstream_event/{workstream_event}/websites/associate/{website} [POST]
        api_instance.workstream_event_associate_website(workstream_event, website)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_associate_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
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

# **workstream_event_associate_workstream_pattern_engine_source**
> workstream_event_associate_workstream_pattern_engine_source(workstream_event, source)

/workstream_event/{workstream_event}/workstream_pattern_engine/sources/associate/{source} [POST]

This will associate a workstream_event with a workstream_pattern_engine_source. This will do the same thing as the workstream_pattern_engine_source equivalent.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    source = 'source_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSource

    try:
        # /workstream_event/{workstream_event}/workstream_pattern_engine/sources/associate/{source} [POST]
        api_instance.workstream_event_associate_workstream_pattern_engine_source(workstream_event, source)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_associate_workstream_pattern_engine_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
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

# **workstream_event_associate_workstream_summary**
> workstream_event_associate_workstream_summary(workstream_event, workstream_summary)

/workstream_event/{workstream_event}/workstream_summaries/associate/{workstream_summary} [POST]

This will associate a workstream_event with a workstream summary. This will do the same thing as the workstreamSummary equivalent.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /workstream_event/{workstream_event}/workstream_summaries/associate/{workstream_summary} [POST]
        api_instance.workstream_event_associate_workstream_summary(workstream_event, workstream_summary)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_associate_workstream_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 

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

# **workstream_event_disassociate_anchor**
> workstream_event_disassociate_anchor(workstream_event, anchor)

/workstream_event/{workstream_event}/anchors/disassociate/{anchor} [POST]

This will enable us to disassociate an anchor from a workstream event.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /workstream_event/{workstream_event}/anchors/disassociate/{anchor} [POST]
        api_instance.workstream_event_disassociate_anchor(workstream_event, anchor)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_disassociate_anchor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
 **anchor** | **str**| This is the specific uuid of an anchor. | 

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

# **workstream_event_disassociate_annotation**
> workstream_event_disassociate_annotation(workstream_event, annotation)

/workstream_event/{workstream_event}/annotations/disassociate/{annotation} [POST]

This will enable us to dissassociate an annotation from a workstream event.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    annotation = 'annotation_example' # str | This is a specific annotation uuid.

    try:
        # /workstream_event/{workstream_event}/annotations/disassociate/{annotation} [POST]
        api_instance.workstream_event_disassociate_annotation(workstream_event, annotation)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_disassociate_annotation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
 **annotation** | **str**| This is a specific annotation uuid. | 

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

# **workstream_event_disassociate_conversation_message**
> workstream_event_disassociate_conversation_message(workstream_event, message)

/workstream_event/{workstream_event}/messages/disassociate/{message} [POST]

This will enable us to disassociate a conversation_message from an workstream_event. This will do the same thing as the conversation_message equivalent.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    message = 'message_example' # str | This is the uuid of a message.

    try:
        # /workstream_event/{workstream_event}/messages/disassociate/{message} [POST]
        api_instance.workstream_event_disassociate_conversation_message(workstream_event, message)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_disassociate_conversation_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
 **message** | **str**| This is the uuid of a message. | 

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

# **workstream_event_disassociate_person**
> workstream_event_disassociate_person(workstream_event, person)

/workstream_event/{workstream_event}/persons/disassociate/{person} [POST]

This will enable us to disassociate a person from a workstream event.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /workstream_event/{workstream_event}/persons/disassociate/{person} [POST]
        api_instance.workstream_event_disassociate_person(workstream_event, person)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_disassociate_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
 **person** | **str**| This is a uuid that represents a person. | 

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

# **workstream_event_disassociate_source_window**
> workstream_event_disassociate_source_window(workstream_event, source_window)

/workstream_event/{workstream_event}/workstream_pattern_engine/source_windows/disassociate/{source_window} [POST]

This will enable us to disassociate a source window from a workstream event.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    source_window = 'source_window_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow

    try:
        # /workstream_event/{workstream_event}/workstream_pattern_engine/source_windows/disassociate/{source_window} [POST]
        api_instance.workstream_event_disassociate_source_window(workstream_event, source_window)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_disassociate_source_window: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
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

# **workstream_event_disassociate_tag**
> workstream_event_disassociate_tag(workstream_event, tag)

/workstream_event/{workstream_event}/tags/disassociate/{tag} [POST]

This will enable us to disassociate a workstream_event from a tag. This will do the same thing as the tag equivalent.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    tag = 'tag_example' # str | tag id

    try:
        # /workstream_event/{workstream_event}/tags/disassociate/{tag} [POST]
        api_instance.workstream_event_disassociate_tag(workstream_event, tag)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_disassociate_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
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

# **workstream_event_disassociate_website**
> workstream_event_disassociate_website(workstream_event, website)

/workstream_event/{workstream_event}/websites/disassociate/{website} [POST]

This will enable us to disassociate a website from a workstream event.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    website = 'website_example' # str | website id

    try:
        # /workstream_event/{workstream_event}/websites/disassociate/{website} [POST]
        api_instance.workstream_event_disassociate_website(workstream_event, website)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_disassociate_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
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

# **workstream_event_disassociate_workstream_pattern_engine_source**
> workstream_event_disassociate_workstream_pattern_engine_source(workstream_event, source)

/workstream_event/{workstream_event}/workstream_pattern_engine/sources/disassociate/{source} [POST]

This will enable us to disassociate a workstream_event from a workstream_pattern_engine_source. This will do the same thing as the workstream_pattern_engine_source equivalent.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    source = 'source_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSource

    try:
        # /workstream_event/{workstream_event}/workstream_pattern_engine/sources/disassociate/{source} [POST]
        api_instance.workstream_event_disassociate_workstream_pattern_engine_source(workstream_event, source)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_disassociate_workstream_pattern_engine_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
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

# **workstream_event_disassociate_workstream_summary**
> workstream_event_disassociate_workstream_summary(workstream_event, workstream_summary)

/workstream_event/{workstream_event}/workstream_summaries/disassociate/{workstream_summary} [POST]

This will enable us to disassociate a workstream_event from a workstream summary. This will do the same thing as the workstreamSummary equivalent.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /workstream_event/{workstream_event}/workstream_summaries/disassociate/{workstream_summary} [POST]
        api_instance.workstream_event_disassociate_workstream_summary(workstream_event, workstream_summary)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_disassociate_workstream_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 

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

# **workstream_event_scores_increment**
> workstream_event_scores_increment(workstream_event, seeded_score_increment=seeded_score_increment)

'/workstream_event/{workstream_event}/scores/increment' [POST]

This will take in a SeededScoreIncrement and will increment the material relative to the incoming body.

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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    seeded_score_increment = pieces_os_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # '/workstream_event/{workstream_event}/scores/increment' [POST]
        api_instance.workstream_event_scores_increment(workstream_event, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_scores_increment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
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

# **workstream_event_update**
> WorkstreamEvent workstream_event_update(transferables=transferables, workstream_event=workstream_event)

/workstream_event/update [POST]

This will update a specific workstream_event.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.workstream_event import WorkstreamEvent
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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    workstream_event = pieces_os_client.WorkstreamEvent() # WorkstreamEvent |  (optional)

    try:
        # /workstream_event/update [POST]
        api_response = api_instance.workstream_event_update(transferables=transferables, workstream_event=workstream_event)
        print("The response of WorkstreamEventApi->workstream_event_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_event_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **workstream_event** | [**WorkstreamEvent**](WorkstreamEvent.md)|  | [optional] 

### Return type

[**WorkstreamEvent**](WorkstreamEvent.md)

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

# **workstream_events_specific_workstream_event_snapshot**
> WorkstreamEvent workstream_events_specific_workstream_event_snapshot(workstream_event, transferables=transferables)

/workstream_event/{workstream_event} [GET]

This will get a snapshot of a single workstream_event.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.workstream_event import WorkstreamEvent
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
    api_instance = pieces_os_client.WorkstreamEventApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /workstream_event/{workstream_event} [GET]
        api_response = api_instance.workstream_events_specific_workstream_event_snapshot(workstream_event, transferables=transferables)
        print("The response of WorkstreamEventApi->workstream_events_specific_workstream_event_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamEventApi->workstream_events_specific_workstream_event_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**WorkstreamEvent**](WorkstreamEvent.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**410** | WorkstreamEvent not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

