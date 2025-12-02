# pieces_os_client.AnnotationApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotation_associate_anchor**](AnnotationApi.md#annotation_associate_anchor) | **POST** /annotation/{annotation}/anchors/associate/{anchor} | /annotation/{annotation}/anchors/associate/{anchor} [POST]
[**annotation_associate_asset**](AnnotationApi.md#annotation_associate_asset) | **POST** /annotation/{annotation}/assets/associate/{asset} | /annotation/{annotation}/assets/associate/{asset} [POST]
[**annotation_associate_conversation**](AnnotationApi.md#annotation_associate_conversation) | **POST** /annotation/{annotation}/conversations/associate/{conversation} | /annotation/{annotation}/conversations/associate/{conversation} [POST]
[**annotation_associate_conversation_message**](AnnotationApi.md#annotation_associate_conversation_message) | **POST** /annotation/{annotation}/messages/associate/{message} | /annotation/{annotation}/messages/associate/{message} [POST]
[**annotation_associate_person**](AnnotationApi.md#annotation_associate_person) | **POST** /annotation/{annotation}/persons/associate/{person} | /annotation/{annotation}/persons/associate/{person} [POST]
[**annotation_associate_tag**](AnnotationApi.md#annotation_associate_tag) | **POST** /annotation/{annotation}/tags/associate/{tag} | /annotation/{annotation}/tags/associate/{tag} [POST]
[**annotation_associate_website**](AnnotationApi.md#annotation_associate_website) | **POST** /annotation/{annotation}/websites/associate/{website} | /annotation/{annotation}/websites/associate/{website} [POST]
[**annotation_associate_workstream_event**](AnnotationApi.md#annotation_associate_workstream_event) | **POST** /annotation/{annotation}/workstream_events/associate/{workstream_event} | /annotation/{annotation}/workstream_events/associate/{workstream_event} [POST]
[**annotation_associate_workstream_summary**](AnnotationApi.md#annotation_associate_workstream_summary) | **POST** /annotation/{annotation}/workstream_summaries/associate/{workstream_summary} | /annotation/{annotation}/workstream_summaries/associate/{workstream_summary} [POST]
[**annotation_disassociate_anchor**](AnnotationApi.md#annotation_disassociate_anchor) | **POST** /annotation/{annotation}/anchors/disassociate/{anchor} | /annotation/{annotation}/anchors/disassociate/{anchor} [POST]
[**annotation_disassociate_asset**](AnnotationApi.md#annotation_disassociate_asset) | **POST** /annotation/{annotation}/assets/disassociate/{asset} | /annotation/{annotation}/assets/disassociate/{asset} [POST]
[**annotation_disassociate_conversation**](AnnotationApi.md#annotation_disassociate_conversation) | **POST** /annotation/{annotation}/conversations/disassociate/{conversation} | /annotation/{annotation}/conversations/disassociate/{conversation} [POST]
[**annotation_disassociate_conversation_message**](AnnotationApi.md#annotation_disassociate_conversation_message) | **POST** /annotation/{annotation}/messages/disassociate/{message} | /annotation/{annotation}/messages/disassociate/{message} [POST]
[**annotation_disassociate_person**](AnnotationApi.md#annotation_disassociate_person) | **POST** /annotation/{annotation}/persons/disassociate/{person} | /annotation/{annotation}/persons/disassociate/{person} [POST]
[**annotation_disassociate_tag**](AnnotationApi.md#annotation_disassociate_tag) | **POST** /annotation/{annotation}/tags/disassociate/{tag} | /annotation/{annotation}/tags/disassociate/{tag} [POST]
[**annotation_disassociate_website**](AnnotationApi.md#annotation_disassociate_website) | **POST** /annotation/{annotation}/websites/disassociate/{website} | /annotation/{annotation}/websites/disassociate/{website} [POST]
[**annotation_disassociate_workstream_event**](AnnotationApi.md#annotation_disassociate_workstream_event) | **POST** /annotation/{annotation}/workstream_events/disassociate/{workstream_event} | /annotation/{annotation}/workstream_events/disassociate/{workstream_event} [POST]
[**annotation_disassociate_workstream_summary**](AnnotationApi.md#annotation_disassociate_workstream_summary) | **POST** /annotation/{annotation}/workstream_summaries/disassociate/{workstream_summary} | /annotation/{annotation}/workstream_summaries/disassociate/{workstream_summary} [POST]
[**annotation_scores_increment**](AnnotationApi.md#annotation_scores_increment) | **POST** /annotation/{annotation}/scores/increment | &#39;/annotation/{annotation}/scores/increment&#39; [POST]
[**annotation_specific_annotation_snapshot**](AnnotationApi.md#annotation_specific_annotation_snapshot) | **GET** /annotation/{annotation} | /annotation/{annotation} [GET]
[**annotation_update**](AnnotationApi.md#annotation_update) | **POST** /annotation/update | /annotation/update [POST]


# **annotation_associate_anchor**
> annotation_associate_anchor(annotation, anchor)

/annotation/{annotation}/anchors/associate/{anchor} [POST]

This will associate an anchor with an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /annotation/{annotation}/anchors/associate/{anchor} [POST]
        api_instance.annotation_associate_anchor(annotation, anchor)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_associate_anchor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_associate_asset**
> annotation_associate_asset(annotation, asset)

/annotation/{annotation}/assets/associate/{asset} [POST]

This will associate an asset with an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /annotation/{annotation}/assets/associate/{asset} [POST]
        api_instance.annotation_associate_asset(annotation, asset)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_associate_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 

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

# **annotation_associate_conversation**
> annotation_associate_conversation(annotation, conversation)

/annotation/{annotation}/conversations/associate/{conversation} [POST]

This will associate a conversation with an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    conversation = 'conversation_example' # str | This is the uuid of a conversation.

    try:
        # /annotation/{annotation}/conversations/associate/{conversation} [POST]
        api_instance.annotation_associate_conversation(annotation, conversation)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_associate_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
 **conversation** | **str**| This is the uuid of a conversation. | 

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

# **annotation_associate_conversation_message**
> annotation_associate_conversation_message(annotation, message)

/annotation/{annotation}/messages/associate/{message} [POST]

This will associate a message with an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    message = 'message_example' # str | This is the uuid of a message.

    try:
        # /annotation/{annotation}/messages/associate/{message} [POST]
        api_instance.annotation_associate_conversation_message(annotation, message)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_associate_conversation_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_associate_person**
> annotation_associate_person(annotation, person)

/annotation/{annotation}/persons/associate/{person} [POST]

This will associate a person with an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /annotation/{annotation}/persons/associate/{person} [POST]
        api_instance.annotation_associate_person(annotation, person)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_associate_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_associate_tag**
> annotation_associate_tag(annotation, tag)

/annotation/{annotation}/tags/associate/{tag} [POST]

This will enable us to associate a tag with an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    tag = 'tag_example' # str | tag id

    try:
        # /annotation/{annotation}/tags/associate/{tag} [POST]
        api_instance.annotation_associate_tag(annotation, tag)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_associate_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_associate_website**
> annotation_associate_website(annotation, website)

/annotation/{annotation}/websites/associate/{website} [POST]

This will enable us to associate a website with an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    website = 'website_example' # str | website id

    try:
        # /annotation/{annotation}/websites/associate/{website} [POST]
        api_instance.annotation_associate_website(annotation, website)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_associate_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_associate_workstream_event**
> annotation_associate_workstream_event(annotation, workstream_event)

/annotation/{annotation}/workstream_events/associate/{workstream_event} [POST]

This will enable us to associate a workstream event with an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.

    try:
        # /annotation/{annotation}/workstream_events/associate/{workstream_event} [POST]
        api_instance.annotation_associate_workstream_event(annotation, workstream_event)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_associate_workstream_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_associate_workstream_summary**
> annotation_associate_workstream_summary(annotation, workstream_summary)

/annotation/{annotation}/workstream_summaries/associate/{workstream_summary} [POST]

This will enable us to associate a workstream summary with an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /annotation/{annotation}/workstream_summaries/associate/{workstream_summary} [POST]
        api_instance.annotation_associate_workstream_summary(annotation, workstream_summary)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_associate_workstream_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_disassociate_anchor**
> annotation_disassociate_anchor(annotation, anchor)

/annotation/{annotation}/anchors/disassociate/{anchor} [POST]

This will enable us to dissassociate an anchor from an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /annotation/{annotation}/anchors/disassociate/{anchor} [POST]
        api_instance.annotation_disassociate_anchor(annotation, anchor)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_disassociate_anchor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_disassociate_asset**
> annotation_disassociate_asset(annotation, asset)

/annotation/{annotation}/assets/disassociate/{asset} [POST]

This will enable us to dissassociate an asset from an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /annotation/{annotation}/assets/disassociate/{asset} [POST]
        api_instance.annotation_disassociate_asset(annotation, asset)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_disassociate_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 

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

# **annotation_disassociate_conversation**
> annotation_disassociate_conversation(annotation, conversation)

/annotation/{annotation}/conversations/disassociate/{conversation} [POST]

This will enable us to dissassociate a conversation from an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    conversation = 'conversation_example' # str | This is the uuid of a conversation.

    try:
        # /annotation/{annotation}/conversations/disassociate/{conversation} [POST]
        api_instance.annotation_disassociate_conversation(annotation, conversation)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_disassociate_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
 **conversation** | **str**| This is the uuid of a conversation. | 

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

# **annotation_disassociate_conversation_message**
> annotation_disassociate_conversation_message(annotation, message)

/annotation/{annotation}/messages/disassociate/{message} [POST]

This will enable us to dissassociate a message from an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    message = 'message_example' # str | This is the uuid of a message.

    try:
        # /annotation/{annotation}/messages/disassociate/{message} [POST]
        api_instance.annotation_disassociate_conversation_message(annotation, message)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_disassociate_conversation_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_disassociate_person**
> annotation_disassociate_person(annotation, person)

/annotation/{annotation}/persons/disassociate/{person} [POST]

This will enable us to dissassociate a person from an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /annotation/{annotation}/persons/disassociate/{person} [POST]
        api_instance.annotation_disassociate_person(annotation, person)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_disassociate_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_disassociate_tag**
> annotation_disassociate_tag(annotation, tag)

/annotation/{annotation}/tags/disassociate/{tag} [POST]

This will enable us to dissassociate a tag from an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    tag = 'tag_example' # str | tag id

    try:
        # /annotation/{annotation}/tags/disassociate/{tag} [POST]
        api_instance.annotation_disassociate_tag(annotation, tag)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_disassociate_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_disassociate_website**
> annotation_disassociate_website(annotation, website)

/annotation/{annotation}/websites/disassociate/{website} [POST]

This will enable us to dissassociate a website from an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    website = 'website_example' # str | website id

    try:
        # /annotation/{annotation}/websites/disassociate/{website} [POST]
        api_instance.annotation_disassociate_website(annotation, website)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_disassociate_website: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_disassociate_workstream_event**
> annotation_disassociate_workstream_event(annotation, workstream_event)

/annotation/{annotation}/workstream_events/disassociate/{workstream_event} [POST]

This will enable us to dissassociate a workstream event from an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.

    try:
        # /annotation/{annotation}/workstream_events/disassociate/{workstream_event} [POST]
        api_instance.annotation_disassociate_workstream_event(annotation, workstream_event)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_disassociate_workstream_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_disassociate_workstream_summary**
> annotation_disassociate_workstream_summary(annotation, workstream_summary)

/annotation/{annotation}/workstream_summaries/disassociate/{workstream_summary} [POST]

This will enable us to dissassociate a workstream summary from an annotation.

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /annotation/{annotation}/workstream_summaries/disassociate/{workstream_summary} [POST]
        api_instance.annotation_disassociate_workstream_summary(annotation, workstream_summary)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_disassociate_workstream_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_scores_increment**
> annotation_scores_increment(annotation, seeded_score_increment=seeded_score_increment)

'/annotation/{annotation}/scores/increment' [POST]

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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    seeded_score_increment = pieces_os_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # '/annotation/{annotation}/scores/increment' [POST]
        api_instance.annotation_scores_increment(annotation, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_scores_increment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 
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

# **annotation_specific_annotation_snapshot**
> Annotation annotation_specific_annotation_snapshot(annotation)

/annotation/{annotation} [GET]

This will get a snapshot of a specific annotation.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.annotation import Annotation
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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.

    try:
        # /annotation/{annotation} [GET]
        api_response = api_instance.annotation_specific_annotation_snapshot(annotation)
        print("The response of AnnotationApi->annotation_specific_annotation_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_specific_annotation_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 

### Return type

[**Annotation**](Annotation.md)

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

# **annotation_update**
> Annotation annotation_update(annotation=annotation)

/annotation/update [POST]

This will update a specific annotation.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.annotation import Annotation
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
    api_instance = pieces_os_client.AnnotationApi(api_client)
    annotation = pieces_os_client.Annotation() # Annotation |  (optional)

    try:
        # /annotation/update [POST]
        api_response = api_instance.annotation_update(annotation=annotation)
        print("The response of AnnotationApi->annotation_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationApi->annotation_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | [**Annotation**](Annotation.md)|  | [optional] 

### Return type

[**Annotation**](Annotation.md)

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

