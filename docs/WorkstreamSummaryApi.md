# pieces_os_client.WorkstreamSummaryApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workstream_summaries_specific_workstream_summary_snapshot**](WorkstreamSummaryApi.md#workstream_summaries_specific_workstream_summary_snapshot) | **GET** /workstream_summary/{workstream_summary} | /workstream_summary/{workstream_summary} [GET]
[**workstream_summary_associate_anchor**](WorkstreamSummaryApi.md#workstream_summary_associate_anchor) | **POST** /workstream_summary/{workstream_summary}/anchors/associate/{anchor} | /workstream_summary/{workstream_summary}/anchors/associate/{anchor} [POST]
[**workstream_summary_associate_asset**](WorkstreamSummaryApi.md#workstream_summary_associate_asset) | **POST** /workstream_summary/{workstream_summary}/assets/associate/{asset} | /workstream_summary/{workstream_summary}/assets/associate/{asset} [POST]
[**workstream_summary_associate_conversation**](WorkstreamSummaryApi.md#workstream_summary_associate_conversation) | **POST** /workstream_summary/{workstream_summary}/conversations/associate/{conversation} | /workstream_summary/{workstream_summary}/conversations/associate/{conversation} [POST]
[**workstream_summary_associate_conversation_message**](WorkstreamSummaryApi.md#workstream_summary_associate_conversation_message) | **POST** /workstream_summary/{workstream_summary}/messages/associate/{message} | /workstream_summary/{workstream_summary}/messages/associate/{message} [POST]
[**workstream_summary_associate_person**](WorkstreamSummaryApi.md#workstream_summary_associate_person) | **POST** /workstream_summary/{workstream_summary}/persons/associate/{person} | /workstream_summary/{workstream_summary}/persons/associate/{person} [POST]
[**workstream_summary_associate_range**](WorkstreamSummaryApi.md#workstream_summary_associate_range) | **POST** /workstream_summary/{workstream_summary}/ranges/associate/{range} | /workstream_summary/{workstream_summary}/ranges/associate/{range} [POST]
[**workstream_summary_associate_tag**](WorkstreamSummaryApi.md#workstream_summary_associate_tag) | **POST** /workstream_summary/{workstream_summary}/tags/associate/{tag} | /workstream_summary/{workstream_summary}/tags/associate/{tag} [POST]
[**workstream_summary_associate_website**](WorkstreamSummaryApi.md#workstream_summary_associate_website) | **POST** /workstream_summary/{workstream_summary}/websites/associate/{website} | /workstream_summary/{workstream_summary}/websites/associate/{website} [POST]
[**workstream_summary_associate_workstream_event**](WorkstreamSummaryApi.md#workstream_summary_associate_workstream_event) | **POST** /workstream_summary/{workstream_summary}/workstream_events/associate/{workstream_event} | /workstream_summary/{workstream_summary}/workstream_events/associate/{workstream_event} [POST]
[**workstream_summary_associate_workstream_pattern_engine_source**](WorkstreamSummaryApi.md#workstream_summary_associate_workstream_pattern_engine_source) | **POST** /workstream_summary/{workstream_summary}/workstream_pattern_engine/sources/associate/{source} | /workstream_summary/{workstream_summary}/workstream_pattern_engine/sources/associate/{source} [POST]
[**workstream_summary_disassociate_anchor**](WorkstreamSummaryApi.md#workstream_summary_disassociate_anchor) | **POST** /workstream_summary/{workstream_summary}/anchors/disassociate/{anchor} | /workstream_summary/{workstream_summary}/anchors/disassociate/{anchor} [POST]
[**workstream_summary_disassociate_asset**](WorkstreamSummaryApi.md#workstream_summary_disassociate_asset) | **POST** /workstream_summary/{workstream_summary}/assets/disassociate/{asset} | /workstream_summary/{workstream_summary}/assets/disassociate/{asset} [POST]
[**workstream_summary_disassociate_conversation**](WorkstreamSummaryApi.md#workstream_summary_disassociate_conversation) | **POST** /workstream_summary/{workstream_summary}/conversations/disassociate/{conversation} | /workstream_summary/{workstream_summary}/conversations/disassociate/{conversation} [POST]
[**workstream_summary_disassociate_conversation_message**](WorkstreamSummaryApi.md#workstream_summary_disassociate_conversation_message) | **POST** /workstream_summary/{workstream_summary}/messages/disassociate/{message} | /workstream_summary/{workstream_summary}/messages/disassociate/{message} [POST]
[**workstream_summary_disassociate_person**](WorkstreamSummaryApi.md#workstream_summary_disassociate_person) | **POST** /workstream_summary/{workstream_summary}/persons/disassociate/{person} | /workstream_summary/{workstream_summary}/persons/disassociate/{person} [POST]
[**workstream_summary_disassociate_range**](WorkstreamSummaryApi.md#workstream_summary_disassociate_range) | **POST** /workstream_summary/{workstream_summary}/ranges/disassociate/{range} | /workstream_summary/{workstream_summary}/ranges/disassociate/{range} [POST]
[**workstream_summary_disassociate_tag**](WorkstreamSummaryApi.md#workstream_summary_disassociate_tag) | **POST** /workstream_summary/{workstream_summary}/tags/disassociate/{tag} | /workstream_summary/{workstream_summary}/tags/disassociate/{tag} [POST]
[**workstream_summary_disassociate_website**](WorkstreamSummaryApi.md#workstream_summary_disassociate_website) | **POST** /workstream_summary/{workstream_summary}/websites/disassociate/{website} | /workstream_summary/{workstream_summary}/websites/disassociate/{website} [POST]
[**workstream_summary_disassociate_workstream_event**](WorkstreamSummaryApi.md#workstream_summary_disassociate_workstream_event) | **POST** /workstream_summary/{workstream_summary}/workstream_events/disassociate/{workstream_event} | /workstream_summary/{workstream_summary}/workstream_events/disassociate/{workstream_event} [POST]
[**workstream_summary_disassociate_workstream_pattern_engine_source**](WorkstreamSummaryApi.md#workstream_summary_disassociate_workstream_pattern_engine_source) | **POST** /workstream_summary/{workstream_summary}/workstream_pattern_engine/sources/disassociate/{source} | /workstream_summary/{workstream_summary}/workstream_pattern_engine/sources/disassociate/{source} [POST]
[**workstream_summary_regenerate_specific_summary**](WorkstreamSummaryApi.md#workstream_summary_regenerate_specific_summary) | **POST** /workstream_summary/{workstream_summary}/regenerate/summary | /workstream_summary/{workstream_summary}/regenerate/summary [POST]
[**workstream_summary_scores_increment**](WorkstreamSummaryApi.md#workstream_summary_scores_increment) | **POST** /workstream_summary/{workstream_summary}/scores/increment | &#39;/workstream_summary/{workstream_summary}/scores/increment&#39; [POST]
[**workstream_summary_update**](WorkstreamSummaryApi.md#workstream_summary_update) | **POST** /workstream_summary/update | /workstream_summary/update [POST]


# **workstream_summaries_specific_workstream_summary_snapshot**
> WorkstreamSummary workstream_summaries_specific_workstream_summary_snapshot(workstream_summary, transferables=transferables)

/workstream_summary/{workstream_summary} [GET]

This will get a snapshot of a single workstream_summary.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_summary import WorkstreamSummary
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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /workstream_summary/{workstream_summary} [GET]
        api_response = api_instance.workstream_summaries_specific_workstream_summary_snapshot(workstream_summary, transferables=transferables)
        print("The response of WorkstreamSummaryApi->workstream_summaries_specific_workstream_summary_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summaries_specific_workstream_summary_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**WorkstreamSummary**](WorkstreamSummary.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**410** | WorkstreamSummary not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workstream_summary_associate_anchor**
> workstream_summary_associate_anchor(workstream_summary, anchor)

/workstream_summary/{workstream_summary}/anchors/associate/{anchor} [POST]

This will associate a anchor with a workstream_summary. This will do the same thing as the anchor equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /workstream_summary/{workstream_summary}/anchors/associate/{anchor} [POST]
        api_instance.workstream_summary_associate_anchor(workstream_summary, anchor)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_associate_anchor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_associate_asset**
> workstream_summary_associate_asset(workstream_summary, asset)

/workstream_summary/{workstream_summary}/assets/associate/{asset} [POST]

This will associate an asset with a workstream_summary. This will do the same thing as the asset equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /workstream_summary/{workstream_summary}/assets/associate/{asset} [POST]
        api_instance.workstream_summary_associate_asset(workstream_summary, asset)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_associate_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_associate_conversation**
> workstream_summary_associate_conversation(workstream_summary, conversation)

/workstream_summary/{workstream_summary}/conversations/associate/{conversation} [POST]

This will associate an conversation with a workstream_summary. This will do the same thing as the conversation equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    conversation = 'conversation_example' # str | This is the uuid of a conversation.

    try:
        # /workstream_summary/{workstream_summary}/conversations/associate/{conversation} [POST]
        api_instance.workstream_summary_associate_conversation(workstream_summary, conversation)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_associate_conversation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_associate_conversation_message**
> workstream_summary_associate_conversation_message(workstream_summary, message)

/workstream_summary/{workstream_summary}/messages/associate/{message} [POST]

This will associate a workstream_summary with a conversation_message. This will do the same thing as the conversation_message equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    message = 'message_example' # str | This is the uuid of a message.

    try:
        # /workstream_summary/{workstream_summary}/messages/associate/{message} [POST]
        api_instance.workstream_summary_associate_conversation_message(workstream_summary, message)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_associate_conversation_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_associate_person**
> workstream_summary_associate_person(workstream_summary, person)

/workstream_summary/{workstream_summary}/persons/associate/{person} [POST]

This will associate an person with a workstream_summary. This will do the same thing as the person equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /workstream_summary/{workstream_summary}/persons/associate/{person} [POST]
        api_instance.workstream_summary_associate_person(workstream_summary, person)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_associate_person: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_associate_range**
> workstream_summary_associate_range(workstream_summary, range)

/workstream_summary/{workstream_summary}/ranges/associate/{range} [POST]

This will associate a range with a workstream_summary. This will do the same thing as the range equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    range = 'range_example' # str | This is a identifier that is used to identify a specific range.

    try:
        # /workstream_summary/{workstream_summary}/ranges/associate/{range} [POST]
        api_instance.workstream_summary_associate_range(workstream_summary, range)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_associate_range: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_associate_tag**
> workstream_summary_associate_tag(workstream_summary, tag)

/workstream_summary/{workstream_summary}/tags/associate/{tag} [POST]

This will associate a workstream_summary with a tag. This will do the same thing as the tag equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    tag = 'tag_example' # str | tag id

    try:
        # /workstream_summary/{workstream_summary}/tags/associate/{tag} [POST]
        api_instance.workstream_summary_associate_tag(workstream_summary, tag)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_associate_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_associate_website**
> workstream_summary_associate_website(workstream_summary, website)

/workstream_summary/{workstream_summary}/websites/associate/{website} [POST]

This will associate a website with a workstream_summary. This will do the same thing as the website equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    website = 'website_example' # str | website id

    try:
        # /workstream_summary/{workstream_summary}/websites/associate/{website} [POST]
        api_instance.workstream_summary_associate_website(workstream_summary, website)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_associate_website: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_associate_workstream_event**
> workstream_summary_associate_workstream_event(workstream_summary, workstream_event)

/workstream_summary/{workstream_summary}/workstream_events/associate/{workstream_event} [POST]

This will associate a workstream_summary with a workstream_event. This will do the same thing as the workstream_event equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.

    try:
        # /workstream_summary/{workstream_summary}/workstream_events/associate/{workstream_event} [POST]
        api_instance.workstream_summary_associate_workstream_event(workstream_summary, workstream_event)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_associate_workstream_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_associate_workstream_pattern_engine_source**
> workstream_summary_associate_workstream_pattern_engine_source(workstream_summary, source)

/workstream_summary/{workstream_summary}/workstream_pattern_engine/sources/associate/{source} [POST]

This will associate a workstream_summary with a workstream_pattern_engine_source. This will do the same thing as the workstream_pattern_engine_source equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    source = 'source_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSource

    try:
        # /workstream_summary/{workstream_summary}/workstream_pattern_engine/sources/associate/{source} [POST]
        api_instance.workstream_summary_associate_workstream_pattern_engine_source(workstream_summary, source)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_associate_workstream_pattern_engine_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_disassociate_anchor**
> workstream_summary_disassociate_anchor(workstream_summary, anchor)

/workstream_summary/{workstream_summary}/anchors/disassociate/{anchor} [POST]

This will enable us to disassociate a anchor from a workstream_summary. This will do the same thing as the anchor equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /workstream_summary/{workstream_summary}/anchors/disassociate/{anchor} [POST]
        api_instance.workstream_summary_disassociate_anchor(workstream_summary, anchor)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_disassociate_anchor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_disassociate_asset**
> workstream_summary_disassociate_asset(workstream_summary, asset)

/workstream_summary/{workstream_summary}/assets/disassociate/{asset} [POST]

This will enable us to disassociate a asset from a workstream_summary. This will do the same thing as the asset equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /workstream_summary/{workstream_summary}/assets/disassociate/{asset} [POST]
        api_instance.workstream_summary_disassociate_asset(workstream_summary, asset)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_disassociate_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_disassociate_conversation**
> workstream_summary_disassociate_conversation(workstream_summary, conversation)

/workstream_summary/{workstream_summary}/conversations/disassociate/{conversation} [POST]

This will enable us to disassociate a conversation from a workstream_summary. This will do the same thing as the conversation equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    conversation = 'conversation_example' # str | This is the uuid of a conversation.

    try:
        # /workstream_summary/{workstream_summary}/conversations/disassociate/{conversation} [POST]
        api_instance.workstream_summary_disassociate_conversation(workstream_summary, conversation)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_disassociate_conversation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_disassociate_conversation_message**
> workstream_summary_disassociate_conversation_message(workstream_summary, message)

/workstream_summary/{workstream_summary}/messages/disassociate/{message} [POST]

This will enable us to disassociate a conversation_message from an workstream_summary. This will do the same thing as the conversation_message equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    message = 'message_example' # str | This is the uuid of a message.

    try:
        # /workstream_summary/{workstream_summary}/messages/disassociate/{message} [POST]
        api_instance.workstream_summary_disassociate_conversation_message(workstream_summary, message)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_disassociate_conversation_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_disassociate_person**
> workstream_summary_disassociate_person(workstream_summary, person)

/workstream_summary/{workstream_summary}/persons/disassociate/{person} [POST]

This will enable us to disassociate a person from a workstream_summary. This will do the same thing as the person equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /workstream_summary/{workstream_summary}/persons/disassociate/{person} [POST]
        api_instance.workstream_summary_disassociate_person(workstream_summary, person)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_disassociate_person: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_disassociate_range**
> workstream_summary_disassociate_range(workstream_summary, range)

/workstream_summary/{workstream_summary}/ranges/disassociate/{range} [POST]

This will enable us to disassociate a range from a workstream_summary. This will do the same thing as the range equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    range = 'range_example' # str | This is a identifier that is used to identify a specific range.

    try:
        # /workstream_summary/{workstream_summary}/ranges/disassociate/{range} [POST]
        api_instance.workstream_summary_disassociate_range(workstream_summary, range)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_disassociate_range: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_disassociate_tag**
> workstream_summary_disassociate_tag(workstream_summary, tag)

/workstream_summary/{workstream_summary}/tags/disassociate/{tag} [POST]

This will enable us to disassociate a workstream_summary from a tag. This will do the same thing as the tag equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    tag = 'tag_example' # str | tag id

    try:
        # /workstream_summary/{workstream_summary}/tags/disassociate/{tag} [POST]
        api_instance.workstream_summary_disassociate_tag(workstream_summary, tag)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_disassociate_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_disassociate_website**
> workstream_summary_disassociate_website(workstream_summary, website)

/workstream_summary/{workstream_summary}/websites/disassociate/{website} [POST]

This will enable us to disassociate a website from a workstream_summary. This will do the same thing as the website equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    website = 'website_example' # str | website id

    try:
        # /workstream_summary/{workstream_summary}/websites/disassociate/{website} [POST]
        api_instance.workstream_summary_disassociate_website(workstream_summary, website)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_disassociate_website: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_disassociate_workstream_event**
> workstream_summary_disassociate_workstream_event(workstream_summary, workstream_event)

/workstream_summary/{workstream_summary}/workstream_events/disassociate/{workstream_event} [POST]

This will enable us to disassociate a workstream_summary from a workstream_event. This will do the same thing as the workstream_event equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.

    try:
        # /workstream_summary/{workstream_summary}/workstream_events/disassociate/{workstream_event} [POST]
        api_instance.workstream_summary_disassociate_workstream_event(workstream_summary, workstream_event)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_disassociate_workstream_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_disassociate_workstream_pattern_engine_source**
> workstream_summary_disassociate_workstream_pattern_engine_source(workstream_summary, source)

/workstream_summary/{workstream_summary}/workstream_pattern_engine/sources/disassociate/{source} [POST]

This will enable us to disassociate a workstream_summary from a workstream_pattern_engine_source. This will do the same thing as the workstream_pattern_engine_source equivalent.

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    source = 'source_example' # str | This is a identifier that is used to identify a specific WorkstreamPatternEngineSource

    try:
        # /workstream_summary/{workstream_summary}/workstream_pattern_engine/sources/disassociate/{source} [POST]
        api_instance.workstream_summary_disassociate_workstream_pattern_engine_source(workstream_summary, source)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_disassociate_workstream_pattern_engine_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_regenerate_specific_summary**
> WorkstreamSummary workstream_summary_regenerate_specific_summary(workstream_summary, transferables=transferables)

/workstream_summary/{workstream_summary}/regenerate/summary [POST]

This will regenerate a summary for a given summary ID, this can allow additional properties in the future 
but it will just regen for now

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_summary import WorkstreamSummary
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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /workstream_summary/{workstream_summary}/regenerate/summary [POST]
        api_response = api_instance.workstream_summary_regenerate_specific_summary(workstream_summary, transferables=transferables)
        print("The response of WorkstreamSummaryApi->workstream_summary_regenerate_specific_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_regenerate_specific_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**WorkstreamSummary**](WorkstreamSummary.md)

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
**511** | if we return a 511, they need to adjust their processing to blended or cloud for all of their models. |  -  |
**412** | if we return a 412, this means that the summary was set to local or the events were in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workstream_summary_scores_increment**
> workstream_summary_scores_increment(workstream_summary, seeded_score_increment=seeded_score_increment)

'/workstream_summary/{workstream_summary}/scores/increment' [POST]

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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.
    seeded_score_increment = pieces_os_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # '/workstream_summary/{workstream_summary}/scores/increment' [POST]
        api_instance.workstream_summary_scores_increment(workstream_summary, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_scores_increment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 
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

# **workstream_summary_update**
> WorkstreamSummary workstream_summary_update(transferables=transferables, workstream_summary=workstream_summary)

/workstream_summary/update [POST]

This will update a specific workstream_summary.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_summary import WorkstreamSummary
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
    api_instance = pieces_os_client.WorkstreamSummaryApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    workstream_summary = pieces_os_client.WorkstreamSummary() # WorkstreamSummary |  (optional)

    try:
        # /workstream_summary/update [POST]
        api_response = api_instance.workstream_summary_update(transferables=transferables, workstream_summary=workstream_summary)
        print("The response of WorkstreamSummaryApi->workstream_summary_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamSummaryApi->workstream_summary_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **workstream_summary** | [**WorkstreamSummary**](WorkstreamSummary.md)|  | [optional] 

### Return type

[**WorkstreamSummary**](WorkstreamSummary.md)

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

