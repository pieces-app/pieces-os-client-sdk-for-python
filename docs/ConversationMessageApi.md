# pieces_os_client.ConversationMessageApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversation_message_associate_asset**](ConversationMessageApi.md#conversation_message_associate_asset) | **POST** /message/{message}/assets/associate/{asset} | /message/{message}/assets/associate/{asset} [POST]
[**conversation_message_associate_conversation_message**](ConversationMessageApi.md#conversation_message_associate_conversation_message) | **POST** /message/{message}/messages/associate/{additional_message} | /message/{message}/messages/associate/{additional_message} [POST]
[**conversation_message_associate_range**](ConversationMessageApi.md#conversation_message_associate_range) | **POST** /message/{message}/ranges/associate/{range} | /message/{message}/ranges/associate/{range} [POST]
[**conversation_message_associate_tag**](ConversationMessageApi.md#conversation_message_associate_tag) | **POST** /message/{message}/tags/associate/{tag} | /message/{message}/tags/associate/{tag} [POST]
[**conversation_message_associate_workstream_event**](ConversationMessageApi.md#conversation_message_associate_workstream_event) | **POST** /message/{message}/workstream_events/associate/{workstream_event} | /message/{message}/workstream_events/associate/{workstream_event} [POST]
[**conversation_message_associate_workstream_pattern_engine_source**](ConversationMessageApi.md#conversation_message_associate_workstream_pattern_engine_source) | **POST** /message/{message}/workstream_pattern_engine/sources/associate/{source} | /message/{message}/workstream_pattern_engine/sources/associate/{source} [POST]
[**conversation_message_associate_workstream_summary**](ConversationMessageApi.md#conversation_message_associate_workstream_summary) | **POST** /message/{message}/workstream_summaries/associate/{workstream_summary} | /message/{message}/workstream_summaries/associate/{workstream_summary} [POST]
[**conversation_message_disassociate_asset**](ConversationMessageApi.md#conversation_message_disassociate_asset) | **POST** /message/{message}/assets/disassociate/{asset} | /message/{message}/assets/disassociate/{asset} [POST]
[**conversation_message_disassociate_conversation_message**](ConversationMessageApi.md#conversation_message_disassociate_conversation_message) | **POST** /message/{message}/messages/disassociate/{additional_message} | /message/{message}/messages/disassociate/{additional_message} [POST]
[**conversation_message_disassociate_range**](ConversationMessageApi.md#conversation_message_disassociate_range) | **POST** /message/{message}/ranges/disassociate/{range} | /message/{message}/ranges/disassociate/{range} [POST]
[**conversation_message_disassociate_tag**](ConversationMessageApi.md#conversation_message_disassociate_tag) | **POST** /message/{message}/tags/disassociate/{tag} | /message/{message}/tags/disassociate/{tag} [POST]
[**conversation_message_disassociate_workstream_event**](ConversationMessageApi.md#conversation_message_disassociate_workstream_event) | **POST** /message/{message}/workstream_events/disassociate/{workstream_event} | /message/{message}/workstream_events/disassociate/{workstream_event} [POST]
[**conversation_message_disassociate_workstream_pattern_engine_source**](ConversationMessageApi.md#conversation_message_disassociate_workstream_pattern_engine_source) | **POST** /message/{message}/workstream_pattern_engine/sources/disassociate/{source} | /message/{message}/workstream_pattern_engine/sources/disassociate/{source} [POST]
[**conversation_message_disassociate_workstream_summary**](ConversationMessageApi.md#conversation_message_disassociate_workstream_summary) | **POST** /message/{message}/workstream_summaries/disassociate/{workstream_summary} | /message/{message}/workstream_summaries/disassociate/{workstream_summary} [POST]
[**message_associate_anchor**](ConversationMessageApi.md#message_associate_anchor) | **POST** /message/{message}/anchors/associate/{anchor} | /message/{message}/anchors/associate/{anchor} [POST]
[**message_associate_annotation**](ConversationMessageApi.md#message_associate_annotation) | **POST** /message/{message}/annotations/associate/{annotation} | /message/{message}/annotations/associate/{annotation} [POST]
[**message_associate_person**](ConversationMessageApi.md#message_associate_person) | **POST** /message/{message}/persons/associate/{person} | /message/{message}/persons/associate/{person} [POST]
[**message_associate_website**](ConversationMessageApi.md#message_associate_website) | **POST** /message/{message}/websites/associate/{website} | Associate a message with a website
[**message_disassociate_anchor**](ConversationMessageApi.md#message_disassociate_anchor) | **POST** /message/{message}/anchors/disassociate/{anchor} | /message/{message}/anchors/disassociate/{anchor} [POST]
[**message_disassociate_annotation**](ConversationMessageApi.md#message_disassociate_annotation) | **POST** /message/{message}/annotations/disassociate/{annotation} | /message/{message}/annotations/disassociate/{annotation} [POST]
[**message_disassociate_person**](ConversationMessageApi.md#message_disassociate_person) | **POST** /message/{message}/persons/disassociate/{person} | /message/{message}/persons/disassociate/{person} [POST]
[**message_disassociate_website**](ConversationMessageApi.md#message_disassociate_website) | **POST** /message/{message}/websites/disassociate/{website} | /message/{message}/websites/disassociate/{website} [POST]
[**message_scores_increment**](ConversationMessageApi.md#message_scores_increment) | **POST** /message/{message}/scores/increment | &#39;/message/{message}/scores/increment&#39; [POST]
[**message_specific_message_snapshot**](ConversationMessageApi.md#message_specific_message_snapshot) | **GET** /message/{message} | /message/{message} [GET]
[**message_specific_message_update**](ConversationMessageApi.md#message_specific_message_update) | **POST** /message/update | /message/update [GET]
[**message_update_value**](ConversationMessageApi.md#message_update_value) | **POST** /message/update/value | /message/update/value [POST]


# **conversation_message_associate_asset**
> conversation_message_associate_asset(message, asset)

/message/{message}/assets/associate/{asset} [POST]

This will associate a conversation-message with a asset. This will do the same thing as the asset equivalent.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /message/{message}/assets/associate/{asset} [POST]
        api_instance.conversation_message_associate_asset(message, asset)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->conversation_message_associate_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **conversation_message_associate_conversation_message**
> conversation_message_associate_conversation_message(message, additional_message)

/message/{message}/messages/associate/{additional_message} [POST]

This will associate a conversation_message with a conversation_message.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    additional_message = 'additional_message_example' # str | In the case of 2 route params we can use the additional prefix.

    try:
        # /message/{message}/messages/associate/{additional_message} [POST]
        api_instance.conversation_message_associate_conversation_message(message, additional_message)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->conversation_message_associate_conversation_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
 **additional_message** | **str**| In the case of 2 route params we can use the additional prefix. | 

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

# **conversation_message_associate_range**
> conversation_message_associate_range(message, range)

/message/{message}/ranges/associate/{range} [POST]

This will associate a conversation-message with a range. This will do the same thing as the range equivalent.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    range = 'range_example' # str | This is a identifier that is used to identify a specific range.

    try:
        # /message/{message}/ranges/associate/{range} [POST]
        api_instance.conversation_message_associate_range(message, range)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->conversation_message_associate_range: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
 **range** | **str**| This is a identifier that is used to identify a specific range. | 

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

# **conversation_message_associate_tag**
> conversation_message_associate_tag(message, tag)

/message/{message}/tags/associate/{tag} [POST]

This will associate a conversation-message with a tag. This will do the same thing as the tag equivalent.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    tag = 'tag_example' # str | tag id

    try:
        # /message/{message}/tags/associate/{tag} [POST]
        api_instance.conversation_message_associate_tag(message, tag)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->conversation_message_associate_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **conversation_message_associate_workstream_event**
> conversation_message_associate_workstream_event(message, workstream_event)

/message/{message}/workstream_events/associate/{workstream_event} [POST]

This will associate a conversation-message with a workstream_event. This will do the same thing as the workstream_event equivalent.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.

    try:
        # /message/{message}/workstream_events/associate/{workstream_event} [POST]
        api_instance.conversation_message_associate_workstream_event(message, workstream_event)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->conversation_message_associate_workstream_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **conversation_message_associate_workstream_pattern_engine_source**
> conversation_message_associate_workstream_pattern_engine_source(message, source)

/message/{message}/workstream_pattern_engine/sources/associate/{source} [POST]

This will associate a conversation-message with a source. This will do the same thing as the source equivalent.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    source = 'source_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSource

    try:
        # /message/{message}/workstream_pattern_engine/sources/associate/{source} [POST]
        api_instance.conversation_message_associate_workstream_pattern_engine_source(message, source)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->conversation_message_associate_workstream_pattern_engine_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **conversation_message_associate_workstream_summary**
> conversation_message_associate_workstream_summary(message, workstream_summary)

/message/{message}/workstream_summaries/associate/{workstream_summary} [POST]

This will associate a conversation-message with a workstream_summary. This will do the same thing as the workstream_summary equivalent.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /message/{message}/workstream_summaries/associate/{workstream_summary} [POST]
        api_instance.conversation_message_associate_workstream_summary(message, workstream_summary)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->conversation_message_associate_workstream_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **conversation_message_disassociate_asset**
> conversation_message_disassociate_asset(message, asset)

/message/{message}/assets/disassociate/{asset} [POST]

This will enable us to disassociate a conversation_message from a asset. This will do the same thing as the asset equivalent.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /message/{message}/assets/disassociate/{asset} [POST]
        api_instance.conversation_message_disassociate_asset(message, asset)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->conversation_message_disassociate_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **conversation_message_disassociate_conversation_message**
> conversation_message_disassociate_conversation_message(message, additional_message)

/message/{message}/messages/disassociate/{additional_message} [POST]

This will enable us to disassociate a conversation_message from a conversation_message.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    additional_message = 'additional_message_example' # str | In the case of 2 route params we can use the additional prefix.

    try:
        # /message/{message}/messages/disassociate/{additional_message} [POST]
        api_instance.conversation_message_disassociate_conversation_message(message, additional_message)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->conversation_message_disassociate_conversation_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
 **additional_message** | **str**| In the case of 2 route params we can use the additional prefix. | 

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

# **conversation_message_disassociate_range**
> conversation_message_disassociate_range(message, range)

/message/{message}/ranges/disassociate/{range} [POST]

This will enable us to disassociate a conversation_message from a range. This will do the same thing as the range equivalent.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    range = 'range_example' # str | This is a identifier that is used to identify a specific range.

    try:
        # /message/{message}/ranges/disassociate/{range} [POST]
        api_instance.conversation_message_disassociate_range(message, range)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->conversation_message_disassociate_range: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
 **range** | **str**| This is a identifier that is used to identify a specific range. | 

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

# **conversation_message_disassociate_tag**
> conversation_message_disassociate_tag(message, tag)

/message/{message}/tags/disassociate/{tag} [POST]

This will enable us to disassociate a conversation_message from a tag. This will do the same thing as the tag equivalent.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    tag = 'tag_example' # str | tag id

    try:
        # /message/{message}/tags/disassociate/{tag} [POST]
        api_instance.conversation_message_disassociate_tag(message, tag)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->conversation_message_disassociate_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **conversation_message_disassociate_workstream_event**
> conversation_message_disassociate_workstream_event(message, workstream_event)

/message/{message}/workstream_events/disassociate/{workstream_event} [POST]

This will enable us to disassociate a conversation_message from a workstream_event. This will do the same thing as the workstream_event equivalent.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.

    try:
        # /message/{message}/workstream_events/disassociate/{workstream_event} [POST]
        api_instance.conversation_message_disassociate_workstream_event(message, workstream_event)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->conversation_message_disassociate_workstream_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **conversation_message_disassociate_workstream_pattern_engine_source**
> conversation_message_disassociate_workstream_pattern_engine_source(message, source)

/message/{message}/workstream_pattern_engine/sources/disassociate/{source} [POST]

This will enable us to disassociate a conversation_message from a source. This will do the same thing as the source equivalent.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    source = 'source_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSource

    try:
        # /message/{message}/workstream_pattern_engine/sources/disassociate/{source} [POST]
        api_instance.conversation_message_disassociate_workstream_pattern_engine_source(message, source)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->conversation_message_disassociate_workstream_pattern_engine_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **conversation_message_disassociate_workstream_summary**
> conversation_message_disassociate_workstream_summary(message, workstream_summary)

/message/{message}/workstream_summaries/disassociate/{workstream_summary} [POST]

This will enable us to disassociate a conversation_message from a workstream_summary. This will do the same thing as the workstream_summary equivalent.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /message/{message}/workstream_summaries/disassociate/{workstream_summary} [POST]
        api_instance.conversation_message_disassociate_workstream_summary(message, workstream_summary)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->conversation_message_disassociate_workstream_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **message_associate_anchor**
> message_associate_anchor(message, anchor)

/message/{message}/anchors/associate/{anchor} [POST]

This will associate a message with an anchor.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /message/{message}/anchors/associate/{anchor} [POST]
        api_instance.message_associate_anchor(message, anchor)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->message_associate_anchor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **message_associate_annotation**
> message_associate_annotation(annotation, message)

/message/{message}/annotations/associate/{annotation} [POST]

This will associate a message with an annotation.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    message = 'message_example' # str | This is the uuid of a message.

    try:
        # /message/{message}/annotations/associate/{annotation} [POST]
        api_instance.message_associate_annotation(annotation, message)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->message_associate_annotation: %s\n" % e)
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

# **message_associate_person**
> message_associate_person(message, person)

/message/{message}/persons/associate/{person} [POST]

This will associate a message with a person.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /message/{message}/persons/associate/{person} [POST]
        api_instance.message_associate_person(message, person)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->message_associate_person: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **message_associate_website**
> message_associate_website(message, website)

Associate a message with a website

This will associate a message with a website.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    website = 'website_example' # str | website id

    try:
        # Associate a message with a website
        api_instance.message_associate_website(message, website)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->message_associate_website: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **message_disassociate_anchor**
> message_disassociate_anchor(message, anchor)

/message/{message}/anchors/disassociate/{anchor} [POST]

This will enable us to disassociate a message from an anchor.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /message/{message}/anchors/disassociate/{anchor} [POST]
        api_instance.message_disassociate_anchor(message, anchor)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->message_disassociate_anchor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **message_disassociate_annotation**
> message_disassociate_annotation(annotation, message)

/message/{message}/annotations/disassociate/{annotation} [POST]

This will enable us to dissassociate a message from an annotation.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.
    message = 'message_example' # str | This is the uuid of a message.

    try:
        # /message/{message}/annotations/disassociate/{annotation} [POST]
        api_instance.message_disassociate_annotation(annotation, message)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->message_disassociate_annotation: %s\n" % e)
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

# **message_disassociate_person**
> message_disassociate_person(message, person)

/message/{message}/persons/disassociate/{person} [POST]

This will enable us to disassociate a message from a person.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /message/{message}/persons/disassociate/{person} [POST]
        api_instance.message_disassociate_person(message, person)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->message_disassociate_person: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **message_disassociate_website**
> message_disassociate_website(message, website)

/message/{message}/websites/disassociate/{website} [POST]

This will enable us to disassociate a message from a website.

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    website = 'website_example' # str | website id

    try:
        # /message/{message}/websites/disassociate/{website} [POST]
        api_instance.message_disassociate_website(message, website)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->message_disassociate_website: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **message_scores_increment**
> message_scores_increment(message, seeded_score_increment=seeded_score_increment)

'/message/{message}/scores/increment' [POST]

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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    seeded_score_increment = pieces_os_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # '/message/{message}/scores/increment' [POST]
        api_instance.message_scores_increment(message, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->message_scores_increment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
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

# **message_specific_message_snapshot**
> ConversationMessage message_specific_message_snapshot(message, transferables=transferables)

/message/{message} [GET]

This will get a specific snapshot of a message

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.conversation_message import ConversationMessage
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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /message/{message} [GET]
        api_response = api_instance.message_specific_message_snapshot(message, transferables=transferables)
        print("The response of ConversationMessageApi->message_specific_message_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->message_specific_message_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| This is the uuid of a message. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**ConversationMessage**](ConversationMessage.md)

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

# **message_specific_message_update**
> ConversationMessage message_specific_message_update(transferables=transferables, conversation_message=conversation_message)

/message/update [GET]

This will update a conversation message.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.conversation_message import ConversationMessage
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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    conversation_message = pieces_os_client.ConversationMessage() # ConversationMessage |  (optional)

    try:
        # /message/update [GET]
        api_response = api_instance.message_specific_message_update(transferables=transferables, conversation_message=conversation_message)
        print("The response of ConversationMessageApi->message_specific_message_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->message_specific_message_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **conversation_message** | [**ConversationMessage**](ConversationMessage.md)|  | [optional] 

### Return type

[**ConversationMessage**](ConversationMessage.md)

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

# **message_update_value**
> ConversationMessage message_update_value(transferables=transferables, conversation_message=conversation_message)

/message/update/value [POST]

This will update the value of a conversation message.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.conversation_message import ConversationMessage
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
    api_instance = pieces_os_client.ConversationMessageApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    conversation_message = pieces_os_client.ConversationMessage() # ConversationMessage |  (optional)

    try:
        # /message/update/value [POST]
        api_response = api_instance.message_update_value(transferables=transferables, conversation_message=conversation_message)
        print("The response of ConversationMessageApi->message_update_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationMessageApi->message_update_value: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **conversation_message** | [**ConversationMessage**](ConversationMessage.md)|  | [optional] 

### Return type

[**ConversationMessage**](ConversationMessage.md)

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

