# pieces_os_client.WorkstreamEventsApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workstream_events_batch**](WorkstreamEventsApi.md#workstream_events_batch) | **POST** /workstream_events/batch/fetch | /workstream_events/batch/fetch [POST]
[**workstream_events_create_new_workstream_event**](WorkstreamEventsApi.md#workstream_events_create_new_workstream_event) | **POST** /workstream_events/create | /workstream_events/create [POST]
[**workstream_events_delete_specific_workstream_event**](WorkstreamEventsApi.md#workstream_events_delete_specific_workstream_event) | **POST** /workstream_events/{workstream_event}/delete | /workstream_events/{workstream_event}/delete [POST]
[**workstream_events_identifiers_snapshot**](WorkstreamEventsApi.md#workstream_events_identifiers_snapshot) | **GET** /workstream_events/identifiers | /workstream_events/identifiers [GET]
[**workstream_events_snapshot**](WorkstreamEventsApi.md#workstream_events_snapshot) | **GET** /workstream_events | /workstream_events [GET]


# **workstream_events_batch**
> WorkstreamEventsBatchFetchOutput workstream_events_batch(workstream_events_batch_fetch_input, transferables=transferables)

/workstream_events/batch/fetch [POST]

Batch fetch workstream events by providing a list of UUIDs.
This endpoint allows for efficient retrieval of multiple workstream events in a single request.
The response will include successfully fetched events and a list of any UUIDs that were not found.
Note: If a UUID in the batch doesn't exist, it will be caught and added to the notFound list in the response.
The transferables query parameter defaults to false for performance optimization.


### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.workstream_events_batch_fetch_input import WorkstreamEventsBatchFetchInput
from pieces_os_client.models.workstream_events_batch_fetch_output import WorkstreamEventsBatchFetchOutput
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
    api_instance = pieces_os_client.WorkstreamEventsApi(api_client)
    workstream_events_batch_fetch_input = pieces_os_client.WorkstreamEventsBatchFetchInput() # WorkstreamEventsBatchFetchInput | 
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /workstream_events/batch/fetch [POST]
        api_response = api_instance.workstream_events_batch(workstream_events_batch_fetch_input, transferables=transferables)
        print("The response of WorkstreamEventsApi->workstream_events_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamEventsApi->workstream_events_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_events_batch_fetch_input** | [**WorkstreamEventsBatchFetchInput**](WorkstreamEventsBatchFetchInput.md)|  | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**WorkstreamEventsBatchFetchOutput**](WorkstreamEventsBatchFetchOutput.md)

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

# **workstream_events_create_new_workstream_event**
> WorkstreamEvent workstream_events_create_new_workstream_event(transferables=transferables, seeded_workstream_event=seeded_workstream_event)

/workstream_events/create [POST]

This will create a new WorkstreamEvent in the database.

### Example

* Api Key Authentication (application):

```python
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

# **workstream_events_delete_specific_workstream_event**
> workstream_events_delete_specific_workstream_event(workstream_event)

/workstream_events/{workstream_event}/delete [POST]

This will delete a specific workstream_event from the database!

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

# **workstream_events_identifiers_snapshot**
> FlattenedWorkstreamEvents workstream_events_identifiers_snapshot(limit=limit, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to)

/workstream_events/identifiers [GET]

This is going to return all the identifiers of the workstream event in order of most recent -> oldest.

Note: When both created and updated timestamp filters are provided, the filters default to OR logic.
This means events will match if they satisfy EITHER the created timestamp range OR the updated timestamp range.


### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.flattened_workstream_events import FlattenedWorkstreamEvents
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
    api_instance = pieces_os_client.WorkstreamEventsApi(api_client)
    limit = 56 # int | Maximum number of results to return. (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter results to include only events created from this timestamp onwards. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter results to include only events created up to this timestamp. (optional)
    updated_from = '2013-10-20T19:20:30+01:00' # datetime | Filter results to include only events updated from this timestamp onwards. (optional)
    updated_to = '2013-10-20T19:20:30+01:00' # datetime | Filter results to include only events updated up to this timestamp. (optional)

    try:
        # /workstream_events/identifiers [GET]
        api_response = api_instance.workstream_events_identifiers_snapshot(limit=limit, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to)
        print("The response of WorkstreamEventsApi->workstream_events_identifiers_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamEventsApi->workstream_events_identifiers_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results to return. | [optional] 
 **created_from** | **datetime**| Filter results to include only events created from this timestamp onwards. | [optional] 
 **created_to** | **datetime**| Filter results to include only events created up to this timestamp. | [optional] 
 **updated_from** | **datetime**| Filter results to include only events updated from this timestamp onwards. | [optional] 
 **updated_to** | **datetime**| Filter results to include only events updated up to this timestamp. | [optional] 

### Return type

[**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md)

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

# **workstream_events_snapshot**
> WorkstreamEvents workstream_events_snapshot(transferables=transferables)

/workstream_events [GET]

This will get a snapshot of all your workstream events.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.workstream_events import WorkstreamEvents
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

