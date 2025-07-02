# pieces_os_client.PaddleCheckoutApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paddle_checkout_update_status**](PaddleCheckoutApi.md#paddle_checkout_update_status) | **POST** /paddle_checkout/update_status | /paddle_checkout/update_status [POST]


# **paddle_checkout_update_status**
> str paddle_checkout_update_status(paddle_checkout_event)

/paddle_checkout/update_status [POST]

Accepts webhook-style events for checkout lifecycle updates.
Supports checkout.loaded, checkout.closed, checkout.updated,
checkout.completed, checkout.warning, and checkout.error.
The request body must include a top-level discriminator field (name for normal events,
type for warning/error) to select the correct payload schema.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.paddle_checkout_event import PaddleCheckoutEvent
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
    api_instance = pieces_os_client.PaddleCheckoutApi(api_client)
    paddle_checkout_event = pieces_os_client.PaddleCheckoutEvent() # PaddleCheckoutEvent | 

    try:
        # /paddle_checkout/update_status [POST]
        api_response = api_instance.paddle_checkout_update_status(paddle_checkout_event)
        print("The response of PaddleCheckoutApi->paddle_checkout_update_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaddleCheckoutApi->paddle_checkout_update_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paddle_checkout_event** | [**PaddleCheckoutEvent**](PaddleCheckoutEvent.md)|  | 

### Return type

**str**

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully processed |  -  |
**400** | Invalid payload |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

