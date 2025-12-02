# pieces_os_client.OCRAnalysesApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ocr_analyses_snapshot**](OCRAnalysesApi.md#ocr_analyses_snapshot) | **GET** /ocr_analyses | Your GET endpoint


# **ocr_analyses_snapshot**
> OCRAnalyses ocr_analyses_snapshot(transferables=transferables)

Your GET endpoint

This will get a snapshot of all of your ocr analyses, an ocr analysis is attached to an image analysis.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.ocr_analyses import OCRAnalyses
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
    api_instance = pieces_os_client.OCRAnalysesApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # Your GET endpoint
        api_response = api_instance.ocr_analyses_snapshot(transferables=transferables)
        print("The response of OCRAnalysesApi->ocr_analyses_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OCRAnalysesApi->ocr_analyses_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**OCRAnalyses**](OCRAnalyses.md)

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

