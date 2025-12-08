# pieces_os_client.DeepResearchApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deep_research_stream**](DeepResearchApi.md#deep_research_stream) | **GET** /deep_research/stream | /deep_research/stream [WS]


# **deep_research_stream**
> DeepResearchStreamOutput deep_research_stream(deep_research_stream_input=deep_research_stream_input)

/deep_research/stream [WS]

Provides a WebSocket connection that streams inputs to deep research. It handles relevance and questions, but will throw an error if both are passed in simultaneously. However, if you wish to utilize both question and relevance, you can obtain stream results by passing relevance with the option 'question:true'. It is designed to manage multiple conversations.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.deep_research_stream_input import DeepResearchStreamInput
from pieces_os_client.models.deep_research_stream_output import DeepResearchStreamOutput
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
    api_instance = pieces_os_client.DeepResearchApi(api_client)
    deep_research_stream_input = pieces_os_client.DeepResearchStreamInput() # DeepResearchStreamInput |  (optional)

    try:
        # /deep_research/stream [WS]
        api_response = api_instance.deep_research_stream(deep_research_stream_input=deep_research_stream_input)
        print("The response of DeepResearchApi->deep_research_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeepResearchApi->deep_research_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deep_research_stream_input** | [**DeepResearchStreamInput**](DeepResearchStreamInput.md)|  | [optional] 

### Return type

[**DeepResearchStreamOutput**](DeepResearchStreamOutput.md)

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
**429** | Rate limit/Quota exceeded |  -  |
**500** | Internal Server Error |  -  |
**503** | The engine is currently overloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

