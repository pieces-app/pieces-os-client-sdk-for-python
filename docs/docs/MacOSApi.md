# openapi_client.MacOSApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_create_new_asset_from_macos**](MacOSApi.md#assets_create_new_asset_from_macos) | **POST** /macos/assets/create | /macos/assets/create [Post]


# **assets_create_new_asset_from_macos**
> Asset assets_create_new_asset_from_macos(seeded_mac_os_asset=seeded_mac_os_asset)

/macos/assets/create [Post]

Exposes an endpoint for the MacOS Services plugin to send over MacOS Specific Data

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.asset import Asset
from openapi_client.models.seeded_mac_os_asset import SeededMacOSAsset
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
    api_instance = openapi_client.MacOSApi(api_client)
    seeded_mac_os_asset = openapi_client.SeededMacOSAsset() # SeededMacOSAsset | A SeededMacosApplication which contains the value and an Application Instance (optional)

    try:
        # /macos/assets/create [Post]
        api_response = api_instance.assets_create_new_asset_from_macos(seeded_mac_os_asset=seeded_mac_os_asset)
        print("The response of MacOSApi->assets_create_new_asset_from_macos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MacOSApi->assets_create_new_asset_from_macos: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_mac_os_asset** | [**SeededMacOSAsset**](SeededMacOSAsset.md)| A SeededMacosApplication which contains the value and an Application Instance | [optional] 

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

