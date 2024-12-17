# pieces_os_client.AnchorPointsApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anchor_points_create_new_anchor_point**](AnchorPointsApi.md#anchor_points_create_new_anchor_point) | **POST** /anchor_points/create | /anchor_points/create [POST]
[**anchor_points_delete_specific_anchor_point**](AnchorPointsApi.md#anchor_points_delete_specific_anchor_point) | **POST** /anchor_points/{anchor_point}/delete | /anchor_points/{anchor_point}/delete [POST]
[**anchor_points_snapshot**](AnchorPointsApi.md#anchor_points_snapshot) | **GET** /anchor_points | /anchor_points [GET]
[**anchor_points_stream_identifiers**](AnchorPointsApi.md#anchor_points_stream_identifiers) | **GET** /anchor_points/stream/identifiers | /anchor_points/stream/identifiers [WS]


# **anchor_points_create_new_anchor_point**
> AnchorPoint anchor_points_create_new_anchor_point(transferables=transferables, seeded_anchor_point=seeded_anchor_point)

/anchor_points/create [POST]

This will create a anchorPoint.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.anchor_point import AnchorPoint
from pieces_os_client.models.seeded_anchor_point import SeededAnchorPoint
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
    api_instance = pieces_os_client.AnchorPointsApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    seeded_anchor_point = pieces_os_client.SeededAnchorPoint() # SeededAnchorPoint |  (optional)

    try:
        # /anchor_points/create [POST]
        api_response = api_instance.anchor_points_create_new_anchor_point(transferables=transferables, seeded_anchor_point=seeded_anchor_point)
        print("The response of AnchorPointsApi->anchor_points_create_new_anchor_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorPointsApi->anchor_points_create_new_anchor_point: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **seeded_anchor_point** | [**SeededAnchorPoint**](SeededAnchorPoint.md)|  | [optional] 

### Return type

[**AnchorPoint**](AnchorPoint.md)

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

# **anchor_points_delete_specific_anchor_point**
> anchor_points_delete_specific_anchor_point(anchor_point)

/anchor_points/{anchor_point}/delete [POST]

This will delete a specific anchorPoint!

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
    api_instance = pieces_os_client.AnchorPointsApi(api_client)
    anchor_point = 'anchor_point_example' # str | This is the specific uuid of an anchor_point.

    try:
        # /anchor_points/{anchor_point}/delete [POST]
        api_instance.anchor_points_delete_specific_anchor_point(anchor_point)
    except Exception as e:
        print("Exception when calling AnchorPointsApi->anchor_points_delete_specific_anchor_point: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor_point** | **str**| This is the specific uuid of an anchor_point. | 

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

# **anchor_points_snapshot**
> AnchorPoints anchor_points_snapshot(transferables=transferables)

/anchor_points [GET]

This will get a snapshot of all your anchorPoints.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.anchor_points import AnchorPoints
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
    api_instance = pieces_os_client.AnchorPointsApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /anchor_points [GET]
        api_response = api_instance.anchor_points_snapshot(transferables=transferables)
        print("The response of AnchorPointsApi->anchor_points_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorPointsApi->anchor_points_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**AnchorPoints**](AnchorPoints.md)

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

# **anchor_points_stream_identifiers**
> StreamedIdentifiers anchor_points_stream_identifiers()

/anchor_points/stream/identifiers [WS]

Provides a WebSocket connection that emits changes to your annotation identifiers (UUIDs).

### Example

* Api Key Authentication (application):
```python
import time
import os
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
    api_instance = pieces_os_client.AnchorPointsApi(api_client)

    try:
        # /anchor_points/stream/identifiers [WS]
        api_response = api_instance.anchor_points_stream_identifiers()
        print("The response of AnchorPointsApi->anchor_points_stream_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorPointsApi->anchor_points_stream_identifiers: %s\n" % e)
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

