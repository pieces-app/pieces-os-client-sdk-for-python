# openapi_client.HintsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hints_create_new_hint**](HintsApi.md#hints_create_new_hint) | **POST** /hints/create | /hints/create [POST]
[**hints_delete_specific_hint**](HintsApi.md#hints_delete_specific_hint) | **POST** /hints/{hint}/delete | /hints/{hint}/delete [POST]
[**hints_snapshot**](HintsApi.md#hints_snapshot) | **GET** /hints | /hints [GET]


# **hints_create_new_hint**
> Hint hints_create_new_hint(seeded_hint=seeded_hint)

/hints/create [POST]

This will create a hint.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.hint import Hint
from openapi_client.models.seeded_hint import SeededHint
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
    api_instance = openapi_client.HintsApi(api_client)
    seeded_hint = openapi_client.SeededHint() # SeededHint |  (optional)

    try:
        # /hints/create [POST]
        api_response = api_instance.hints_create_new_hint(seeded_hint=seeded_hint)
        print("The response of HintsApi->hints_create_new_hint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HintsApi->hints_create_new_hint: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_hint** | [**SeededHint**](SeededHint.md)|  | [optional] 

### Return type

[**Hint**](Hint.md)

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

# **hints_delete_specific_hint**
> hints_delete_specific_hint(hint)

/hints/{hint}/delete [POST]

This will delete a specific hint.

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
    api_instance = openapi_client.HintsApi(api_client)
    hint = 'hint_example' # str | This is a specific hint uuid

    try:
        # /hints/{hint}/delete [POST]
        api_instance.hints_delete_specific_hint(hint)
    except Exception as e:
        print("Exception when calling HintsApi->hints_delete_specific_hint: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hint** | **str**| This is a specific hint uuid | 

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

# **hints_snapshot**
> Hints hints_snapshot()

/hints [GET]

This will get a snapshot of all of the hints.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.hints import Hints
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
    api_instance = openapi_client.HintsApi(api_client)

    try:
        # /hints [GET]
        api_response = api_instance.hints_snapshot()
        print("The response of HintsApi->hints_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HintsApi->hints_snapshot: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Hints**](Hints.md)

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

