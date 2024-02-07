# openapi_client.AnchorPointsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anchor_points_create_new_anchor_point**](AnchorPointsApi.md#anchor_points_create_new_anchor_point) | **POST** /anchor_points/create | /anchor_points/create [POST]
[**anchor_points_delete_specific_anchor_point**](AnchorPointsApi.md#anchor_points_delete_specific_anchor_point) | **POST** /anchor_points/{anchor_point}/delete | /anchor_points/{anchor_point}/delete [POST]
[**anchor_points_snapshot**](AnchorPointsApi.md#anchor_points_snapshot) | **GET** /anchor_points | /anchor_points [GET]


# **anchor_points_create_new_anchor_point**
> AnchorPoint anchor_points_create_new_anchor_point(transferables=transferables, seeded_anchor_point=seeded_anchor_point)

/anchor_points/create [POST]

This will create a anchorPoint.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.anchor_point import AnchorPoint
from openapi_client.models.seeded_anchor_point import SeededAnchorPoint
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
    api_instance = openapi_client.AnchorPointsApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    seeded_anchor_point = openapi_client.SeededAnchorPoint() # SeededAnchorPoint |  (optional)

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

# **anchor_points_delete_specific_anchor_point**
> anchor_points_delete_specific_anchor_point(anchor_point)

/anchor_points/{anchor_point}/delete [POST]

This will delete a specific anchorPoint!

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
    api_instance = openapi_client.AnchorPointsApi(api_client)
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

# **anchor_points_snapshot**
> AnchorPoints anchor_points_snapshot(transferables=transferables)

/anchor_points [GET]

This will get a snapshot of all your anchorPoints.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.anchor_points import AnchorPoints
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
    api_instance = openapi_client.AnchorPointsApi(api_client)
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

