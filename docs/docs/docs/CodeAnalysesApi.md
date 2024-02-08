# openapi_client.CodeAnalysesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**code_analyses_snapshot**](CodeAnalysesApi.md#code_analyses_snapshot) | **GET** /code_analyses | Your GET endpoint


# **code_analyses_snapshot**
> CodeAnalyses code_analyses_snapshot()

Your GET endpoint

This will get a snapshot of all of your code analyses, a code analysis is attached to an analysis.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.code_analyses import CodeAnalyses
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
    api_instance = openapi_client.CodeAnalysesApi(api_client)

    try:
        # Your GET endpoint
        api_response = api_instance.code_analyses_snapshot()
        print("The response of CodeAnalysesApi->code_analyses_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeAnalysesApi->code_analyses_snapshot: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**CodeAnalyses**](CodeAnalyses.md)

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

