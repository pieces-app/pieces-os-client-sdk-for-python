# pieces_os_client.PersonsApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**persons_create_new_person**](PersonsApi.md#persons_create_new_person) | **POST** /persons/create | /persons/create [POST]
[**persons_delete_person**](PersonsApi.md#persons_delete_person) | **POST** /persons/{person}/delete | /persons/{person}/delete [POST]
[**persons_snapshot**](PersonsApi.md#persons_snapshot) | **GET** /persons | /persons [GET]
[**persons_stream_identifiers**](PersonsApi.md#persons_stream_identifiers) | **GET** /persons/stream/identifiers | /persons/stream/identifiers [WS]
[**search_persons**](PersonsApi.md#search_persons) | **POST** /persons/search | /persons/search [POST]


# **persons_create_new_person**
> Person persons_create_new_person(transferables=transferables, seeded_person=seeded_person)

/persons/create [POST]

This will create a new person.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.person import Person
from pieces_os_client.models.seeded_person import SeededPerson
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
    api_instance = pieces_os_client.PersonsApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    seeded_person = pieces_os_client.SeededPerson() # SeededPerson |  (optional)

    try:
        # /persons/create [POST]
        api_response = api_instance.persons_create_new_person(transferables=transferables, seeded_person=seeded_person)
        print("The response of PersonsApi->persons_create_new_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->persons_create_new_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **seeded_person** | [**SeededPerson**](SeededPerson.md)|  | [optional] 

### Return type

[**Person**](Person.md)

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

# **persons_delete_person**
> persons_delete_person(person)

/persons/{person}/delete [POST]

This will delete a specific person.

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
    api_instance = pieces_os_client.PersonsApi(api_client)
    person = 'person_example' # str | This is a uuid that represents a person.

    try:
        # /persons/{person}/delete [POST]
        api_instance.persons_delete_person(person)
    except Exception as e:
        print("Exception when calling PersonsApi->persons_delete_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **str**| This is a uuid that represents a person. | 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **persons_snapshot**
> Persons persons_snapshot(transferables=transferables)

/persons [GET]

This will get a snapshot of all of your people

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.persons import Persons
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
    api_instance = pieces_os_client.PersonsApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /persons [GET]
        api_response = api_instance.persons_snapshot(transferables=transferables)
        print("The response of PersonsApi->persons_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->persons_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Persons**](Persons.md)

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

# **persons_stream_identifiers**
> StreamedIdentifiers persons_stream_identifiers()

/persons/stream/identifiers [WS]

Provides a WebSocket connection that emits changes to your person identifiers (UUIDs).

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
    api_instance = pieces_os_client.PersonsApi(api_client)

    try:
        # /persons/stream/identifiers [WS]
        api_response = api_instance.persons_stream_identifiers()
        print("The response of PersonsApi->persons_stream_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->persons_stream_identifiers: %s\n" % e)
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

# **search_persons**
> SearchedPersons search_persons(transferables=transferables, search_input=search_input)

/persons/search [POST]

This will search your persons for a specific person

note: we will search, name, email, and username

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.search_input import SearchInput
from pieces_os_client.models.searched_persons import SearchedPersons
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
    api_instance = pieces_os_client.PersonsApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    search_input = pieces_os_client.SearchInput() # SearchInput |  (optional)

    try:
        # /persons/search [POST]
        api_response = api_instance.search_persons(transferables=transferables, search_input=search_input)
        print("The response of PersonsApi->search_persons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->search_persons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **search_input** | [**SearchInput**](SearchInput.md)|  | [optional] 

### Return type

[**SearchedPersons**](SearchedPersons.md)

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

