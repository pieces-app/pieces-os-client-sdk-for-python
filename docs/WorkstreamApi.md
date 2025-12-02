# pieces_os_client.WorkstreamApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workstream_suggestions_refresh**](WorkstreamApi.md#workstream_suggestions_refresh) | **POST** /workstream/suggestions/refresh | /workstream/suggestions/refresh [POST]
[**workstream_suggestions_stream**](WorkstreamApi.md#workstream_suggestions_stream) | **GET** /workstream/suggestions/stream | /workstream/suggestions/stream [WS]


# **workstream_suggestions_refresh**
> WorkstreamSuggestionsRefresh workstream_suggestions_refresh(seeded_workstream_suggestions_refresh=seeded_workstream_suggestions_refresh)

/workstream/suggestions/refresh [POST]

This will trigger a refresh(recalculation) of the suggestions items.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.seeded_workstream_suggestions_refresh import SeededWorkstreamSuggestionsRefresh
from pieces_os_client.models.workstream_suggestions_refresh import WorkstreamSuggestionsRefresh
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
    api_instance = pieces_os_client.WorkstreamApi(api_client)
    seeded_workstream_suggestions_refresh = pieces_os_client.SeededWorkstreamSuggestionsRefresh() # SeededWorkstreamSuggestionsRefresh |  (optional)

    try:
        # /workstream/suggestions/refresh [POST]
        api_response = api_instance.workstream_suggestions_refresh(seeded_workstream_suggestions_refresh=seeded_workstream_suggestions_refresh)
        print("The response of WorkstreamApi->workstream_suggestions_refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamApi->workstream_suggestions_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_workstream_suggestions_refresh** | [**SeededWorkstreamSuggestionsRefresh**](SeededWorkstreamSuggestionsRefresh.md)|  | [optional] 

### Return type

[**WorkstreamSuggestionsRefresh**](WorkstreamSuggestionsRefresh.md)

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

# **workstream_suggestions_stream**
> WorkstreamSuggestions workstream_suggestions_stream()

/workstream/suggestions/stream [WS]

Provides a WebSocket connection that emits changes to your workstream suggestions.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.workstream_suggestions import WorkstreamSuggestions
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
    api_instance = pieces_os_client.WorkstreamApi(api_client)

    try:
        # /workstream/suggestions/stream [WS]
        api_response = api_instance.workstream_suggestions_stream()
        print("The response of WorkstreamApi->workstream_suggestions_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamApi->workstream_suggestions_stream: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WorkstreamSuggestions**](WorkstreamSuggestions.md)

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

