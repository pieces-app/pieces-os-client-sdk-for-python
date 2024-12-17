# pieces_os_client.PersonApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**person_associate_anchor**](PersonApi.md#person_associate_anchor) | **POST** /person/{person}/anchors/associate/{anchor} | /person/{person}/anchors/associate/{anchor} [POST]
[**person_associate_asset**](PersonApi.md#person_associate_asset) | **POST** /person/{person}/assets/associate/{asset} | /person/{person}/assets/associate/{asset} [POST]
[**person_associate_message**](PersonApi.md#person_associate_message) | **POST** /person/{person}/messages/associate/{message} | /person/{person}/messages/associate/{message} [POST]
[**person_associate_tag**](PersonApi.md#person_associate_tag) | **POST** /person/{person}/tags/associate/{tag} | /person/{person}/tags/associate/{tag} [POST]
[**person_associate_website**](PersonApi.md#person_associate_website) | **POST** /person/{person}/websites/associate/{website} | /person/{person}/websites/associate/{website} [POST]
[**person_associate_workstream_summary**](PersonApi.md#person_associate_workstream_summary) | **POST** /person/{person}/workstream_summaries/associate/{workstream_summary} | /person/{person}/workstream_summaries/associate/{workstream_summary} [POST]
[**person_disassociate_anchor**](PersonApi.md#person_disassociate_anchor) | **POST** /person/{person}/anchors/disassociate/{anchor} | /person/{person}/anchors/disassociate/{anchor} [POST]
[**person_disassociate_asset**](PersonApi.md#person_disassociate_asset) | **POST** /person/{person}/assets/disassociate/{asset} | /person/{person}/assets/disassociate/{asset} [POST]
[**person_disassociate_message**](PersonApi.md#person_disassociate_message) | **POST** /person/{person}/messages/disassociate/{message} | /person/{person}/messages/disassociate/{message} [POST]
[**person_disassociate_tag**](PersonApi.md#person_disassociate_tag) | **POST** /person/{person}/tags/disassociate/{tag} | /person/{person}/tags/disassociate/{tag} [POST]
[**person_disassociate_website**](PersonApi.md#person_disassociate_website) | **POST** /person/{person}/websites/disassociate/{website} | /person/{person}/websites/disassociate/{website} [POST]
[**person_disassociate_workstream_summary**](PersonApi.md#person_disassociate_workstream_summary) | **POST** /person/{person}/workstream_summaries/disassociate/{workstream_summary} | /person/{person}/workstream_summaries/disassociate/{workstream_summary} [POST]
[**person_scores_increment**](PersonApi.md#person_scores_increment) | **POST** /person/{person}/scores/increment | &#39;/person/{person}/scores/increment&#39; [POST]
[**person_snapshot**](PersonApi.md#person_snapshot) | **GET** /person/{person} | /person/{person} [GET]
[**update_person**](PersonApi.md#update_person) | **POST** /person/update | /person/update [POST]


# **person_associate_anchor**
> person_associate_anchor(person, anchor)

/person/{person}/anchors/associate/{anchor} [POST]

associates a person and an anchor. It performs the same action as the anchor equivalent.

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
    api_instance = pieces_os_client.PersonApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /person/{person}/anchors/associate/{anchor} [POST]
        api_instance.person_associate_anchor(person, anchor)
    except Exception as e:
        print("Exception when calling PersonApi->person_associate_anchor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 
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

# **person_associate_asset**
> person_associate_asset(person, asset)

/person/{person}/assets/associate/{asset} [POST]

associates a person and an asset. It performs the same action as the asset equivalent.

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
    api_instance = pieces_os_client.PersonApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /person/{person}/assets/associate/{asset} [POST]
        api_instance.person_associate_asset(person, asset)
    except Exception as e:
        print("Exception when calling PersonApi->person_associate_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 
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

# **person_associate_message**
> person_associate_message(person, message)

/person/{person}/messages/associate/{message} [POST]

This will associate a person with a message.

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
    api_instance = pieces_os_client.PersonApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.
    message = 'message_example' # str | This is the uuid of a message.

    try:
        # /person/{person}/messages/associate/{message} [POST]
        api_instance.person_associate_message(person, message)
    except Exception as e:
        print("Exception when calling PersonApi->person_associate_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 
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

# **person_associate_tag**
> person_associate_tag(person, tag)

/person/{person}/tags/associate/{tag} [POST]

associates a tag and a person. It performs the same action as the tag equivalent.

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
    api_instance = pieces_os_client.PersonApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.
    tag = 'tag_example' # str | tag id

    try:
        # /person/{person}/tags/associate/{tag} [POST]
        api_instance.person_associate_tag(person, tag)
    except Exception as e:
        print("Exception when calling PersonApi->person_associate_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 
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

# **person_associate_website**
> person_associate_website(person, website)

/person/{person}/websites/associate/{website} [POST]

associates a website and a person. It performs the same action as the website equivalent.

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
    api_instance = pieces_os_client.PersonApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.
    website = 'website_example' # str | website id

    try:
        # /person/{person}/websites/associate/{website} [POST]
        api_instance.person_associate_website(person, website)
    except Exception as e:
        print("Exception when calling PersonApi->person_associate_website: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 
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

# **person_associate_workstream_summary**
> person_associate_workstream_summary(person, workstream_summary)

/person/{person}/workstream_summaries/associate/{workstream_summary} [POST]

This will associate a person with a workstream summary. This will do the same thing as the workstreamSummary equivalent.

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
    api_instance = pieces_os_client.PersonApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /person/{person}/workstream_summaries/associate/{workstream_summary} [POST]
        api_instance.person_associate_workstream_summary(person, workstream_summary)
    except Exception as e:
        print("Exception when calling PersonApi->person_associate_workstream_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 
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

# **person_disassociate_anchor**
> person_disassociate_anchor(person, anchor)

/person/{person}/anchors/disassociate/{anchor} [POST]

Disassociates a person from an achor. It performs the same action as the anchor equivalent.

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
    api_instance = pieces_os_client.PersonApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /person/{person}/anchors/disassociate/{anchor} [POST]
        api_instance.person_disassociate_anchor(person, anchor)
    except Exception as e:
        print("Exception when calling PersonApi->person_disassociate_anchor: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 
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

# **person_disassociate_asset**
> person_disassociate_asset(person, asset)

/person/{person}/assets/disassociate/{asset} [POST]

Disassociates a person from an asset. It performs the same action as the asset equivalent.

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
    api_instance = pieces_os_client.PersonApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /person/{person}/assets/disassociate/{asset} [POST]
        api_instance.person_disassociate_asset(person, asset)
    except Exception as e:
        print("Exception when calling PersonApi->person_disassociate_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 
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

# **person_disassociate_message**
> person_disassociate_message(person, message)

/person/{person}/messages/disassociate/{message} [POST]

This will enable us to disassociate a person from a message.

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
    api_instance = pieces_os_client.PersonApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.
    message = 'message_example' # str | This is the uuid of a message.

    try:
        # /person/{person}/messages/disassociate/{message} [POST]
        api_instance.person_disassociate_message(person, message)
    except Exception as e:
        print("Exception when calling PersonApi->person_disassociate_message: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 
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

# **person_disassociate_tag**
> person_disassociate_tag(person, tag)

/person/{person}/tags/disassociate/{tag} [POST]

Disassociates a person from a tag. It performs the same action as the tag equivalent.

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
    api_instance = pieces_os_client.PersonApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.
    tag = 'tag_example' # str | tag id

    try:
        # /person/{person}/tags/disassociate/{tag} [POST]
        api_instance.person_disassociate_tag(person, tag)
    except Exception as e:
        print("Exception when calling PersonApi->person_disassociate_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 
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

# **person_disassociate_website**
> person_disassociate_website(person, website)

/person/{person}/websites/disassociate/{website} [POST]

Disassociates a person from a website. It performs the same action as the website equivalent.

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
    api_instance = pieces_os_client.PersonApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.
    website = 'website_example' # str | website id

    try:
        # /person/{person}/websites/disassociate/{website} [POST]
        api_instance.person_disassociate_website(person, website)
    except Exception as e:
        print("Exception when calling PersonApi->person_disassociate_website: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 
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

# **person_disassociate_workstream_summary**
> person_disassociate_workstream_summary(person, workstream_summary)

/person/{person}/workstream_summaries/disassociate/{workstream_summary} [POST]

This will enable us to disassociate an person from a workstream summary. This will do the same thing as the workstreamSummary equivalent.

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
    api_instance = pieces_os_client.PersonApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /person/{person}/workstream_summaries/disassociate/{workstream_summary} [POST]
        api_instance.person_disassociate_workstream_summary(person, workstream_summary)
    except Exception as e:
        print("Exception when calling PersonApi->person_disassociate_workstream_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 
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

# **person_scores_increment**
> person_scores_increment(person, seeded_score_increment=seeded_score_increment)

'/person/{person}/scores/increment' [POST]

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
    api_instance = pieces_os_client.PersonApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.
    seeded_score_increment = pieces_os_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # '/person/{person}/scores/increment' [POST]
        api_instance.person_scores_increment(person, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling PersonApi->person_scores_increment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 
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

# **person_snapshot**
> Person person_snapshot(person, transferables=transferables)

/person/{person} [GET]

This will get a snapshot of a specific person

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.person import Person
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
    api_instance = pieces_os_client.PersonApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /person/{person} [GET]
        api_response = api_instance.person_snapshot(person, transferables=transferables)
        print("The response of PersonApi->person_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonApi->person_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Person**](Person.md)

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

# **update_person**
> Person update_person(transferables=transferables, person=person)

/person/update [POST]

This will update a specific person

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.person import Person
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
    api_instance = pieces_os_client.PersonApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    person = pieces_os_client.Person() # Person |  (optional)

    try:
        # /person/update [POST]
        api_response = api_instance.update_person(transferables=transferables, person=person)
        print("The response of PersonApi->update_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonApi->update_person: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **person** | [**Person**](Person.md)|  | [optional] 

### Return type

[**Person**](Person.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

