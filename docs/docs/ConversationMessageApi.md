# openapi_client.ConversationMessageApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**message_associate_annotation**](ConversationMessageApi.md#message_associate_annotation) | **POST** /message/{message}/annotations/associate/{annotation} | /message/{message}/annotations/associate/{annotation} [POST]
[**message_disassociate_annotation**](ConversationMessageApi.md#message_disassociate_annotation) | **POST** /message/{message}/annotations/disassociate/{annotation} | /message/{message}/annotations/disassociate/{annotation} [POST]
[**message_scores_increment**](ConversationMessageApi.md#message_scores_increment) | **POST** /message/{message}/scores/increment | &#39;/message/{message}/scores/increment&#39; [POST]
[**message_specific_message_snapshot**](ConversationMessageApi.md#message_specific_message_snapshot) | **GET** /message/{message} | /message/{message} [GET]
[**message_specific_message_update**](ConversationMessageApi.md#message_specific_message_update) | **POST** /message/update | /message/update [GET]


# **message_associate_annotation**
> message_associate_annotation(annotation, message)

/message/{message}/annotations/associate/{annotation} [POST]

This will associate a message with an annotation.

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ConversationMessageApi(api_client)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ConversationMessageApi(api_client)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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

```python
import time
import os
import openapi_client
from openapi_client.models.seeded_score_increment import SeededScoreIncrement
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ConversationMessageApi(api_client)
    message = 'message_example' # str | This is the uuid of a message.
    seeded_score_increment = openapi_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

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

```python
import time
import os
import openapi_client
from openapi_client.models.conversation_message import ConversationMessage
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ConversationMessageApi(api_client)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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

```python
import time
import os
import openapi_client
from openapi_client.models.conversation_message import ConversationMessage
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ConversationMessageApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    conversation_message = openapi_client.ConversationMessage() # ConversationMessage |  (optional)

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

