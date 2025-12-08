# pieces_os_client.MetricsApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics_formats**](MetricsApi.md#get_metrics_formats) | **GET** /metrics/formats | /metrics/formats [GET]
[**metrics_formats_ordered**](MetricsApi.md#metrics_formats_ordered) | **GET** /metrics/formats/ordered | /metrics/formats/ordered [GET]


# **get_metrics_formats**
> FormatsMetrics get_metrics_formats()

/metrics/formats [GET]

This is going to get a snapshot of our FormatsMetrics

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.formats_metrics import FormatsMetrics
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
    api_instance = pieces_os_client.MetricsApi(api_client)

    try:
        # /metrics/formats [GET]
        api_response = api_instance.get_metrics_formats()
        print("The response of MetricsApi->get_metrics_formats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_metrics_formats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FormatsMetrics**](FormatsMetrics.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_formats_ordered**
> OrderedMetrics metrics_formats_ordered()

/metrics/formats/ordered [GET]

This will return a list of code formats in desc order from most to least formats uploaded.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.ordered_metrics import OrderedMetrics
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
    api_instance = pieces_os_client.MetricsApi(api_client)

    try:
        # /metrics/formats/ordered [GET]
        api_response = api_instance.metrics_formats_ordered()
        print("The response of MetricsApi->metrics_formats_ordered:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->metrics_formats_ordered: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrderedMetrics**](OrderedMetrics.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

