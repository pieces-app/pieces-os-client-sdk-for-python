# pieces_os_client.AnchorApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anchor_associate_asset**](AnchorApi.md#anchor_associate_asset) | **POST** /anchor/{anchor}/assets/associate/{asset} | /anchor/{anchor}/assets/associate/{asset} [POST]
[**anchor_associate_conversation**](AnchorApi.md#anchor_associate_conversation) | **POST** /anchor/{anchor}/conversations/associate/{conversation} | /anchor/{anchor}/conversations/associate/{conversation} [POST]
[**anchor_associate_person**](AnchorApi.md#anchor_associate_person) | **POST** /anchor/{anchor}/persons/associate/{person} | /anchor/{anchor}/persons/associate/{person} [POST]
[**anchor_associate_workstream_summary**](AnchorApi.md#anchor_associate_workstream_summary) | **POST** /anchor/{anchor}/workstream_summaries/associate/{workstream_summary} | /anchor/{anchor}/workstream_summaries/associate/{workstream_summary} [POST]
[**anchor_disassociate_asset**](AnchorApi.md#anchor_disassociate_asset) | **POST** /anchor/{anchor}/assets/disassociate/{asset} | /anchor/{anchor}/assets/disassociate/{asset} [POST]
[**anchor_disassociate_conversation**](AnchorApi.md#anchor_disassociate_conversation) | **POST** /anchor/{anchor}/conversations/disassociate/{conversation} | /anchor/{anchor}/conversations/disassociate/{conversation} [POST]
[**anchor_disassociate_person**](AnchorApi.md#anchor_disassociate_person) | **POST** /anchors/{anchor}/persons/disassociate/{person} | /anchor/{anchor}/persons/disassociate/{person} [POST]
[**anchor_disassociate_workstream_summary**](AnchorApi.md#anchor_disassociate_workstream_summary) | **POST** /anchor/{anchor}/workstream_summaries/disassociate/{workstream_summary} | /anchor/{anchor}/workstream_summaries/disassociate/{workstream_summary} [POST]
[**anchor_rename**](AnchorApi.md#anchor_rename) | **POST** /anchor/{anchor}/rename | /anchor/{anchor}/rename [POST]
[**anchor_scores_increment**](AnchorApi.md#anchor_scores_increment) | **POST** /anchor/{anchor}/scores/increment | &#39;/anchor/{anchor}/scores/increment&#39; [POST]
[**anchor_specific_anchor_snapshot**](AnchorApi.md#anchor_specific_anchor_snapshot) | **GET** /anchor/{anchor} | /anchor/{anchor} [GET]
[**anchor_update**](AnchorApi.md#anchor_update) | **POST** /anchor/update | /anchor/update [POST]


# **anchor_associate_asset**
> anchor_associate_asset(anchor, asset)

/anchor/{anchor}/assets/associate/{asset} [POST]

associates an anchor and an asset. It performs the same action as the asset equivalent.

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
    api_instance = pieces_os_client.AnchorApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /anchor/{anchor}/assets/associate/{asset} [POST]
        api_instance.anchor_associate_asset(anchor, asset)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_associate_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor** | **str**| This is the specific uuid of an anchor. | 
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 

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

# **anchor_associate_conversation**
> anchor_associate_conversation(anchor, conversation)

/anchor/{anchor}/conversations/associate/{conversation} [POST]

associates an anchor and a conversation. It performs the same action as the conversation equivalent.

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
    api_instance = pieces_os_client.AnchorApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.
    conversation = 'conversation_example' # str | This is the uuid of a conversation.

    try:
        # /anchor/{anchor}/conversations/associate/{conversation} [POST]
        api_instance.anchor_associate_conversation(anchor, conversation)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_associate_conversation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor** | **str**| This is the specific uuid of an anchor. | 
 **conversation** | **str**| This is the uuid of a conversation. | 

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

# **anchor_associate_person**
> anchor_associate_person(anchor, person)

/anchor/{anchor}/persons/associate/{person} [POST]

associates an anchor and a person. It performs the same action as the person equivalent.

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
    api_instance = pieces_os_client.AnchorApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /anchor/{anchor}/persons/associate/{person} [POST]
        api_instance.anchor_associate_person(anchor, person)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_associate_person: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor** | **str**| This is the specific uuid of an anchor. | 
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

# **anchor_associate_workstream_summary**
> anchor_associate_workstream_summary(anchor, workstream_summary)

/anchor/{anchor}/workstream_summaries/associate/{workstream_summary} [POST]

This will associate a anchor with a workstream summary. This will do the same thing as the workstreamSummary equivalent.

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
    api_instance = pieces_os_client.AnchorApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /anchor/{anchor}/workstream_summaries/associate/{workstream_summary} [POST]
        api_instance.anchor_associate_workstream_summary(anchor, workstream_summary)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_associate_workstream_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor** | **str**| This is the specific uuid of an anchor. | 
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 

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

# **anchor_disassociate_asset**
> anchor_disassociate_asset(anchor, asset)

/anchor/{anchor}/assets/disassociate/{asset} [POST]

Disassociates an anchor from an asset. It performs the same action as the asset equivalent.

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
    api_instance = pieces_os_client.AnchorApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /anchor/{anchor}/assets/disassociate/{asset} [POST]
        api_instance.anchor_disassociate_asset(anchor, asset)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_disassociate_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor** | **str**| This is the specific uuid of an anchor. | 
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 

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

# **anchor_disassociate_conversation**
> anchor_disassociate_conversation(anchor, conversation)

/anchor/{anchor}/conversations/disassociate/{conversation} [POST]

Disassociates an anchor from a conversation. It performs the same action as the conversation equivalent.

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
    api_instance = pieces_os_client.AnchorApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.
    conversation = 'conversation_example' # str | This is the uuid of a conversation.

    try:
        # /anchor/{anchor}/conversations/disassociate/{conversation} [POST]
        api_instance.anchor_disassociate_conversation(anchor, conversation)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_disassociate_conversation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor** | **str**| This is the specific uuid of an anchor. | 
 **conversation** | **str**| This is the uuid of a conversation. | 

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

# **anchor_disassociate_person**
> anchor_disassociate_person(anchor, person)

/anchor/{anchor}/persons/disassociate/{person} [POST]

Disassociates an anchor from a person. It performs the same action as the person equivalent.

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
    api_instance = pieces_os_client.AnchorApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /anchor/{anchor}/persons/disassociate/{person} [POST]
        api_instance.anchor_disassociate_person(anchor, person)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_disassociate_person: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor** | **str**| This is the specific uuid of an anchor. | 
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

# **anchor_disassociate_workstream_summary**
> anchor_disassociate_workstream_summary(anchor, workstream_summary)

/anchor/{anchor}/workstream_summaries/disassociate/{workstream_summary} [POST]

This will enable us to disassociate a anchor from a workstream summary. This will do the same thing as the workstreamSummary equivalent.

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
    api_instance = pieces_os_client.AnchorApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /anchor/{anchor}/workstream_summaries/disassociate/{workstream_summary} [POST]
        api_instance.anchor_disassociate_workstream_summary(anchor, workstream_summary)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_disassociate_workstream_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor** | **str**| This is the specific uuid of an anchor. | 
 **workstream_summary** | **str**| This is a identifier that is used to identify a specific workstream_summary. | 

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

# **anchor_rename**
> Anchor anchor_rename(anchor, transferables=transferables)

/anchor/{anchor}/rename [POST]

This will rename a specific anchor.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.anchor import Anchor
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
    api_instance = pieces_os_client.AnchorApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /anchor/{anchor}/rename [POST]
        api_response = api_instance.anchor_rename(anchor, transferables=transferables)
        print("The response of AnchorApi->anchor_rename:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_rename: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor** | **str**| This is the specific uuid of an anchor. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Anchor**](Anchor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **anchor_scores_increment**
> anchor_scores_increment(anchor, seeded_score_increment=seeded_score_increment)

'/anchor/{anchor}/scores/increment' [POST]

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
    api_instance = pieces_os_client.AnchorApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.
    seeded_score_increment = pieces_os_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # '/anchor/{anchor}/scores/increment' [POST]
        api_instance.anchor_scores_increment(anchor, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_scores_increment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor** | **str**| This is the specific uuid of an anchor. | 
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

# **anchor_specific_anchor_snapshot**
> Anchor anchor_specific_anchor_snapshot(anchor, transferables=transferables)

/anchor/{anchor} [GET]

This will get a snapshot of a single anchor.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.anchor import Anchor
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
    api_instance = pieces_os_client.AnchorApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /anchor/{anchor} [GET]
        api_response = api_instance.anchor_specific_anchor_snapshot(anchor, transferables=transferables)
        print("The response of AnchorApi->anchor_specific_anchor_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_specific_anchor_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor** | **str**| This is the specific uuid of an anchor. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Anchor**](Anchor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**410** | Anchor not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **anchor_update**
> Anchor anchor_update(transferables=transferables, anchor=anchor)

/anchor/update [POST]

This will update a specific anchor.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.anchor import Anchor
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
    api_instance = pieces_os_client.AnchorApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    anchor = pieces_os_client.Anchor() # Anchor |  (optional)

    try:
        # /anchor/update [POST]
        api_response = api_instance.anchor_update(transferables=transferables, anchor=anchor)
        print("The response of AnchorApi->anchor_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **anchor** | [**Anchor**](Anchor.md)|  | [optional] 

### Return type

[**Anchor**](Anchor.md)

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

