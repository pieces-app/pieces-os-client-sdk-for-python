# openapi_client.DistributionsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**distributions_create_new_distribution**](DistributionsApi.md#distributions_create_new_distribution) | **POST** /distributions/create | /distributions/create [POST]
[**distributions_delete_specific_distribution**](DistributionsApi.md#distributions_delete_specific_distribution) | **POST** /distributions/{distribution}/delete | /distributions/{distribution}/delete [POST]
[**distributions_snapshot**](DistributionsApi.md#distributions_snapshot) | **GET** /distributions | /distributions [GET]


# **distributions_create_new_distribution**
> Distribution distributions_create_new_distribution(seeded_distribution=seeded_distribution)

/distributions/create [POST]

This will create a new distribution.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.distribution import Distribution
from openapi_client.models.seeded_distribution import SeededDistribution
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
    api_instance = openapi_client.DistributionsApi(api_client)
    seeded_distribution = openapi_client.SeededDistribution() # SeededDistribution |  (optional)

    try:
        # /distributions/create [POST]
        api_response = api_instance.distributions_create_new_distribution(seeded_distribution=seeded_distribution)
        print("The response of DistributionsApi->distributions_create_new_distribution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionsApi->distributions_create_new_distribution: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_distribution** | [**SeededDistribution**](SeededDistribution.md)|  | [optional] 

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

# **distributions_delete_specific_distribution**
> distributions_delete_specific_distribution(distribution)

/distributions/{distribution}/delete [POST]

This will delete a specific distribution.

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
    api_instance = openapi_client.DistributionsApi(api_client)
    distribution = 'distribution_example' # str | This is the uuid of a specific distribution.

    try:
        # /distributions/{distribution}/delete [POST]
        api_instance.distributions_delete_specific_distribution(distribution)
    except Exception as e:
        print("Exception when calling DistributionsApi->distributions_delete_specific_distribution: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution** | **str**| This is the uuid of a specific distribution. | 

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

# **distributions_snapshot**
> Distributions distributions_snapshot()

/distributions [GET]

This will get a specific snapshot of all our distributions.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.distributions import Distributions
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
    api_instance = openapi_client.DistributionsApi(api_client)

    try:
        # /distributions [GET]
        api_response = api_instance.distributions_snapshot()
        print("The response of DistributionsApi->distributions_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DistributionsApi->distributions_snapshot: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Distributions**](Distributions.md)

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

