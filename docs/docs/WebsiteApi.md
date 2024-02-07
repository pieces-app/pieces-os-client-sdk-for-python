# openapi_client.WebsiteApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**website_associate_asset**](WebsiteApi.md#website_associate_asset) | **POST** /website/{website}/assets/associate/{asset} | /website/{website}/assets/associate/{asset} [POST]
[**website_associate_conversation**](WebsiteApi.md#website_associate_conversation) | **POST** /website/{website}/conversations/associate/{conversation} | /website/{website}/conversations/associate/{conversation} [POST]
[**website_associate_person**](WebsiteApi.md#website_associate_person) | **POST** /website/{website}/persons/associate/{person} | /website/{website}/persons/associate/{person} [POST]
[**website_disassociate_asset**](WebsiteApi.md#website_disassociate_asset) | **POST** /website/{website}/assets/disassociate/{asset} | /website/{website}/assets/disassociate/{asset} [POST]
[**website_disassociate_conversation**](WebsiteApi.md#website_disassociate_conversation) | **POST** /website/{website}/conversations/disassociate/{conversation} | /website/{website}/conversations/disassociate/{conversation} [POST]
[**website_disassociate_person**](WebsiteApi.md#website_disassociate_person) | **POST** /website/{website}/persons/disassociate/{person} | /website/{website}/persons/disassociate/{person} [POST]
[**website_scores_increment**](WebsiteApi.md#website_scores_increment) | **POST** /website/{website}/scores/increment | &#39;/website/{website}/scores/increment&#39; [POST]
[**website_update**](WebsiteApi.md#website_update) | **POST** /website/update | /website/update [POST]
[**websites_specific_website_snapshot**](WebsiteApi.md#websites_specific_website_snapshot) | **GET** /website/{website} | /website/{website} [GET]


# **website_associate_asset**
> website_associate_asset(asset, website)

/website/{website}/assets/associate/{asset} [POST]

This will associate a website with a asset.

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
    api_instance = openapi_client.WebsiteApi(api_client)
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

# **website_associate_conversation**
> website_associate_conversation(website, conversation)

/website/{website}/conversations/associate/{conversation} [POST]

This will associate a website with a conversation.

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
    api_instance = openapi_client.WebsiteApi(api_client)
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

# **website_associate_person**
> website_associate_person(website, person)

/website/{website}/persons/associate/{person} [POST]

This will associate a website with a person.

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
    api_instance = openapi_client.WebsiteApi(api_client)
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

# **website_disassociate_asset**
> website_disassociate_asset(website, asset)

/website/{website}/assets/disassociate/{asset} [POST]

This will enable us to dissassociate a website from a asset.

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
    api_instance = openapi_client.WebsiteApi(api_client)
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

# **website_disassociate_conversation**
> website_disassociate_conversation(website, conversation)

/website/{website}/conversations/disassociate/{conversation} [POST]

This will enable us to dissassociate a website from a conversation.

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
    api_instance = openapi_client.WebsiteApi(api_client)
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

# **website_disassociate_person**
> website_disassociate_person(website, person)

/website/{website}/persons/disassociate/{person} [POST]

This will enable us to dissassociate a website from a person.

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
    api_instance = openapi_client.WebsiteApi(api_client)
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

# **website_scores_increment**
> website_scores_increment(website, seeded_score_increment=seeded_score_increment)

'/website/{website}/scores/increment' [POST]

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
    api_instance = openapi_client.WebsiteApi(api_client)
    website = 'website_example' # str | website id
    seeded_score_increment = openapi_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

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

# **website_update**
> Website website_update(transferables=transferables, website=website)

/website/update [POST]

This will update a specific website.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.website import Website
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
    api_instance = openapi_client.WebsiteApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    website = openapi_client.Website() # Website |  (optional)

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

# **websites_specific_website_snapshot**
> Website websites_specific_website_snapshot(website, transferables=transferables)

/website/{website} [GET]

This will get a snapshot of a single website.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.website import Website
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
    api_instance = openapi_client.WebsiteApi(api_client)
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

