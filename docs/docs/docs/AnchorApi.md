# openapi_client.AnchorApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anchor_rename**](AnchorApi.md#anchor_rename) | **POST** /anchor/{anchor}/rename | /anchor/{anchor}/rename [POST]
[**anchor_scores_increment**](AnchorApi.md#anchor_scores_increment) | **POST** /anchor/{anchor}/scores/increment | &#39;/anchor/{anchor}/scores/increment&#39; [POST]
[**anchor_specific_anchor_snapshot**](AnchorApi.md#anchor_specific_anchor_snapshot) | **GET** /anchor/{anchor} | /anchor/{anchor} [GET]
[**anchor_update**](AnchorApi.md#anchor_update) | **POST** /anchor/update | /anchor/update [POST]


# **anchor_rename**
> Anchor anchor_rename(anchor, transferables=transferables)

/anchor/{anchor}/rename [POST]

This will rename a specific anchor.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.anchor import Anchor
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
    api_instance = openapi_client.AnchorApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /anchor/{anchor}/rename [POST]
        api_response = api_instance.anchor_rename(anchor, transferables=transferables)
        print("The response of AnchorApi->anchor_rename:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_rename: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor** | **str**| This is the specific uuid of an anchor. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Anchor**](Anchor.md)

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

# **anchor_scores_increment**
> anchor_scores_increment(anchor, seeded_score_increment=seeded_score_increment)

'/anchor/{anchor}/scores/increment' [POST]

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
    api_instance = openapi_client.AnchorApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.
    seeded_score_increment = openapi_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # '/anchor/{anchor}/scores/increment' [POST]
        api_instance.anchor_scores_increment(anchor, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_scores_increment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor** | **str**| This is the specific uuid of an anchor. | 
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

# **anchor_specific_anchor_snapshot**
> Anchor anchor_specific_anchor_snapshot(anchor, transferables=transferables)

/anchor/{anchor} [GET]

This will get a snapshot of a single anchor.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.anchor import Anchor
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
    api_instance = openapi_client.AnchorApi(api_client)
    anchor = 'anchor_example' # str | This is the specific uuid of an anchor.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /anchor/{anchor} [GET]
        api_response = api_instance.anchor_specific_anchor_snapshot(anchor, transferables=transferables)
        print("The response of AnchorApi->anchor_specific_anchor_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_specific_anchor_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anchor** | **str**| This is the specific uuid of an anchor. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Anchor**](Anchor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**410** | Anchor not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **anchor_update**
> Anchor anchor_update(transferables=transferables, anchor=anchor)

/anchor/update [POST]

This will update a specific anchor.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.anchor import Anchor
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
    api_instance = openapi_client.AnchorApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    anchor = openapi_client.Anchor() # Anchor |  (optional)

    try:
        # /anchor/update [POST]
        api_response = api_instance.anchor_update(transferables=transferables, anchor=anchor)
        print("The response of AnchorApi->anchor_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnchorApi->anchor_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **anchor** | [**Anchor**](Anchor.md)|  | [optional] 

### Return type

[**Anchor**](Anchor.md)

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

