# openapi_client.DistributionApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**distribution_update**](DistributionApi.md#distribution_update) | **POST** /distribution/update | /distribution/update [POST]
[**distributions_specific_distribution_snapshot**](DistributionApi.md#distributions_specific_distribution_snapshot) | **GET** /distribution/{distribution} | /distribution/{distribution} [GET]


# **distribution_update**
> Distribution distribution_update(distribution=distribution)

/distribution/update [POST]

This will update a specific Distribution.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.distribution import Distribution
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
    api_instance = openapi_client.DistributionApi(api_client)
    distribution = openapi_client.Distribution() # Distribution |  (optional)

    try:
        # /distribution/update [POST]
        api_response = api_instance.distribution_update(distribution=distribution)
        print("The response of DistributionApi->distribution_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionApi->distribution_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution** | [**Distribution**](Distribution.md)|  | [optional] 

### Return type

[**Distribution**](Distribution.md)

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

# **distributions_specific_distribution_snapshot**
> Distribution distributions_specific_distribution_snapshot(distribution)

/distribution/{distribution} [GET]

This will get a specific snapshot of a distribution.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.distribution import Distribution
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
    api_instance = openapi_client.DistributionApi(api_client)
    distribution = 'distribution_example' # str | This is the uuid of a specific distribution.

    try:
        # /distribution/{distribution} [GET]
        api_response = api_instance.distributions_specific_distribution_snapshot(distribution)
        print("The response of DistributionApi->distributions_specific_distribution_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionApi->distributions_specific_distribution_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution** | **str**| This is the uuid of a specific distribution. | 

### Return type

[**Distribution**](Distribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**410** | Distribution not found. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

