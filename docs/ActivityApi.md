# pieces_os_client.ActivityApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activities_specific_activity_snapshot**](ActivityApi.md#activities_specific_activity_snapshot) | **GET** /activity/{activity} | /activity/{activity} [GET]
[**activity_identifiers_snapshot**](ActivityApi.md#activity_identifiers_snapshot) | **GET** /activity/identifiers | /activity/identifiers [GET]
[**activity_update**](ActivityApi.md#activity_update) | **POST** /activity/update | /activity/update [POST]


# **activities_specific_activity_snapshot**
> Activity activities_specific_activity_snapshot(activity, transferables=transferables)

/activity/{activity} [GET]

This will attempt to get a specific activity.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.activity import Activity
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
    api_instance = pieces_os_client.ActivityApi(api_client)
    activity = 'activity_example' # str | This is a specific activity uuid.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /activity/{activity} [GET]
        api_response = api_instance.activities_specific_activity_snapshot(activity, transferables=transferables)
        print("The response of ActivityApi->activities_specific_activity_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activities_specific_activity_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity** | **str**| This is a specific activity uuid. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Activity**](Activity.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**410** | Activity was not found. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_identifiers_snapshot**
> FlattenedActivities activity_identifiers_snapshot(pseudo=pseudo, activity_filter_enum=activity_filter_enum)

/activity/identifiers [GET]

This is going to return all the identifiers of the activity event in order of most recent -> oldest.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.flattened_activities import FlattenedActivities
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
    api_instance = pieces_os_client.ActivityApi(api_client)
    pseudo = True # bool | This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false. (optional)
    activity_filter_enum = 'UNKNOWN' # str | This is an ActivityFilterEnum as a optional filter. Ensure you update ActivityFilterEnum if this is updated. (optional) (default to 'UNKNOWN')

    try:
        # /activity/identifiers [GET]
        api_response = api_instance.activity_identifiers_snapshot(pseudo=pseudo, activity_filter_enum=activity_filter_enum)
        print("The response of ActivityApi->activity_identifiers_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_identifiers_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pseudo** | **bool**| This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false. | [optional] 
 **activity_filter_enum** | **str**| This is an ActivityFilterEnum as a optional filter. Ensure you update ActivityFilterEnum if this is updated. | [optional] [default to &#39;UNKNOWN&#39;]

### Return type

[**FlattenedActivities**](FlattenedActivities.md)

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

# **activity_update**
> Activity activity_update(transferables=transferables, activity=activity)

/activity/update [POST]

this will update a specific activity.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.activity import Activity
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
    api_instance = pieces_os_client.ActivityApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    activity = pieces_os_client.Activity() # Activity |  (optional)

    try:
        # /activity/update [POST]
        api_response = api_instance.activity_update(transferables=transferables, activity=activity)
        print("The response of ActivityApi->activity_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **activity** | [**Activity**](Activity.md)|  | [optional] 

### Return type

[**Activity**](Activity.md)

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

