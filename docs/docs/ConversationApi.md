# openapi_client.ConversationApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversation_associate_anchor**](ConversationApi.md#conversation_associate_anchor) | **POST** /conversation/{conversation}/anchors/associate/{anchor} | /conversation/{conversation}/anchors/associate/{anchor} [POST]
[**conversation_associate_asset**](ConversationApi.md#conversation_associate_asset) | **POST** /conversation/{conversation}/assets/associate/{asset} | /conversation/{conversation}/assets/associate/{asset} [POST]
[**conversation_associate_website**](ConversationApi.md#conversation_associate_website) | **POST** /conversation/{conversation}/websites/associate/{website} | /conversation/{conversation}/websites/associate/{website} [POST]
[**conversation_disassociate_anchor**](ConversationApi.md#conversation_disassociate_anchor) | **POST** /conversation/{conversation}/anchors/delete/{anchor} | /conversation/{conversation}/anchors/delete/{anchor} [POST]
[**conversation_disassociate_asset**](ConversationApi.md#conversation_disassociate_asset) | **POST** /conversation/{conversation}/assets/delete/{asset} | /conversation/{conversation}/assets/delete/{asset} [POST]
[**conversation_disassociate_website**](ConversationApi.md#conversation_disassociate_website) | **POST** /conversation/{conversation}/websites/disassociate/{website} | /website/{website}/websites/disassociate/{website} [POST]
[**conversation_get_specific_conversation**](ConversationApi.md#conversation_get_specific_conversation) | **GET** /conversation/{conversation} | /conversation/{conversation} [GET]
[**conversation_grounding_messages_associate_message**](ConversationApi.md#conversation_grounding_messages_associate_message) | **POST** /conversation/{conversation}/grounding/messages/associate/{message} | /conversation/{conversation}/grounding/messages/associate/{message} [POST]
[**conversation_grounding_messages_disassociate_message**](ConversationApi.md#conversation_grounding_messages_disassociate_message) | **POST** /conversation/{conversation}/grounding/messages/disassociate/{message} | /conversation/{conversation}/grounding/messages/disassociate/{message} [POST]
[**conversation_scores_increment**](ConversationApi.md#conversation_scores_increment) | **POST** /conversation/{conversation}/scores/increment | &#39;/conversation/{conversation}/scores/increment&#39; [POST]
[**conversation_specific_conversation_messages**](ConversationApi.md#conversation_specific_conversation_messages) | **GET** /conversation/{conversation}/messages | /conversation/{conversation}/messages [GET]
[**conversation_specific_conversation_rename**](ConversationApi.md#conversation_specific_conversation_rename) | **POST** /conversation/{conversation}/rename | /conversation/{conversation}/rename [POST]
[**conversation_summarize**](ConversationApi.md#conversation_summarize) | **POST** /conversation/{conversation}/summarize | /conversation/{conversation}/summarize [POST]
[**conversation_update**](ConversationApi.md#conversation_update) | **POST** /conversation/update | /conversation/update [POST]


# **conversation_associate_anchor**
> conversation_associate_anchor(conversation, anchor)

/conversation/{conversation}/anchors/associate/{anchor} [POST]

This will update both the anchor and the conversation.  and associate the 2 together

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
    api_instance = openapi_client.ConversationApi(api_client)
    conversation = 'conversation_example' # str | This is the uuid of a conversation.
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /conversation/{conversation}/anchors/associate/{anchor} [POST]
        api_instance.conversation_associate_anchor(conversation, anchor)
    except Exception as e:
        print("Exception when calling ConversationApi->conversation_associate_anchor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation** | **str**| This is the uuid of a conversation. | 
 **anchor** | **str**| This is the specific uuid of an anchor. | 

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

# **conversation_associate_asset**
> conversation_associate_asset(conversation, asset)

/conversation/{conversation}/assets/associate/{asset} [POST]

This will update both the asset and the conversation.  and associate the 2 together

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
    api_instance = openapi_client.ConversationApi(api_client)
    conversation = 'conversation_example' # str | This is the uuid of a conversation.
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /conversation/{conversation}/assets/associate/{asset} [POST]
        api_instance.conversation_associate_asset(conversation, asset)
    except Exception as e:
        print("Exception when calling ConversationApi->conversation_associate_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation** | **str**| This is the uuid of a conversation. | 
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 

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

# **conversation_associate_website**
> conversation_associate_website(conversation, website)

/conversation/{conversation}/websites/associate/{website} [POST]

This will update both the website and the conversation.  and associate the 2 together

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
    api_instance = openapi_client.ConversationApi(api_client)
    conversation = 'conversation_example' # str | This is the uuid of a conversation.
    website = 'website_example' # str | website id

    try:
        # /conversation/{conversation}/websites/associate/{website} [POST]
        api_instance.conversation_associate_website(conversation, website)
    except Exception as e:
        print("Exception when calling ConversationApi->conversation_associate_website: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation** | **str**| This is the uuid of a conversation. | 
 **website** | **str**| website id | 

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

# **conversation_disassociate_anchor**
> conversation_disassociate_anchor(conversation, anchor)

/conversation/{conversation}/anchors/delete/{anchor} [POST]

This will update both the anchor and the conversation.  and delete(disassociate) the 2 together

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
    api_instance = openapi_client.ConversationApi(api_client)
    conversation = 'conversation_example' # str | This is the uuid of a conversation.
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /conversation/{conversation}/anchors/delete/{anchor} [POST]
        api_instance.conversation_disassociate_anchor(conversation, anchor)
    except Exception as e:
        print("Exception when calling ConversationApi->conversation_disassociate_anchor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation** | **str**| This is the uuid of a conversation. | 
 **anchor** | **str**| This is the specific uuid of an anchor. | 

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

# **conversation_disassociate_asset**
> conversation_disassociate_asset(conversation, asset)

/conversation/{conversation}/assets/delete/{asset} [POST]

This will update both the asset and the conversation.  and delete(disassociate) the 2.

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
    api_instance = openapi_client.ConversationApi(api_client)
    conversation = 'conversation_example' # str | This is the uuid of a conversation.
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /conversation/{conversation}/assets/delete/{asset} [POST]
        api_instance.conversation_disassociate_asset(conversation, asset)
    except Exception as e:
        print("Exception when calling ConversationApi->conversation_disassociate_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation** | **str**| This is the uuid of a conversation. | 
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 

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

# **conversation_disassociate_website**
> conversation_disassociate_website(conversation, website)

/website/{website}/websites/disassociate/{website} [POST]

This will enable us to dissassociate a conversation from a website.

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
    api_instance = openapi_client.ConversationApi(api_client)
    conversation = 'conversation_example' # str | This is the uuid of a conversation.
    website = 'website_example' # str | website id

    try:
        # /website/{website}/websites/disassociate/{website} [POST]
        api_instance.conversation_disassociate_website(conversation, website)
    except Exception as e:
        print("Exception when calling ConversationApi->conversation_disassociate_website: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation** | **str**| This is the uuid of a conversation. | 
 **website** | **str**| website id | 

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

# **conversation_get_specific_conversation**
> Conversation conversation_get_specific_conversation(conversation, transferables=transferables)

/conversation/{conversation} [GET]

This will get a specific conversation.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.conversation import Conversation
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
    api_instance = openapi_client.ConversationApi(api_client)
    conversation = 'conversation_example' # str | This is the uuid of a conversation.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /conversation/{conversation} [GET]
        api_response = api_instance.conversation_get_specific_conversation(conversation, transferables=transferables)
        print("The response of ConversationApi->conversation_get_specific_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationApi->conversation_get_specific_conversation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation** | **str**| This is the uuid of a conversation. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Conversation**](Conversation.md)

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

# **conversation_grounding_messages_associate_message**
> conversation_grounding_messages_associate_message(conversation, message)

/conversation/{conversation}/grounding/messages/associate/{message} [POST]

This will save the grounding context for a conversation. This will enable us to associate a message to the conversation.grounding object.

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
    api_instance = openapi_client.ConversationApi(api_client)
    conversation = 'conversation_example' # str | This is the uuid of a conversation.
    message = 'message_example' # str | This is the uuid of a message.

    try:
        # /conversation/{conversation}/grounding/messages/associate/{message} [POST]
        api_instance.conversation_grounding_messages_associate_message(conversation, message)
    except Exception as e:
        print("Exception when calling ConversationApi->conversation_grounding_messages_associate_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation** | **str**| This is the uuid of a conversation. | 
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

# **conversation_grounding_messages_disassociate_message**
> conversation_grounding_messages_disassociate_message(conversation, message)

/conversation/{conversation}/grounding/messages/disassociate/{message} [POST]

This will remove specific grounding context for a conversation. This will enable us to dissassociate a message from the conversation.grounding object.

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
    api_instance = openapi_client.ConversationApi(api_client)
    conversation = 'conversation_example' # str | This is the uuid of a conversation.
    message = 'message_example' # str | This is the uuid of a message.

    try:
        # /conversation/{conversation}/grounding/messages/disassociate/{message} [POST]
        api_instance.conversation_grounding_messages_disassociate_message(conversation, message)
    except Exception as e:
        print("Exception when calling ConversationApi->conversation_grounding_messages_disassociate_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation** | **str**| This is the uuid of a conversation. | 
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

# **conversation_scores_increment**
> conversation_scores_increment(conversation, seeded_score_increment=seeded_score_increment)

'/conversation/{conversation}/scores/increment' [POST]

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
    api_instance = openapi_client.ConversationApi(api_client)
    conversation = 'conversation_example' # str | This is the uuid of a conversation.
    seeded_score_increment = openapi_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # '/conversation/{conversation}/scores/increment' [POST]
        api_instance.conversation_scores_increment(conversation, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling ConversationApi->conversation_scores_increment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation** | **str**| This is the uuid of a conversation. | 
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

# **conversation_specific_conversation_messages**
> ConversationMessages conversation_specific_conversation_messages(conversation, transferables=transferables)

/conversation/{conversation}/messages [GET]

This will get a specific conversations messages

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.conversation_messages import ConversationMessages
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
    api_instance = openapi_client.ConversationApi(api_client)
    conversation = 'conversation_example' # str | This is the uuid of a conversation.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /conversation/{conversation}/messages [GET]
        api_response = api_instance.conversation_specific_conversation_messages(conversation, transferables=transferables)
        print("The response of ConversationApi->conversation_specific_conversation_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationApi->conversation_specific_conversation_messages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation** | **str**| This is the uuid of a conversation. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**ConversationMessages**](ConversationMessages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversation_specific_conversation_rename**
> Conversation conversation_specific_conversation_rename(conversation, transferables=transferables)

/conversation/{conversation}/rename [POST]

This will take a specific converssation and it will rename using ML.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.conversation import Conversation
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
    api_instance = openapi_client.ConversationApi(api_client)
    conversation = 'conversation_example' # str | This is the uuid of a conversation.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /conversation/{conversation}/rename [POST]
        api_response = api_instance.conversation_specific_conversation_rename(conversation, transferables=transferables)
        print("The response of ConversationApi->conversation_specific_conversation_rename:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationApi->conversation_specific_conversation_rename: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation** | **str**| This is the uuid of a conversation. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Conversation**](Conversation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversation_summarize**
> ConversationSummarizeOutput conversation_summarize(conversation, conversation_summarize_input=conversation_summarize_input)

/conversation/{conversation}/summarize [POST]

This will take a current conversation and create a summary of the conversation and save it as an annotation on the conversation.  will return the annotation reference used as the summary.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.conversation_summarize_input import ConversationSummarizeInput
from openapi_client.models.conversation_summarize_output import ConversationSummarizeOutput
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
    api_instance = openapi_client.ConversationApi(api_client)
    conversation = 'conversation_example' # str | This is the uuid of a conversation.
    conversation_summarize_input = openapi_client.ConversationSummarizeInput() # ConversationSummarizeInput |  (optional)

    try:
        # /conversation/{conversation}/summarize [POST]
        api_response = api_instance.conversation_summarize(conversation, conversation_summarize_input=conversation_summarize_input)
        print("The response of ConversationApi->conversation_summarize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationApi->conversation_summarize: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation** | **str**| This is the uuid of a conversation. | 
 **conversation_summarize_input** | [**ConversationSummarizeInput**](ConversationSummarizeInput.md)|  | [optional] 

### Return type

[**ConversationSummarizeOutput**](ConversationSummarizeOutput.md)

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

# **conversation_update**
> Conversation conversation_update(transferables=transferables, conversation=conversation)

/conversation/update [POST]

This will update a specific conversation.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.conversation import Conversation
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
    api_instance = openapi_client.ConversationApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    conversation = openapi_client.Conversation() # Conversation |  (optional)

    try:
        # /conversation/update [POST]
        api_response = api_instance.conversation_update(transferables=transferables, conversation=conversation)
        print("The response of ConversationApi->conversation_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationApi->conversation_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **conversation** | [**Conversation**](Conversation.md)|  | [optional] 

### Return type

[**Conversation**](Conversation.md)

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

