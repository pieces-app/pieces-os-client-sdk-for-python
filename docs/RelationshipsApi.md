# pieces_os_client.RelationshipsApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**relationships_snapshot**](RelationshipsApi.md#relationships_snapshot) | **GET** /relationships | /relationships [GET]


# **relationships_snapshot**
> Relationships relationships_snapshot()

/relationships [GET]

This will return all of the relationships that exists within your pieces db.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.relationships import Relationships
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
    api_instance = pieces_os_client.RelationshipsApi(api_client)

    try:
        # /relationships [GET]
        api_response = api_instance.relationships_snapshot()
        print("The response of RelationshipsApi->relationships_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RelationshipsApi->relationships_snapshot: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Relationships**](Relationships.md)

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

