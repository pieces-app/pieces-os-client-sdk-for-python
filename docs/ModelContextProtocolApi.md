# pieces_os_client.ModelContextProtocolApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**model_context_protocol_messages**](ModelContextProtocolApi.md#model_context_protocol_messages) | **POST** /model_context_protocol/{schema_version}/messages | /model_context_protocol/{schema_version}/messages [POST]
[**model_context_protocol_schema_versions**](ModelContextProtocolApi.md#model_context_protocol_schema_versions) | **GET** /model_context_protocol/schema_versions | /model_context_protocol/schema_versions [GET]
[**model_context_protocol_server_sent_events**](ModelContextProtocolApi.md#model_context_protocol_server_sent_events) | **GET** /model_context_protocol/{schema_version}/sse | /model_context_protocol/{schema_version}/sse [GET]


# **model_context_protocol_messages**
> model_context_protocol_messages(schema_version)

/model_context_protocol/{schema_version}/messages [POST]

depending on the schema version,
for 2024-11-05: this is use to take in the requests and the response will be sent via the SSE endpoint
for 2025-03-26: This will establish the connection, and accept and return events via this endpoint

NOTE: these endpoint are just for DOCUMENTATION!!! do not use(generating will fail because the incoming body is dynamic to support different schema versions)

### Example

* Api Key Authentication (application):

```python
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
    api_instance = pieces_os_client.ModelContextProtocolApi(api_client)
    schema_version = 'schema_version_example' # str | This is a supported schema version IE 2024-11-05 or 2025-03-26

    try:
        # /model_context_protocol/{schema_version}/messages [POST]
        api_instance.model_context_protocol_messages(schema_version)
    except Exception as e:
        print("Exception when calling ModelContextProtocolApi->model_context_protocol_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_version** | **str**| This is a supported schema version IE 2024-11-05 or 2025-03-26 | 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_context_protocol_schema_versions**
> ModelContextProtocolSchemaVersions model_context_protocol_schema_versions()

/model_context_protocol/schema_versions [GET]

This will list all of the supported schema versions for MCP

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.model_context_protocol_schema_versions import ModelContextProtocolSchemaVersions
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
    api_instance = pieces_os_client.ModelContextProtocolApi(api_client)

    try:
        # /model_context_protocol/schema_versions [GET]
        api_response = api_instance.model_context_protocol_schema_versions()
        print("The response of ModelContextProtocolApi->model_context_protocol_schema_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelContextProtocolApi->model_context_protocol_schema_versions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ModelContextProtocolSchemaVersions**](ModelContextProtocolSchemaVersions.md)

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

# **model_context_protocol_server_sent_events**
> model_context_protocol_server_sent_events(schema_version)

/model_context_protocol/{schema_version}/sse [GET]

This is a streamed endpoint that is NOT a websocket however establishes a long running connection for the MCP integration

NOTE: these endpoint are just for DOCUMENTATION!!! do not use(generating will fail because the incoming body is dynamic to support different schema versions)

### Example

* Api Key Authentication (application):

```python
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
    api_instance = pieces_os_client.ModelContextProtocolApi(api_client)
    schema_version = 'schema_version_example' # str | This is a supported schema version IE 2024-11-05 or 2025-03-26

    try:
        # /model_context_protocol/{schema_version}/sse [GET]
        api_instance.model_context_protocol_server_sent_events(schema_version)
    except Exception as e:
        print("Exception when calling ModelContextProtocolApi->model_context_protocol_server_sent_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_version** | **str**| This is a supported schema version IE 2024-11-05 or 2025-03-26 | 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

