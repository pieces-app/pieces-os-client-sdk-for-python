# pieces_os_client.AnchorPointApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anchor_point_scores_increment**](AnchorPointApi.md#anchor_point_scores_increment) | **POST** /anchor_point/{anchor_point}/scores/increment | &#39;/anchor_point/{anchor_point}/scores/increment&#39; [POST]
[**anchor_point_specific_anchor_point_snapshot**](AnchorPointApi.md#anchor_point_specific_anchor_point_snapshot) | **GET** /anchor_point/{anchor_point} | /anchor_point/{anchor_point} [GET]
[**anchor_point_update**](AnchorPointApi.md#anchor_point_update) | **POST** /anchor_point/update | /anchor_point/update [POST]


# **anchor_point_scores_increment**
> anchor_point_scores_increment(anchor_point, seeded_score_increment=seeded_score_increment)

'/anchor_point/{anchor_point}/scores/increment' [POST]

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
    api_instance = pieces_os_client.AnchorPointApi(api_client)
    anchor_point = 'anchor_point_example' # str | This is the specific uuid of an anchor_point.
    seeded_score_increment = pieces_os_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # '/anchor_point/{anchor_point}/scores/increment' [POST]
        api_instance.anchor_point_scores_increment(anchor_point, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling AnchorPointApi->anchor_point_scores_increment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor_point** | **str**| This is the specific uuid of an anchor_point. | 
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

# **anchor_point_specific_anchor_point_snapshot**
> AnchorPoint anchor_point_specific_anchor_point_snapshot(anchor_point, transferables=transferables)

/anchor_point/{anchor_point} [GET]

This will get a snapshot of a single anchorPoint.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.anchor_point import AnchorPoint
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
    api_instance = pieces_os_client.AnchorPointApi(api_client)
    anchor_point = 'anchor_point_example' # str | This is the specific uuid of an anchor_point.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /anchor_point/{anchor_point} [GET]
        api_response = api_instance.anchor_point_specific_anchor_point_snapshot(anchor_point, transferables=transferables)
        print("The response of AnchorPointApi->anchor_point_specific_anchor_point_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorPointApi->anchor_point_specific_anchor_point_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor_point** | **str**| This is the specific uuid of an anchor_point. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**AnchorPoint**](AnchorPoint.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**410** | AnchorPoint not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **anchor_point_update**
> AnchorPoint anchor_point_update(transferables=transferables, anchor_point=anchor_point)

/anchor_point/update [POST]

This will update a specific anchorPoint.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.anchor_point import AnchorPoint
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
    api_instance = pieces_os_client.AnchorPointApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    anchor_point = pieces_os_client.AnchorPoint() # AnchorPoint |  (optional)

    try:
        # /anchor_point/update [POST]
        api_response = api_instance.anchor_point_update(transferables=transferables, anchor_point=anchor_point)
        print("The response of AnchorPointApi->anchor_point_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorPointApi->anchor_point_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **anchor_point** | [**AnchorPoint**](AnchorPoint.md)|  | [optional] 

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

