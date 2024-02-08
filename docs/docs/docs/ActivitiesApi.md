# openapi_client.ActivitiesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activities_create_new_activity**](ActivitiesApi.md#activities_create_new_activity) | **POST** /activities/create | /activities/create [POST]
[**activities_delete_specific_activity**](ActivitiesApi.md#activities_delete_specific_activity) | **POST** /activities/{activity}/delete | /activities/{activity}/delete [POST]
[**activities_snapshot**](ActivitiesApi.md#activities_snapshot) | **GET** /activities | /activities [GET]


# **activities_create_new_activity**
> Activity activities_create_new_activity(transferables=transferables, seeded_activity=seeded_activity)

/activities/create [POST]

This will create a new Activity.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.activity import Activity
from openapi_client.models.seeded_activity import SeededActivity
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
    api_instance = openapi_client.ActivitiesApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    seeded_activity = openapi_client.SeededActivity() # SeededActivity |  (optional)

    try:
        # /activities/create [POST]
        api_response = api_instance.activities_create_new_activity(transferables=transferables, seeded_activity=seeded_activity)
        print("The response of ActivitiesApi->activities_create_new_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->activities_create_new_activity: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **seeded_activity** | [**SeededActivity**](SeededActivity.md)|  | [optional] 

### Return type

[**Activity**](Activity.md)

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

# **activities_delete_specific_activity**
> activities_delete_specific_activity(activity)

/activities/{activity}/delete [POST]

This will delete a specific activity.  important note: if we delete an activity: that is going to be a generic or a specific/ we will also delete its counter part i.e the specific. and vise versa, this ensures that the references are always cleaned.

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
    api_instance = openapi_client.ActivitiesApi(api_client)
    activity = 'activity_example' # str | This is a specific activity uuid.

    try:
        # /activities/{activity}/delete [POST]
        api_instance.activities_delete_specific_activity(activity)
    except Exception as e:
        print("Exception when calling ActivitiesApi->activities_delete_specific_activity: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity** | **str**| This is a specific activity uuid. | 

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

# **activities_snapshot**
> Activities activities_snapshot(transferables=transferables, pseudo=pseudo)

/activities [GET]

This will get a snapshot of all of the activities

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.activities import Activities
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
    api_instance = openapi_client.ActivitiesApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    pseudo = True # bool | This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false. (optional)

    try:
        # /activities [GET]
        api_response = api_instance.activities_snapshot(transferables=transferables, pseudo=pseudo)
        print("The response of ActivitiesApi->activities_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivitiesApi->activities_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **pseudo** | **bool**| This is helper boolean that will give you the ability to also include your pseudo assets, we will always default to false. | [optional] 

### Return type

[**Activities**](Activities.md)

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

