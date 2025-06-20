# pieces_os_client.WebsiteApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**website_associate_annotation**](WebsiteApi.md#website_associate_annotation) | **POST** /website/{website}/annotations/associate/{annotation} | /website/{website}/annotations/associate/{annotation} [POST]
[**website_associate_asset**](WebsiteApi.md#website_associate_asset) | **POST** /website/{website}/assets/associate/{asset} | /website/{website}/assets/associate/{asset} [POST]
[**website_associate_conversation**](WebsiteApi.md#website_associate_conversation) | **POST** /website/{website}/conversations/associate/{conversation} | /website/{website}/conversations/associate/{conversation} [POST]
[**website_associate_message**](WebsiteApi.md#website_associate_message) | **POST** /website/{website}/messages/associate/{message} | /website/{website}/messages/associate/{message} [POST]
[**website_associate_person**](WebsiteApi.md#website_associate_person) | **POST** /website/{website}/persons/associate/{person} | /website/{website}/persons/associate/{person} [POST]
[**website_associate_tag**](WebsiteApi.md#website_associate_tag) | **POST** /website/{website}/tags/associate/{tag} | /website/{website}/tags/associate/{tag} [POST]
[**website_associate_workstream_event**](WebsiteApi.md#website_associate_workstream_event) | **POST** /website/{website}/workstream_events/associate/{workstream_event} | /website/{website}/workstream_events/associate/{workstream_event} [POST]
[**website_associate_workstream_pattern_engine_source**](WebsiteApi.md#website_associate_workstream_pattern_engine_source) | **POST** /website/{website}/workstream_pattern_engine/sources/associate/{source} | /website/{website}/workstream_pattern_engine/sources/associate/{source} [POST]
[**website_associate_workstream_pattern_engine_source_window**](WebsiteApi.md#website_associate_workstream_pattern_engine_source_window) | **POST** /website/{website}/workstream_pattern_engine/source_windows/associate/{source_window} | /website/{website}/workstream_pattern_engine/source_windows/associate/{source_window} [POST]
[**website_associate_workstream_summary**](WebsiteApi.md#website_associate_workstream_summary) | **POST** /website/{website}/workstream_summaries/associate/{workstream_summary} | /website/{website}/workstream_summaries/associate/{workstream_summary} [POST]
[**website_disassociate_annotation**](WebsiteApi.md#website_disassociate_annotation) | **POST** /website/{website}/annotations/disassociate/{annotation} | /website/{website}/annotations/disassociate/{annotation} [POST]
[**website_disassociate_asset**](WebsiteApi.md#website_disassociate_asset) | **POST** /website/{website}/assets/disassociate/{asset} | /website/{website}/assets/disassociate/{asset} [POST]
[**website_disassociate_conversation**](WebsiteApi.md#website_disassociate_conversation) | **POST** /website/{website}/conversations/disassociate/{conversation} | /website/{website}/conversations/disassociate/{conversation} [POST]
[**website_disassociate_message**](WebsiteApi.md#website_disassociate_message) | **POST** /website/{website}/messages/disassociate/{message} | /website/{website}/messages/disassociate/{message} [POST]
[**website_disassociate_person**](WebsiteApi.md#website_disassociate_person) | **POST** /website/{website}/persons/disassociate/{person} | /website/{website}/persons/disassociate/{person} [POST]
[**website_disassociate_tag**](WebsiteApi.md#website_disassociate_tag) | **POST** /website/{website}/tags/disassociate/{tag} | /website/{website}/tags/disassociate/{tag} [POST]
[**website_disassociate_workstream_event**](WebsiteApi.md#website_disassociate_workstream_event) | **POST** /website/{website}/workstream_events/disassociate/{workstream_event} | /website/{website}/workstream_events/disassociate/{workstream_event} [POST]
[**website_disassociate_workstream_pattern_engine_source**](WebsiteApi.md#website_disassociate_workstream_pattern_engine_source) | **POST** /website/{website}/workstream_pattern_engine/sources/disassociate/{source} | /website/{website}/workstream_pattern_engine/sources/disassociate/{source} [POST]
[**website_disassociate_workstream_pattern_engine_source_window**](WebsiteApi.md#website_disassociate_workstream_pattern_engine_source_window) | **POST** /website/{website}/workstream_pattern_engine/source_windows/disassociate/{source_window} | /website/{website}/workstream_pattern_engine/source_windows/disassociate/{source_window} [POST]
[**website_disassociate_workstream_summary**](WebsiteApi.md#website_disassociate_workstream_summary) | **POST** /website/{website}/workstream_summaries/disassociate/{workstream_summary} | /website/{website}/workstream_summaries/disassociate/{workstream_summary} [POST]
[**website_scores_increment**](WebsiteApi.md#website_scores_increment) | **POST** /website/{website}/scores/increment | &#39;/website/{website}/scores/increment&#39; [POST]
[**website_update**](WebsiteApi.md#website_update) | **POST** /website/update | /website/update [POST]
[**websites_specific_website_snapshot**](WebsiteApi.md#websites_specific_website_snapshot) | **GET** /website/{website} | /website/{website} [GET]


# **website_associate_annotation**
> website_associate_annotation(website, annotation)

/website/{website}/annotations/associate/{annotation} [POST]

This will enable us to associate an annotation with a website.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    annotation = 'annotation_example' # str | This is a specific annotation uuid.

    try:
        # /website/{website}/annotations/associate/{annotation} [POST]
        api_instance.website_associate_annotation(website, annotation)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_associate_annotation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_associate_asset**
> website_associate_asset(asset, website)

/website/{website}/assets/associate/{asset} [POST]

This will associate a website with a asset.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    website = 'website_example' # str | website id

    try:
        # /website/{website}/assets/associate/{asset} [POST]
        api_instance.website_associate_asset(asset, website)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_associate_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
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

# **website_associate_conversation**
> website_associate_conversation(website, conversation)

/website/{website}/conversations/associate/{conversation} [POST]

This will associate a website with a conversation.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    conversation = 'conversation_example' # str | This is the uuid of a conversation.

    try:
        # /website/{website}/conversations/associate/{conversation} [POST]
        api_instance.website_associate_conversation(website, conversation)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_associate_conversation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_associate_message**
> website_associate_message(website, message)

/website/{website}/messages/associate/{message} [POST]

This will associate a website with a message.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    message = 'message_example' # str | This is the uuid of a message.

    try:
        # /website/{website}/messages/associate/{message} [POST]
        api_instance.website_associate_message(website, message)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_associate_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_associate_person**
> website_associate_person(website, person)

/website/{website}/persons/associate/{person} [POST]

This will associate a website with a person.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /website/{website}/persons/associate/{person} [POST]
        api_instance.website_associate_person(website, person)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_associate_person: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_associate_tag**
> website_associate_tag(website, tag)

/website/{website}/tags/associate/{tag} [POST]

This will enable us to associate a tag with a website.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    tag = 'tag_example' # str | tag id

    try:
        # /website/{website}/tags/associate/{tag} [POST]
        api_instance.website_associate_tag(website, tag)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_associate_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_associate_workstream_event**
> website_associate_workstream_event(website, workstream_event)

/website/{website}/workstream_events/associate/{workstream_event} [POST]

This will enable us to associate a workstream event with a website.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.

    try:
        # /website/{website}/workstream_events/associate/{workstream_event} [POST]
        api_instance.website_associate_workstream_event(website, workstream_event)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_associate_workstream_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_associate_workstream_pattern_engine_source**
> website_associate_workstream_pattern_engine_source(website, source)

/website/{website}/workstream_pattern_engine/sources/associate/{source} [POST]

This will enable us to associate a source with a website.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    source = 'source_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSource

    try:
        # /website/{website}/workstream_pattern_engine/sources/associate/{source} [POST]
        api_instance.website_associate_workstream_pattern_engine_source(website, source)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_associate_workstream_pattern_engine_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_associate_workstream_pattern_engine_source_window**
> website_associate_workstream_pattern_engine_source_window(website, source_window)

/website/{website}/workstream_pattern_engine/source_windows/associate/{source_window} [POST]

This will enable us to associate a source window with a website.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    source_window = 'source_window_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow

    try:
        # /website/{website}/workstream_pattern_engine/source_windows/associate/{source_window} [POST]
        api_instance.website_associate_workstream_pattern_engine_source_window(website, source_window)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_associate_workstream_pattern_engine_source_window: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_associate_workstream_summary**
> website_associate_workstream_summary(website, workstream_summary)

/website/{website}/workstream_summaries/associate/{workstream_summary} [POST]

This will associate a website with a workstream summary. This will do the same thing as the workstreamSummary equivalent.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /website/{website}/workstream_summaries/associate/{workstream_summary} [POST]
        api_instance.website_associate_workstream_summary(website, workstream_summary)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_associate_workstream_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_disassociate_annotation**
> website_disassociate_annotation(website, annotation)

/website/{website}/annotations/disassociate/{annotation} [POST]

This will enable us to dissassociate an annotation from a website.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    annotation = 'annotation_example' # str | This is a specific annotation uuid.

    try:
        # /website/{website}/annotations/disassociate/{annotation} [POST]
        api_instance.website_disassociate_annotation(website, annotation)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_disassociate_annotation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_disassociate_asset**
> website_disassociate_asset(website, asset)

/website/{website}/assets/disassociate/{asset} [POST]

This will enable us to dissassociate a website from a asset.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /website/{website}/assets/disassociate/{asset} [POST]
        api_instance.website_disassociate_asset(website, asset)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_disassociate_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_disassociate_conversation**
> website_disassociate_conversation(website, conversation)

/website/{website}/conversations/disassociate/{conversation} [POST]

This will enable us to dissassociate a website from a conversation.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    conversation = 'conversation_example' # str | This is the uuid of a conversation.

    try:
        # /website/{website}/conversations/disassociate/{conversation} [POST]
        api_instance.website_disassociate_conversation(website, conversation)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_disassociate_conversation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_disassociate_message**
> website_disassociate_message(website, message)

/website/{website}/messages/disassociate/{message} [POST]

This will enable us to disassociate a website from a message.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    message = 'message_example' # str | This is the uuid of a message.

    try:
        # /website/{website}/messages/disassociate/{message} [POST]
        api_instance.website_disassociate_message(website, message)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_disassociate_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_disassociate_person**
> website_disassociate_person(website, person)

/website/{website}/persons/disassociate/{person} [POST]

This will enable us to dissassociate a website from a person.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /website/{website}/persons/disassociate/{person} [POST]
        api_instance.website_disassociate_person(website, person)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_disassociate_person: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_disassociate_tag**
> website_disassociate_tag(website, tag)

/website/{website}/tags/disassociate/{tag} [POST]

This will enable us to disassociate a tag from a website.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    tag = 'tag_example' # str | tag id

    try:
        # /website/{website}/tags/disassociate/{tag} [POST]
        api_instance.website_disassociate_tag(website, tag)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_disassociate_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_disassociate_workstream_event**
> website_disassociate_workstream_event(website, workstream_event)

/website/{website}/workstream_events/disassociate/{workstream_event} [POST]

This will enable us to disassociate a workstream event from a website.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.

    try:
        # /website/{website}/workstream_events/disassociate/{workstream_event} [POST]
        api_instance.website_disassociate_workstream_event(website, workstream_event)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_disassociate_workstream_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_disassociate_workstream_pattern_engine_source**
> website_disassociate_workstream_pattern_engine_source(website, source)

/website/{website}/workstream_pattern_engine/sources/disassociate/{source} [POST]

This will enable us to disassociate a source from a website.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    source = 'source_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSource

    try:
        # /website/{website}/workstream_pattern_engine/sources/disassociate/{source} [POST]
        api_instance.website_disassociate_workstream_pattern_engine_source(website, source)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_disassociate_workstream_pattern_engine_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_disassociate_workstream_pattern_engine_source_window**
> website_disassociate_workstream_pattern_engine_source_window(website, source_window)

/website/{website}/workstream_pattern_engine/source_windows/disassociate/{source_window} [POST]

This will enable us to disassociate a source window from a website.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    source_window = 'source_window_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSourceWindow

    try:
        # /website/{website}/workstream_pattern_engine/source_windows/disassociate/{source_window} [POST]
        api_instance.website_disassociate_workstream_pattern_engine_source_window(website, source_window)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_disassociate_workstream_pattern_engine_source_window: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_disassociate_workstream_summary**
> website_disassociate_workstream_summary(website, workstream_summary)

/website/{website}/workstream_summaries/disassociate/{workstream_summary} [POST]

This will enable us to disassociate a website from a workstream summary. This will do the same thing as the workstreamSummary equivalent.

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /website/{website}/workstream_summaries/disassociate/{workstream_summary} [POST]
        api_instance.website_disassociate_workstream_summary(website, workstream_summary)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_disassociate_workstream_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_scores_increment**
> website_scores_increment(website, seeded_score_increment=seeded_score_increment)

'/website/{website}/scores/increment' [POST]

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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    seeded_score_increment = pieces_os_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # '/website/{website}/scores/increment' [POST]
        api_instance.website_scores_increment(website, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_scores_increment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **website_update**
> Website website_update(transferables=transferables, website=website)

/website/update [POST]

This will update a specific website.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.website import Website
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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    website = pieces_os_client.Website() # Website |  (optional)

    try:
        # /website/update [POST]
        api_response = api_instance.website_update(transferables=transferables, website=website)
        print("The response of WebsiteApi->website_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteApi->website_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **website** | [**Website**](Website.md)|  | [optional] 

### Return type

[**Website**](Website.md)

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

# **websites_specific_website_snapshot**
> Website websites_specific_website_snapshot(website, transferables=transferables)

/website/{website} [GET]

This will get a snapshot of a single website.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.website import Website
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
    api_instance = pieces_os_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /website/{website} [GET]
        api_response = api_instance.websites_specific_website_snapshot(website, transferables=transferables)
        print("The response of WebsiteApi->websites_specific_website_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebsiteApi->websites_specific_website_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Website**](Website.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**410** | Website not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

