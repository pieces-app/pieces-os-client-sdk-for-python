# pieces_os_client.WorkstreamEventsApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workstream_events_create_new_workstream_event**](WorkstreamEventsApi.md#workstream_events_create_new_workstream_event) | **POST** /workstream_events/create | /workstream_events/create [POST]
[**workstream_events_delete_specific_workstream_event**](WorkstreamEventsApi.md#workstream_events_delete_specific_workstream_event) | **POST** /workstream_events/{workstream_event}/delete | /workstream_events/{workstream_event}/delete [POST]
[**workstream_events_snapshot**](WorkstreamEventsApi.md#workstream_events_snapshot) | **GET** /workstream_events | /workstream_events [GET]


# **workstream_events_create_new_workstream_event**
> WorkstreamEvent workstream_events_create_new_workstream_event(transferables=transferables, seeded_workstream_event=seeded_workstream_event)

/workstream_events/create [POST]

This will create a new WorkstreamEvent in the database.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.seeded_workstream_event import SeededWorkstreamEvent
from pieces_os_client.models.workstream_event import WorkstreamEvent
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
    api_instance = pieces_os_client.WorkstreamEventsApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    seeded_workstream_event = pieces_os_client.SeededWorkstreamEvent() # SeededWorkstreamEvent |  (optional)

    try:
        # /workstream_events/create [POST]
        api_response = api_instance.workstream_events_create_new_workstream_event(transferables=transferables, seeded_workstream_event=seeded_workstream_event)
        print("The response of WorkstreamEventsApi->workstream_events_create_new_workstream_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamEventsApi->workstream_events_create_new_workstream_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **seeded_workstream_event** | [**SeededWorkstreamEvent**](SeededWorkstreamEvent.md)|  | [optional] 

### Return type

[**WorkstreamEvent**](WorkstreamEvent.md)

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

# **workstream_events_delete_specific_workstream_event**
> workstream_events_delete_specific_workstream_event(workstream_event)

/workstream_events/{workstream_event}/delete [POST]

This will delete a specific workstream_event from the database!

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
    api_instance = pieces_os_client.WorkstreamEventsApi(api_client)
    workstream_event = 'workstream_event_example' # str | This is a identifier that is used to identify a specific workstream_event.

    try:
        # /workstream_events/{workstream_event}/delete [POST]
        api_instance.workstream_events_delete_specific_workstream_event(workstream_event)
    except Exception as e:
        print("Exception when calling WorkstreamEventsApi->workstream_events_delete_specific_workstream_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_event** | **str**| This is a identifier that is used to identify a specific workstream_event. | 

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

# **workstream_events_snapshot**
> WorkstreamEvents workstream_events_snapshot(transferables=transferables)

/workstream_events [GET]

This will get a snapshot of all your workstream events.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_events import WorkstreamEvents
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
    api_instance = pieces_os_client.WorkstreamEventsApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /workstream_events [GET]
        api_response = api_instance.workstream_events_snapshot(transferables=transferables)
        print("The response of WorkstreamEventsApi->workstream_events_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamEventsApi->workstream_events_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**WorkstreamEvents**](WorkstreamEvents.md)

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

