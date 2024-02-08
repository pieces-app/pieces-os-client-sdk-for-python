# openapi_client.HintApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hint_scores_increment**](HintApi.md#hint_scores_increment) | **POST** /hint/{hint}/scores/increment | &#39;/hint/{hint}/scores/increment&#39; [POST]
[**hint_specific_hint_snapshot**](HintApi.md#hint_specific_hint_snapshot) | **GET** /hint/{hint} | /hint/{hint} [POST]
[**hint_update**](HintApi.md#hint_update) | **POST** /hint/update | /hint/update [POST]


# **hint_scores_increment**
> hint_scores_increment(hint, seeded_score_increment=seeded_score_increment)

'/hint/{hint}/scores/increment' [POST]

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
    api_instance = openapi_client.HintApi(api_client)
    hint = 'hint_example' # str | This is a specific hint uuid
    seeded_score_increment = openapi_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # '/hint/{hint}/scores/increment' [POST]
        api_instance.hint_scores_increment(hint, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling HintApi->hint_scores_increment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hint** | **str**| This is a specific hint uuid | 
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

# **hint_specific_hint_snapshot**
> Hint hint_specific_hint_snapshot(hint)

/hint/{hint} [POST]

This will get a snapshot of a specific hint.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.hint import Hint
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
    api_instance = openapi_client.HintApi(api_client)
    hint = 'hint_example' # str | This is a specific hint uuid

    try:
        # /hint/{hint} [POST]
        api_response = api_instance.hint_specific_hint_snapshot(hint)
        print("The response of HintApi->hint_specific_hint_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HintApi->hint_specific_hint_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hint** | **str**| This is a specific hint uuid | 

### Return type

[**Hint**](Hint.md)

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

# **hint_update**
> Hint hint_update(hint=hint)

/hint/update [POST]

This will update a specific hint.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.hint import Hint
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
    api_instance = openapi_client.HintApi(api_client)
    hint = openapi_client.Hint() # Hint |  (optional)

    try:
        # /hint/update [POST]
        api_response = api_instance.hint_update(hint=hint)
        print("The response of HintApi->hint_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HintApi->hint_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hint** | [**Hint**](Hint.md)|  | [optional] 

### Return type

[**Hint**](Hint.md)

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

