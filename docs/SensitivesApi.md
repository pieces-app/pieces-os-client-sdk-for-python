# pieces_os_client.SensitivesApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_sensitives**](SensitivesApi.md#search_sensitives) | **POST** /sensitives/search | /sensitives/search [POST]
[**sensitives_create_new_sensitive**](SensitivesApi.md#sensitives_create_new_sensitive) | **POST** /sensitives/create | /sensitives/create [POST]
[**sensitives_delete_sensitive**](SensitivesApi.md#sensitives_delete_sensitive) | **POST** /sensitives/{sensitive}/delete | /sensitives/{sensitive}/delete [POST]
[**sensitives_snapshot**](SensitivesApi.md#sensitives_snapshot) | **GET** /sensitives | /sensitives [GET]
[**sensitives_stream_identifiers**](SensitivesApi.md#sensitives_stream_identifiers) | **GET** /sensitives/stream/identifiers | /sensitives/stream/identifiers [WS]


# **search_sensitives**
> SearchedSensitives search_sensitives(transferables=transferables, search_input=search_input)

/sensitives/search [POST]

This will search your sensitives for a specific sensitive

note: we will search the value of the sensitive

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.search_input import SearchInput
from pieces_os_client.models.searched_sensitives import SearchedSensitives
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
    api_instance = pieces_os_client.SensitivesApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    search_input = pieces_os_client.SearchInput() # SearchInput |  (optional)

    try:
        # /sensitives/search [POST]
        api_response = api_instance.search_sensitives(transferables=transferables, search_input=search_input)
        print("The response of SensitivesApi->search_sensitives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensitivesApi->search_sensitives: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **search_input** | [**SearchInput**](SearchInput.md)|  | [optional] 

### Return type

[**SearchedSensitives**](SearchedSensitives.md)

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

# **sensitives_create_new_sensitive**
> Sensitive sensitives_create_new_sensitive(seeded_sensitive=seeded_sensitive)

/sensitives/create [POST]

This will create a new sensitive model.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.seeded_sensitive import SeededSensitive
from pieces_os_client.models.sensitive import Sensitive
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
    api_instance = pieces_os_client.SensitivesApi(api_client)
    seeded_sensitive = pieces_os_client.SeededSensitive() # SeededSensitive |  (optional)

    try:
        # /sensitives/create [POST]
        api_response = api_instance.sensitives_create_new_sensitive(seeded_sensitive=seeded_sensitive)
        print("The response of SensitivesApi->sensitives_create_new_sensitive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensitivesApi->sensitives_create_new_sensitive: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_sensitive** | [**SeededSensitive**](SeededSensitive.md)|  | [optional] 

### Return type

[**Sensitive**](Sensitive.md)

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

# **sensitives_delete_sensitive**
> sensitives_delete_sensitive(sensitive)

/sensitives/{sensitive}/delete [POST]

This will delete a sensitive based on the sensitive uuid.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
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
    api_instance = pieces_os_client.SensitivesApi(api_client)
    sensitive = 'sensitive_example' # str | This is a uuid that represents a sensitive.

    try:
        # /sensitives/{sensitive}/delete [POST]
        api_instance.sensitives_delete_sensitive(sensitive)
    except Exception as e:
        print("Exception when calling SensitivesApi->sensitives_delete_sensitive: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensitive** | **str**| This is a uuid that represents a sensitive. | 

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensitives_snapshot**
> Sensitives sensitives_snapshot()

/sensitives [GET]

This will get a snapshot of all of the sensitives.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.sensitives import Sensitives
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
    api_instance = pieces_os_client.SensitivesApi(api_client)

    try:
        # /sensitives [GET]
        api_response = api_instance.sensitives_snapshot()
        print("The response of SensitivesApi->sensitives_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensitivesApi->sensitives_snapshot: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Sensitives**](Sensitives.md)

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

# **sensitives_stream_identifiers**
> StreamedIdentifiers sensitives_stream_identifiers()

/sensitives/stream/identifiers [WS]

Provides a WebSocket connection that emits changes to your sensitive identifiers (UUIDs).

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.streamed_identifiers import StreamedIdentifiers
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
    api_instance = pieces_os_client.SensitivesApi(api_client)

    try:
        # /sensitives/stream/identifiers [WS]
        api_response = api_instance.sensitives_stream_identifiers()
        print("The response of SensitivesApi->sensitives_stream_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensitivesApi->sensitives_stream_identifiers: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**StreamedIdentifiers**](StreamedIdentifiers.md)

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

