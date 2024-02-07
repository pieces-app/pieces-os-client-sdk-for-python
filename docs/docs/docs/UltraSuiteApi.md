# openapi_client.UltraSuiteApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_create_ultra_suite_asset**](UltraSuiteApi.md#assets_create_ultra_suite_asset) | **POST** /ultra_suite/assets/create | /ultra_suite/assets/create [POST]


# **assets_create_ultra_suite_asset**
> Asset assets_create_ultra_suite_asset(seeded_ultra_suite_asset=seeded_ultra_suite_asset)

/ultra_suite/assets/create [POST]

This Endpoint will create an Asset that is sent from UltraSuite.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.asset import Asset
from openapi_client.models.seeded_ultra_suite_asset import SeededUltraSuiteAsset
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
    api_instance = openapi_client.UltraSuiteApi(api_client)
    seeded_ultra_suite_asset = openapi_client.SeededUltraSuiteAsset() # SeededUltraSuiteAsset |  (optional)

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

