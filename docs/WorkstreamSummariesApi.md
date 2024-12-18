# pieces_os_client.WorkstreamSummariesApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_workstream_summaries**](WorkstreamSummariesApi.md#search_workstream_summaries) | **POST** /workstream_summaries/search | /workstream_summaries/search [POST]
[**workstream_summaries_create_new_workstream_summary**](WorkstreamSummariesApi.md#workstream_summaries_create_new_workstream_summary) | **POST** /workstream_summaries/create | /workstream_summaries/create [POST]
[**workstream_summaries_delete_specific_workstream_summary**](WorkstreamSummariesApi.md#workstream_summaries_delete_specific_workstream_summary) | **POST** /workstream_summaries/{workstream_summary}/delete | /workstream_summaries/{workstream_summary}/delete [POST]
[**workstream_summaries_snapshot**](WorkstreamSummariesApi.md#workstream_summaries_snapshot) | **GET** /workstream_summaries | /workstream_summaries [GET]


# **search_workstream_summaries**
> SearchedWorkstreamSummaries search_workstream_summaries(transferables=transferables, search_input=search_input)

/workstream_summaries/search [POST]

This will search your workstream_summaries for a specific workstream_summary  note: we will just search the summary value(which is an annotation)

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.search_input import SearchInput
from pieces_os_client.models.searched_workstream_summaries import SearchedWorkstreamSummaries
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
    api_instance = pieces_os_client.WorkstreamSummariesApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    search_input = pieces_os_client.SearchInput() # SearchInput |  (optional)

    try:
        # /workstream_summaries/search [POST]
        api_response = api_instance.search_workstream_summaries(transferables=transferables, search_input=search_input)
        print("The response of WorkstreamSummariesApi->search_workstream_summaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamSummariesApi->search_workstream_summaries: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **search_input** | [**SearchInput**](SearchInput.md)|  | [optional] 

### Return type

[**SearchedWorkstreamSummaries**](SearchedWorkstreamSummaries.md)

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

# **workstream_summaries_create_new_workstream_summary**
> WorkstreamSummary workstream_summaries_create_new_workstream_summary(transferables=transferables, seeded_workstream_summary=seeded_workstream_summary)

/workstream_summaries/create [POST]

This will create a new WorkstreamSummary in the database.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.seeded_workstream_summary import SeededWorkstreamSummary
from pieces_os_client.models.workstream_summary import WorkstreamSummary
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
    api_instance = pieces_os_client.WorkstreamSummariesApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    seeded_workstream_summary = pieces_os_client.SeededWorkstreamSummary() # SeededWorkstreamSummary |  (optional)

    try:
        # /workstream_summaries/create [POST]
        api_response = api_instance.workstream_summaries_create_new_workstream_summary(transferables=transferables, seeded_workstream_summary=seeded_workstream_summary)
        print("The response of WorkstreamSummariesApi->workstream_summaries_create_new_workstream_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamSummariesApi->workstream_summaries_create_new_workstream_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **seeded_workstream_summary** | [**SeededWorkstreamSummary**](SeededWorkstreamSummary.md)|  | [optional] 

### Return type

[**WorkstreamSummary**](WorkstreamSummary.md)

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

# **workstream_summaries_delete_specific_workstream_summary**
> workstream_summaries_delete_specific_workstream_summary(workstream_summary)

/workstream_summaries/{workstream_summary}/delete [POST]

This will delete a specific workstream_summary from the database!

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
    api_instance = pieces_os_client.WorkstreamSummariesApi(api_client)
    workstream_summary = 'workstream_summary_example' # str | This is a identifier that is used to identify a specific workstream_summary.

    try:
        # /workstream_summaries/{workstream_summary}/delete [POST]
        api_instance.workstream_summaries_delete_specific_workstream_summary(workstream_summary)
    except Exception as e:
        print("Exception when calling WorkstreamSummariesApi->workstream_summaries_delete_specific_workstream_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **workstream_summaries_snapshot**
> WorkstreamSummaries workstream_summaries_snapshot(transferables=transferables)

/workstream_summaries [GET]

This will get a snapshot of all your workstream summaries.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_summaries import WorkstreamSummaries
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
    api_instance = pieces_os_client.WorkstreamSummariesApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /workstream_summaries [GET]
        api_response = api_instance.workstream_summaries_snapshot(transferables=transferables)
        print("The response of WorkstreamSummariesApi->workstream_summaries_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamSummariesApi->workstream_summaries_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**WorkstreamSummaries**](WorkstreamSummaries.md)

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

