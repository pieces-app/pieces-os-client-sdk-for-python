# pieces_os_client.OpenAIApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**open_ai_models_list**](OpenAIApi.md#open_ai_models_list) | **POST** /open_ai/models/list | /open_ai/models/list [POST]


# **open_ai_models_list**
> OpenAIModelsListOutput open_ai_models_list(open_ai_models_list_input=open_ai_models_list_input)

/open_ai/models/list [POST]

This will get a list of all of your Models from OpenAI w/ you user.auth0.openAI.apiKey.

if the user is unauthenticated or if the openAI key doesnt exist or if it is invalid we will return a 401.

Requires internet as this will ping out to OpenAI's server to get the models.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.open_ai_models_list_input import OpenAIModelsListInput
from pieces_os_client.models.open_ai_models_list_output import OpenAIModelsListOutput
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
    api_instance = pieces_os_client.OpenAIApi(api_client)
    open_ai_models_list_input = pieces_os_client.OpenAIModelsListInput() # OpenAIModelsListInput |  (optional)

    try:
        # /open_ai/models/list [POST]
        api_response = api_instance.open_ai_models_list(open_ai_models_list_input=open_ai_models_list_input)
        print("The response of OpenAIApi->open_ai_models_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenAIApi->open_ai_models_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_ai_models_list_input** | [**OpenAIModelsListInput**](OpenAIModelsListInput.md)|  | [optional] 

### Return type

[**OpenAIModelsListOutput**](OpenAIModelsListOutput.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Invalid Authentication, Incorrect API key provided or organization |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

