# pieces_os_client.ConversationMessageApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
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


# **message_associate_anchor**
> message_associate_anchor(message, anchor)

/message/{message}/anchors/associate/{anchor} [POST]

This will associate a message with an anchor.

### Example

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

