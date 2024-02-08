# openapi_client.SensitiveApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sensitive_scores_increment**](SensitiveApi.md#sensitive_scores_increment) | **POST** /sensitive/{sensitive}/scores/increment | &#39;/sensitive/{sensitive}/scores/increment&#39; [POST]
[**sensitive_snapshot**](SensitiveApi.md#sensitive_snapshot) | **GET** /sensitive/{sensitive} | /sensitive/{sensitive} [GET]
[**update_sensitive**](SensitiveApi.md#update_sensitive) | **POST** /sensitive/update | /sensitive/update [POST]


# **sensitive_scores_increment**
> sensitive_scores_increment(sensitive, seeded_score_increment=seeded_score_increment)

'/sensitive/{sensitive}/scores/increment' [POST]

This will take in a SeededScoreIncrement and will increment the material relative to the incoming body.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.seeded_score_increment import SeededScoreIncrement
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
    api_instance = openapi_client.SensitiveApi(api_client)
    sensitive = 'sensitive_example' # str | This is a uuid that represents a sensitive.
    seeded_score_increment = openapi_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # '/sensitive/{sensitive}/scores/increment' [POST]
        api_instance.sensitive_scores_increment(sensitive, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling SensitiveApi->sensitive_scores_increment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensitive** | **str**| This is a uuid that represents a sensitive. | 
 **seeded_score_increment** | [**SeededScoreIncrement**](SeededScoreIncrement.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensitive_snapshot**
> Sensitive sensitive_snapshot(sensitive)

/sensitive/{sensitive} [GET]

This will get a specific sensitive via the sensitive uuid.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.sensitive import Sensitive
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
    api_instance = openapi_client.SensitiveApi(api_client)
    sensitive = 'sensitive_example' # str | 

    try:
        # /sensitive/{sensitive} [GET]
        api_response = api_instance.sensitive_snapshot(sensitive)
        print("The response of SensitiveApi->sensitive_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensitiveApi->sensitive_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensitive** | **str**|  | 

### Return type

[**Sensitive**](Sensitive.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sensitive**
> Sensitive update_sensitive(sensitive=sensitive)

/sensitive/update [POST]

This will update a specific sensitive

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.sensitive import Sensitive
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
    api_instance = openapi_client.SensitiveApi(api_client)
    sensitive = openapi_client.Sensitive() # Sensitive |  (optional)

    try:
        # /sensitive/update [POST]
        api_response = api_instance.update_sensitive(sensitive=sensitive)
        print("The response of SensitiveApi->update_sensitive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensitiveApi->update_sensitive: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensitive** | [**Sensitive**](Sensitive.md)|  | [optional] 

### Return type

[**Sensitive**](Sensitive.md)

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

