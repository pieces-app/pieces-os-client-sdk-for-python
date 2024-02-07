# openapi_client.MachineLearningApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**segment_technical_language**](MachineLearningApi.md#segment_technical_language) | **POST** /machine_learning/text/technical_language/parsers/segmentation | /machine_learning/text/technical_language/parsers/segmentation [POST]


# **segment_technical_language**
> SegmentedTechnicalLanguage segment_technical_language(classify=classify, unsegmented_technical_language=unsegmented_technical_language)

/machine_learning/text/technical_language/parsers/segmentation [POST]

This is a functional endpoint that will parse a message or text in to text or code.  if the optional query param is passed along 'classify' then we will optionally classify the just the code that is segmented.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.segmented_technical_language import SegmentedTechnicalLanguage
from openapi_client.models.unsegmented_technical_language import UnsegmentedTechnicalLanguage
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
    api_instance = openapi_client.MachineLearningApi(api_client)
    classify = True # bool | This will let us know if you want us to classifiy your code, this is default to false. (optional)
    unsegmented_technical_language = openapi_client.UnsegmentedTechnicalLanguage() # UnsegmentedTechnicalLanguage |  (optional)

    try:
        # /machine_learning/text/technical_language/parsers/segmentation [POST]
        api_response = api_instance.segment_technical_language(classify=classify, unsegmented_technical_language=unsegmented_technical_language)
        print("The response of MachineLearningApi->segment_technical_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachineLearningApi->segment_technical_language: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classify** | **bool**| This will let us know if you want us to classifiy your code, this is default to false. | [optional] 
 **unsegmented_technical_language** | [**UnsegmentedTechnicalLanguage**](UnsegmentedTechnicalLanguage.md)|  | [optional] 

### Return type

[**SegmentedTechnicalLanguage**](SegmentedTechnicalLanguage.md)

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

