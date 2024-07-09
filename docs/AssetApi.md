# pieces_os_client.AssetApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_associate_anchor**](AssetApi.md#asset_associate_anchor) | **POST** /asset/{asset}/anchors/associate/{anchor} | /asset/{asset}/persons/associate/{anchor} [POST]
[**asset_associate_conversation**](AssetApi.md#asset_associate_conversation) | **POST** /asset/{asset}/conversations/associate/{conversation} | /asset/{asset}/conversations/associate/{conversation} [POST]
[**asset_associate_hint**](AssetApi.md#asset_associate_hint) | **POST** /asset/{asset}/hints/associate/{hint} | /asset/{asset}/hints/associate/{hint} [POST]
[**asset_associate_person**](AssetApi.md#asset_associate_person) | **POST** /asset/{asset}/persons/associate/{person} | /asset/{asset}/persons/associate/{person} [POST]
[**asset_associate_tag**](AssetApi.md#asset_associate_tag) | **POST** /asset/{asset}/tags/associate/{tag} | /asset/{asset}/tags/associate/{tag} [POST]
[**asset_associate_website**](AssetApi.md#asset_associate_website) | **POST** /asset/{asset}/websites/associate/{website} | /asset/{asset}/websites/associate/{website} [POST]
[**asset_associate_workstream_summary**](AssetApi.md#asset_associate_workstream_summary) | **POST** /asset/{asset}/workstream_summaries/associate/{workstream_summary} | /asset/{asset}/workstream_summaries/associate/{workstream_summary} [POST]
[**asset_disassociate_anchor**](AssetApi.md#asset_disassociate_anchor) | **POST** /asset/{asset}/anchors/disassociate/{anchor} | /asset/{asset}/anchors/disassociate/{anchor} [POST]
[**asset_disassociate_conversation**](AssetApi.md#asset_disassociate_conversation) | **POST** /asset/{asset}/conversations/disassociate/{conversation} | /asset/{asset}/conversations/disassociate/{conversation} [POST]
[**asset_disassociate_hint**](AssetApi.md#asset_disassociate_hint) | **POST** /asset/{asset}/hints/disassociate/{hint} | /asset/{asset}/hints/disassociate/{hint} [POST]
[**asset_disassociate_person**](AssetApi.md#asset_disassociate_person) | **POST** /asset/{asset}/persons/disassociate/{person} | /asset/{asset}/persons/disassociate/{person} [POST]
[**asset_disassociate_tag**](AssetApi.md#asset_disassociate_tag) | **POST** /asset/{asset}/tags/disassociate/{tag} | /asset/{asset}/tags/disassociate/{tag} [POST]
[**asset_disassociate_website**](AssetApi.md#asset_disassociate_website) | **POST** /asset/{asset}/websites/disassociate/{website} | /asset/{asset}/websites/disassociate/{website} [POST]
[**asset_disassociate_workstream_summary**](AssetApi.md#asset_disassociate_workstream_summary) | **POST** /asset/{asset}/workstream_summaries/disassociate/{workstream_summary} | /asset/{asset}/workstream_summaries/disassociate/{workstream_summary} [POST]
[**asset_formats**](AssetApi.md#asset_formats) | **GET** /asset/{asset}/formats | /asset/{asset}/formats [GET] Scoped To Asset
[**asset_reclassify**](AssetApi.md#asset_reclassify) | **POST** /asset/reclassify | /asset/reclassify [POST]
[**asset_scores_increment**](AssetApi.md#asset_scores_increment) | **POST** /asset/{asset}/scores/increment | /asset/{asset}/scores/increment [POST]
[**asset_snapshot**](AssetApi.md#asset_snapshot) | **GET** /asset/{asset} | /asset/{asset} [GET] Scoped To Asset
[**asset_snapshot_post**](AssetApi.md#asset_snapshot_post) | **POST** /asset/{asset} | /asset/{asset} [POST] Scoped to an Asset
[**asset_specific_asset_activities**](AssetApi.md#asset_specific_asset_activities) | **GET** /asset/{asset}/activities | /asset/{asset}/activities [GET]
[**asset_specific_asset_conversations**](AssetApi.md#asset_specific_asset_conversations) | **GET** /asset/{asset}/conversations | /asset/{asset}/conversations [GET]
[**asset_specific_asset_export**](AssetApi.md#asset_specific_asset_export) | **GET** /asset/{asset}/export | /asset/{asset}/export [GET]
[**asset_update**](AssetApi.md#asset_update) | **POST** /asset/update | /asset/update [POST] Scoped to Asset


# **asset_associate_anchor**
> asset_associate_anchor(asset, anchor)

/asset/{asset}/persons/associate/{anchor} [POST]

associates an anchor and an asset. It performs the same action as the anchor equivalent.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /asset/{asset}/persons/associate/{anchor} [POST]
        api_instance.asset_associate_anchor(asset, anchor)
    except Exception as e:
        print("Exception when calling AssetApi->asset_associate_anchor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
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

# **asset_associate_conversation**
> asset_associate_conversation(asset, conversation)

/asset/{asset}/conversations/associate/{conversation} [POST]

associates a conversation and an asset. It performs the same action as the conversation equivalent.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    conversation = 'conversation_example' # str | This is the uuid of a conversation.

    try:
        # /asset/{asset}/conversations/associate/{conversation} [POST]
        api_instance.asset_associate_conversation(asset, conversation)
    except Exception as e:
        print("Exception when calling AssetApi->asset_associate_conversation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
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

# **asset_associate_hint**
> asset_associate_hint(asset, hint)

/asset/{asset}/hints/associate/{hint} [POST]

associates an asset and a hint. It performs the same action as the hint equivalent.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    hint = 'hint_example' # str | This is a specific hint uuid

    try:
        # /asset/{asset}/hints/associate/{hint} [POST]
        api_instance.asset_associate_hint(asset, hint)
    except Exception as e:
        print("Exception when calling AssetApi->asset_associate_hint: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **hint** | **str**| This is a specific hint uuid | 

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

# **asset_associate_person**
> asset_associate_person(asset, person)

/asset/{asset}/persons/associate/{person} [POST]

associates a person and an asset. It performs the same action as the person equivalent.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /asset/{asset}/persons/associate/{person} [POST]
        api_instance.asset_associate_person(asset, person)
    except Exception as e:
        print("Exception when calling AssetApi->asset_associate_person: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
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

# **asset_associate_tag**
> asset_associate_tag(asset, tag)

/asset/{asset}/tags/associate/{tag} [POST]

Associates a tag with a specified asset. It performs the same action as the tag equivalent.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    tag = 'tag_example' # str | tag id

    try:
        # /asset/{asset}/tags/associate/{tag} [POST]
        api_instance.asset_associate_tag(asset, tag)
    except Exception as e:
        print("Exception when calling AssetApi->asset_associate_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **tag** | **str**| tag id | 

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

# **asset_associate_website**
> asset_associate_website(asset, website)

/asset/{asset}/websites/associate/{website} [POST]

Associates a website with an asset. It performs the same action as its website equivalent.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    website = 'website_example' # str | website id

    try:
        # /asset/{asset}/websites/associate/{website} [POST]
        api_instance.asset_associate_website(asset, website)
    except Exception as e:
        print("Exception when calling AssetApi->asset_associate_website: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
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

# **asset_associate_workstream_summary**
> asset_associate_workstream_summary(asset, workstream_summary)

/asset/{asset}/workstream_summaries/associate/{workstream_summary} [POST]

This will associate a asset with a workstream summary. This will do the same thing as the workstreamSummary equivalent.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /asset/{asset}/workstream_summaries/associate/{workstream_summary} [POST]
        api_instance.asset_associate_workstream_summary(asset, workstream_summary)
    except Exception as e:
        print("Exception when calling AssetApi->asset_associate_workstream_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
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

# **asset_disassociate_anchor**
> asset_disassociate_anchor(asset, anchor)

/asset/{asset}/anchors/disassociate/{anchor} [POST]

Disassociates a anchor from an asset. It performs the same action as the anchor equivalent.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /asset/{asset}/anchors/disassociate/{anchor} [POST]
        api_instance.asset_disassociate_anchor(asset, anchor)
    except Exception as e:
        print("Exception when calling AssetApi->asset_disassociate_anchor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
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

# **asset_disassociate_conversation**
> asset_disassociate_conversation(asset, conversation)

/asset/{asset}/conversations/disassociate/{conversation} [POST]

Disassociates a conversation from an asset. It performs the same action as the conversation equivalent.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    conversation = 'conversation_example' # str | This is the uuid of a conversation.

    try:
        # /asset/{asset}/conversations/disassociate/{conversation} [POST]
        api_instance.asset_disassociate_conversation(asset, conversation)
    except Exception as e:
        print("Exception when calling AssetApi->asset_disassociate_conversation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
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

# **asset_disassociate_hint**
> asset_disassociate_hint(asset, hint)

/asset/{asset}/hints/disassociate/{hint} [POST]

Disassociates an asset from a hint. It performs the same action as the hint equivalent.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    hint = 'hint_example' # str | This is a specific hint uuid

    try:
        # /asset/{asset}/hints/disassociate/{hint} [POST]
        api_instance.asset_disassociate_hint(asset, hint)
    except Exception as e:
        print("Exception when calling AssetApi->asset_disassociate_hint: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **hint** | **str**| This is a specific hint uuid | 

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

# **asset_disassociate_person**
> asset_disassociate_person(asset, person)

/asset/{asset}/persons/disassociate/{person} [POST]

Disassociates a person from an asset. It performs the same action as the person equivalent.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /asset/{asset}/persons/disassociate/{person} [POST]
        api_instance.asset_disassociate_person(asset, person)
    except Exception as e:
        print("Exception when calling AssetApi->asset_disassociate_person: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
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

# **asset_disassociate_tag**
> asset_disassociate_tag(tag, asset)

/asset/{asset}/tags/disassociate/{tag} [POST]

Disassociates a tag from an asset. It performs the same action as the tag equivalent.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    tag = 'tag_example' # str | tag id
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /asset/{asset}/tags/disassociate/{tag} [POST]
        api_instance.asset_disassociate_tag(tag, asset)
    except Exception as e:
        print("Exception when calling AssetApi->asset_disassociate_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| tag id | 
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

# **asset_disassociate_website**
> asset_disassociate_website(website, asset)

/asset/{asset}/websites/disassociate/{website} [POST]

Disassociates a website from an asset. It performs the same action as the website equivalent.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    website = 'website_example' # str | website id
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /asset/{asset}/websites/disassociate/{website} [POST]
        api_instance.asset_disassociate_website(website, asset)
    except Exception as e:
        print("Exception when calling AssetApi->asset_disassociate_website: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
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

# **asset_disassociate_workstream_summary**
> asset_disassociate_workstream_summary(asset, workstream_summary)

/asset/{asset}/workstream_summaries/disassociate/{workstream_summary} [POST]

This will enable us to disassociate an asset from a workstream summary. This will do the same thing as the workstreamSummary equivalent.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /asset/{asset}/workstream_summaries/disassociate/{workstream_summary} [POST]
        api_instance.asset_disassociate_workstream_summary(asset, workstream_summary)
    except Exception as e:
        print("Exception when calling AssetApi->asset_disassociate_workstream_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
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

# **asset_formats**
> Formats asset_formats(asset, transferables=transferables)

/asset/{asset}/formats [GET] Scoped To Asset

Retrieves the formats available for a specified asset.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.formats import Formats
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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /asset/{asset}/formats [GET] Scoped To Asset
        api_response = api_instance.asset_formats(asset, transferables=transferables)
        print("The response of AssetApi->asset_formats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_formats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Formats**](Formats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_reclassify**
> Asset asset_reclassify(transferables=transferables, asset_reclassification=asset_reclassification)

/asset/reclassify [POST]

Retrieves the formats available for a specified asset.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.asset import Asset
from pieces_os_client.models.asset_reclassification import AssetReclassification
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
    api_instance = pieces_os_client.AssetApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    asset_reclassification = pieces_os_client.AssetReclassification() # AssetReclassification | This will accept a Reclassification that includeds and assetand a language that this assets needs to be reclassified to. We will just return an Asset that has been reclassified. (optional)

    try:
        # /asset/reclassify [POST]
        api_response = api_instance.asset_reclassify(transferables=transferables, asset_reclassification=asset_reclassification)
        print("The response of AssetApi->asset_reclassify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_reclassify: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **asset_reclassification** | [**AssetReclassification**](AssetReclassification.md)| This will accept a Reclassification that includeds and assetand a language that this assets needs to be reclassified to. We will just return an Asset that has been reclassified. | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_scores_increment**
> asset_scores_increment(asset, seeded_score_increment=seeded_score_increment)

/asset/{asset}/scores/increment [POST]

Increments the scores associated with the specified asset based on the provided SeededScoreIncrement data in the request body.

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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    seeded_score_increment = pieces_os_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # /asset/{asset}/scores/increment [POST]
        api_instance.asset_scores_increment(asset, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling AssetApi->asset_scores_increment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
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

# **asset_snapshot**
> Asset asset_snapshot(asset, transferables=transferables)

/asset/{asset} [GET] Scoped To Asset

Retrieves the snapshot of a specific asset

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.asset import Asset
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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /asset/{asset} [GET] Scoped To Asset
        api_response = api_instance.asset_snapshot(asset, transferables=transferables)
        print("The response of AssetApi->asset_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**410** | Asset no longer exists and is Gone. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_snapshot_post**
> Asset asset_snapshot_post(asset, transferables=transferables, seeded_accessor=seeded_accessor)

/asset/{asset} [POST] Scoped to an Asset

Retrieves a snapshot of a specific asset, along with the user requesting the snapshot.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.asset import Asset
from pieces_os_client.models.seeded_accessor import SeededAccessor
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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    seeded_accessor = pieces_os_client.SeededAccessor() # SeededAccessor |  (optional)

    try:
        # /asset/{asset} [POST] Scoped to an Asset
        api_response = api_instance.asset_snapshot_post(asset, transferables=transferables, seeded_accessor=seeded_accessor)
        print("The response of AssetApi->asset_snapshot_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_snapshot_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **seeded_accessor** | [**SeededAccessor**](SeededAccessor.md)|  | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_specific_asset_activities**
> Activities asset_specific_asset_activities(asset, transferables=transferables)

/asset/{asset}/activities [GET]

Retrieves activity events specific to the given asset.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.activities import Activities
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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /asset/{asset}/activities [GET]
        api_response = api_instance.asset_specific_asset_activities(asset, transferables=transferables)
        print("The response of AssetApi->asset_specific_asset_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_specific_asset_activities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Activities**](Activities.md)

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

# **asset_specific_asset_conversations**
> Conversations asset_specific_asset_conversations(asset, transferables=transferables)

/asset/{asset}/conversations [GET]

Retrieves conversations specific to the given asset.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.conversations import Conversations
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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /asset/{asset}/conversations [GET]
        api_response = api_instance.asset_specific_asset_conversations(asset, transferables=transferables)
        print("The response of AssetApi->asset_specific_asset_conversations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_specific_asset_conversations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Conversations**](Conversations.md)

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

# **asset_specific_asset_export**
> ExportedAsset asset_specific_asset_export(asset, export_type)

/asset/{asset}/export [GET]

Retrieves an export version of the specified asset.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.exported_asset import ExportedAsset
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
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    export_type = 'export_type_example' # str | This specifies the type of export the user wants.

    try:
        # /asset/{asset}/export [GET]
        api_response = api_instance.asset_specific_asset_export(asset, export_type)
        print("The response of AssetApi->asset_specific_asset_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_specific_asset_export: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **export_type** | **str**| This specifies the type of export the user wants. | 

### Return type

[**ExportedAsset**](ExportedAsset.md)

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

# **asset_update**
> Asset asset_update(transferables=transferables, asset=asset)

/asset/update [POST] Scoped to Asset

Allows the user to update an existing Asset. It accepts the Asset object that needs updating and returns the fully updated Asset.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.asset import Asset
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
    api_instance = pieces_os_client.AssetApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    asset = pieces_os_client.Asset() # Asset | This endpoint allows the user to update an existing Asset. It accepts the Asset object that needs updating and returns the fully updated Asset. (optional)

    try:
        # /asset/update [POST] Scoped to Asset
        api_response = api_instance.asset_update(transferables=transferables, asset=asset)
        print("The response of AssetApi->asset_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **asset** | [**Asset**](Asset.md)| This endpoint allows the user to update an existing Asset. It accepts the Asset object that needs updating and returns the fully updated Asset. | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

