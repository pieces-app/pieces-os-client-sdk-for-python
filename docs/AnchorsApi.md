# pieces_os_client.AnchorsApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anchors_create_new_anchor**](AnchorsApi.md#anchors_create_new_anchor) | **POST** /anchors/create | /anchors/create [POST]
[**anchors_delete_specific_anchor**](AnchorsApi.md#anchors_delete_specific_anchor) | **POST** /anchors/{anchor}/delete | /anchors/{anchor}/delete [POST]
[**anchors_snapshot**](AnchorsApi.md#anchors_snapshot) | **GET** /anchors | /anchors [GET]
[**anchors_stream_identifiers**](AnchorsApi.md#anchors_stream_identifiers) | **GET** /anchors/stream/identifiers | /anchors/stream/identifiers [WS]
[**search_anchors**](AnchorsApi.md#search_anchors) | **POST** /anchors/search | /anchors/search [POST]


# **anchors_create_new_anchor**
> Anchor anchors_create_new_anchor(transferables=transferables, seeded_anchor=seeded_anchor)

/anchors/create [POST]

This will create a anchor and attach it to a specific asset(s) This will also ensure the anchor is normalized.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.anchor import Anchor
from pieces_os_client.models.seeded_anchor import SeededAnchor
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
    api_instance = pieces_os_client.AnchorsApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    seeded_anchor = pieces_os_client.SeededAnchor() # SeededAnchor |  (optional)

    try:
        # /anchors/create [POST]
        api_response = api_instance.anchors_create_new_anchor(transferables=transferables, seeded_anchor=seeded_anchor)
        print("The response of AnchorsApi->anchors_create_new_anchor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorsApi->anchors_create_new_anchor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **seeded_anchor** | [**SeededAnchor**](SeededAnchor.md)|  | [optional] 

### Return type

[**Anchor**](Anchor.md)

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

# **anchors_delete_specific_anchor**
> anchors_delete_specific_anchor(anchor)

/anchors/{anchor}/delete [POST]

This will delete a specific anchor!

### Example

* Api Key Authentication (application):

```python
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
    api_instance = pieces_os_client.AnchorsApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.

    try:
        # /anchors/{anchor}/delete [POST]
        api_instance.anchors_delete_specific_anchor(anchor)
    except Exception as e:
        print("Exception when calling AnchorsApi->anchors_delete_specific_anchor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **anchors_snapshot**
> Anchors anchors_snapshot(transferables=transferables)

/anchors [GET]

This will get a snapshot of all your anchors.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.anchors import Anchors
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
    api_instance = pieces_os_client.AnchorsApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /anchors [GET]
        api_response = api_instance.anchors_snapshot(transferables=transferables)
        print("The response of AnchorsApi->anchors_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorsApi->anchors_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Anchors**](Anchors.md)

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

# **anchors_stream_identifiers**
> StreamedIdentifiers anchors_stream_identifiers()

/anchors/stream/identifiers [WS]

Provides a WebSocket connection that emits changes to your anchor identifiers (UUIDs).

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.streamed_identifiers import StreamedIdentifiers
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
    api_instance = pieces_os_client.AnchorsApi(api_client)

    try:
        # /anchors/stream/identifiers [WS]
        api_response = api_instance.anchors_stream_identifiers()
        print("The response of AnchorsApi->anchors_stream_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorsApi->anchors_stream_identifiers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StreamedIdentifiers**](StreamedIdentifiers.md)

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

# **search_anchors**
> SearchedAnchors search_anchors(transferables=transferables, search_input=search_input)

/anchors/search [POST]

This will search your anchors for a specific anchor

note: we will search all the anchor points

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.search_input import SearchInput
from pieces_os_client.models.searched_anchors import SearchedAnchors
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
    api_instance = pieces_os_client.AnchorsApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    search_input = pieces_os_client.SearchInput() # SearchInput |  (optional)

    try:
        # /anchors/search [POST]
        api_response = api_instance.search_anchors(transferables=transferables, search_input=search_input)
        print("The response of AnchorsApi->search_anchors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorsApi->search_anchors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **search_input** | [**SearchInput**](SearchInput.md)|  | [optional] 

### Return type

[**SearchedAnchors**](SearchedAnchors.md)

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

