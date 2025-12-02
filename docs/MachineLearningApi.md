# pieces_os_client.MachineLearningApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**personification_technical_language_generation**](MachineLearningApi.md#personification_technical_language_generation) | **POST** /machine_learning/text/technical_language/generators/personification | /machine_learning/text/technical_language/generators/personification [GET]


# **personification_technical_language_generation**
> OnboardedPersonaDetails personification_technical_language_generation(preonboarded_persona_details=preonboarded_persona_details)

/machine_learning/text/technical_language/generators/personification [GET]

This is going to take in some personification details ie languages & personas.

and will return generated Seeds that can be used as snippets post/pre onboarding.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.onboarded_persona_details import OnboardedPersonaDetails
from pieces_os_client.models.preonboarded_persona_details import PreonboardedPersonaDetails
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
    api_instance = pieces_os_client.MachineLearningApi(api_client)
    preonboarded_persona_details = pieces_os_client.PreonboardedPersonaDetails() # PreonboardedPersonaDetails |  (optional)

    try:
        # /machine_learning/text/technical_language/generators/personification [GET]
        api_response = api_instance.personification_technical_language_generation(preonboarded_persona_details=preonboarded_persona_details)
        print("The response of MachineLearningApi->personification_technical_language_generation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MachineLearningApi->personification_technical_language_generation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preonboarded_persona_details** | [**PreonboardedPersonaDetails**](PreonboardedPersonaDetails.md)|  | [optional] 

### Return type

[**OnboardedPersonaDetails**](OnboardedPersonaDetails.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

