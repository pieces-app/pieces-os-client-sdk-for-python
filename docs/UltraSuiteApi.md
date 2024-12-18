# pieces_os_client.UltraSuiteApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_create_ultra_suite_asset**](UltraSuiteApi.md#assets_create_ultra_suite_asset) | **POST** /ultra_suite/assets/create | /ultra_suite/assets/create [POST]


# **assets_create_ultra_suite_asset**
> Asset assets_create_ultra_suite_asset(seeded_ultra_suite_asset=seeded_ultra_suite_asset)

/ultra_suite/assets/create [POST]

This Endpoint will create an Asset that is sent from UltraSuite.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.asset import Asset
from pieces_os_client.models.seeded_ultra_suite_asset import SeededUltraSuiteAsset
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
    api_instance = pieces_os_client.UltraSuiteApi(api_client)
    seeded_ultra_suite_asset = pieces_os_client.SeededUltraSuiteAsset() # SeededUltraSuiteAsset |  (optional)

    try:
        # /ultra_suite/assets/create [POST]
        api_response = api_instance.assets_create_ultra_suite_asset(seeded_ultra_suite_asset=seeded_ultra_suite_asset)
        print("The response of UltraSuiteApi->assets_create_ultra_suite_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UltraSuiteApi->assets_create_ultra_suite_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_ultra_suite_asset** | [**SeededUltraSuiteAsset**](SeededUltraSuiteAsset.md)|  | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

