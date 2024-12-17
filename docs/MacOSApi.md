# pieces_os_client.MacOSApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_create_new_asset_from_macos**](MacOSApi.md#assets_create_new_asset_from_macos) | **POST** /macos/assets/create | /macos/assets/create [Post]


# **assets_create_new_asset_from_macos**
> Asset assets_create_new_asset_from_macos(seeded_mac_os_asset=seeded_mac_os_asset)

/macos/assets/create [Post]

Exposes an endpoint for the MacOS Services plugin to send over MacOS Specific Data

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.asset import Asset
from pieces_os_client.models.seeded_mac_os_asset import SeededMacOSAsset
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
    api_instance = pieces_os_client.MacOSApi(api_client)
    seeded_mac_os_asset = pieces_os_client.SeededMacOSAsset() # SeededMacOSAsset | A SeededMacosApplication which contains the value and an Application Instance (optional)

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

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

