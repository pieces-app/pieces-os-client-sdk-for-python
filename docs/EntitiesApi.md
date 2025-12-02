# pieces_os_client.EntitiesApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entities_create_new_entity**](EntitiesApi.md#entities_create_new_entity) | **POST** /entities/create | /entities/create [POST]
[**entities_delete_specific_entity**](EntitiesApi.md#entities_delete_specific_entity) | **POST** /entities/{entity}/delete | /entities/{entity}/delete [POST]
[**entities_snapshot**](EntitiesApi.md#entities_snapshot) | **GET** /entities | /entities [GET]
[**search_entities**](EntitiesApi.md#search_entities) | **POST** /entities/search | /entities/search [POST]
[**stream_entities_identifiers**](EntitiesApi.md#stream_entities_identifiers) | **GET** /entities/stream/identifiers | /entities/stream/identifiers [WS]


# **entities_create_new_entity**
> Entity entities_create_new_entity(transferables=transferables, seeded_entity=seeded_entity)

/entities/create [POST]

This will create a new entity (organization or team).

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.entity import Entity
from pieces_os_client.models.seeded_entity import SeededEntity
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
    api_instance = pieces_os_client.EntitiesApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    seeded_entity = pieces_os_client.SeededEntity() # SeededEntity |  (optional)

    try:
        # /entities/create [POST]
        api_response = api_instance.entities_create_new_entity(transferables=transferables, seeded_entity=seeded_entity)
        print("The response of EntitiesApi->entities_create_new_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->entities_create_new_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **seeded_entity** | [**SeededEntity**](SeededEntity.md)|  | [optional] 

### Return type

[**Entity**](Entity.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden, we are not allowing creating of an entities via the endpoints |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entities_delete_specific_entity**
> entities_delete_specific_entity(entity)

/entities/{entity}/delete [POST]

This will delete a specific entity.

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
    api_instance = pieces_os_client.EntitiesApi(api_client)
    entity = 'entity_example' # str | This is the uuid of an entity (organization or team).

    try:
        # /entities/{entity}/delete [POST]
        api_instance.entities_delete_specific_entity(entity)
    except Exception as e:
        print("Exception when calling EntitiesApi->entities_delete_specific_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| This is the uuid of an entity (organization or team). | 

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
**403** | Forbidden, we are not allowing deleting of an entities via the endpoints |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entities_snapshot**
> Entities entities_snapshot(transferables=transferables)

/entities [GET]

This will get a snapshot of all your entities.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.entities import Entities
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
    api_instance = pieces_os_client.EntitiesApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /entities [GET]
        api_response = api_instance.entities_snapshot(transferables=transferables)
        print("The response of EntitiesApi->entities_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->entities_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Entities**](Entities.md)

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

# **search_entities**
> SearchedEntities search_entities(transferables=transferables, search_input=search_input)

/entities/search [POST]

This will search your entities for a specific query.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.search_input import SearchInput
from pieces_os_client.models.searched_entities import SearchedEntities
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
    api_instance = pieces_os_client.EntitiesApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    search_input = pieces_os_client.SearchInput() # SearchInput |  (optional)

    try:
        # /entities/search [POST]
        api_response = api_instance.search_entities(transferables=transferables, search_input=search_input)
        print("The response of EntitiesApi->search_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->search_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **search_input** | [**SearchInput**](SearchInput.md)|  | [optional] 

### Return type

[**SearchedEntities**](SearchedEntities.md)

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

# **stream_entities_identifiers**
> StreamedIdentifiers stream_entities_identifiers()

/entities/stream/identifiers [WS]

Provides a WebSocket connection that streams entity identifiers as they are created, updated, or deleted.

### Example

* Api Key Authentication (application):

```python
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
    api_instance = pieces_os_client.EntitiesApi(api_client)

    try:
        # /entities/stream/identifiers [WS]
        api_response = api_instance.stream_entities_identifiers()
        print("The response of EntitiesApi->stream_entities_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->stream_entities_identifiers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StreamedIdentifiers**](StreamedIdentifiers.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

