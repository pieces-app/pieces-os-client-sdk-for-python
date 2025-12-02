# pieces_os_client.EntityApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entities_specific_entity_snapshot**](EntityApi.md#entities_specific_entity_snapshot) | **GET** /entity/{entity} | /entity/{entity} [GET]
[**entity_associate_subscription**](EntityApi.md#entity_associate_subscription) | **POST** /entity/{entity}/subscriptions/associate/{subscription} | /entity/{entity}/subscriptions/associate/{subscription} [POST]
[**entity_associate_user**](EntityApi.md#entity_associate_user) | **POST** /entity/{entity}/users/associate/{user} | /entity/{entity}/users/associate/{user} [POST]
[**entity_disassociate_subscription**](EntityApi.md#entity_disassociate_subscription) | **POST** /entity/{entity}/subscriptions/disassociate/{subscription} | /entity/{entity}/subscriptions/disassociate/{subscription} [POST]
[**entity_disassociate_user**](EntityApi.md#entity_disassociate_user) | **POST** /entity/{entity}/users/disassociate/{user} | /entity/{entity}/users/disassociate/{user} [POST]
[**entity_scores_increment**](EntityApi.md#entity_scores_increment) | **POST** /entity/{entity}/scores/increment | /entity/{entity}/scores/increment [POST]
[**entity_update**](EntityApi.md#entity_update) | **POST** /entity/update | /entity/update [POST]


# **entities_specific_entity_snapshot**
> Entity entities_specific_entity_snapshot(entity, transferables=transferables)

/entity/{entity} [GET]

This will get a snapshot of a specific entity.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.entity import Entity
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
    api_instance = pieces_os_client.EntityApi(api_client)
    entity = 'entity_example' # str | This is the uuid of an entity (organization or team).
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /entity/{entity} [GET]
        api_response = api_instance.entities_specific_entity_snapshot(entity, transferables=transferables)
        print("The response of EntityApi->entities_specific_entity_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->entities_specific_entity_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| This is the uuid of an entity (organization or team). | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Entity**](Entity.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_associate_subscription**
> entity_associate_subscription(entity, subscription, entity_associate_to_subscription_input=entity_associate_to_subscription_input)

/entity/{entity}/subscriptions/associate/{subscription} [POST]

Creates an association between an Entity and a Subscription.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.entity_associate_to_subscription_input import EntityAssociateToSubscriptionInput
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
    api_instance = pieces_os_client.EntityApi(api_client)
    entity = 'entity_example' # str | This is the uuid of an entity (organization or team).
    subscription = 'subscription_example' # str | This is a identifier that is used to identify a specific subscription
    entity_associate_to_subscription_input = pieces_os_client.EntityAssociateToSubscriptionInput() # EntityAssociateToSubscriptionInput |  (optional)

    try:
        # /entity/{entity}/subscriptions/associate/{subscription} [POST]
        api_instance.entity_associate_subscription(entity, subscription, entity_associate_to_subscription_input=entity_associate_to_subscription_input)
    except Exception as e:
        print("Exception when calling EntityApi->entity_associate_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| This is the uuid of an entity (organization or team). | 
 **subscription** | **str**| This is a identifier that is used to identify a specific subscription | 
 **entity_associate_to_subscription_input** | [**EntityAssociateToSubscriptionInput**](EntityAssociateToSubscriptionInput.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_associate_user**
> entity_associate_user(entity, user, entity_associate_to_user_input=entity_associate_to_user_input)

/entity/{entity}/users/associate/{user} [POST]

Creates an association between an Entity and a User.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.entity_associate_to_user_input import EntityAssociateToUserInput
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
    api_instance = pieces_os_client.EntityApi(api_client)
    entity = 'entity_example' # str | This is the uuid of an entity (organization or team).
    user = '497f6eca-6276-4993-bfeb-53cbbbba6f08' # str | The id (uuid) for a specific user.
    entity_associate_to_user_input = pieces_os_client.EntityAssociateToUserInput() # EntityAssociateToUserInput |  (optional)

    try:
        # /entity/{entity}/users/associate/{user} [POST]
        api_instance.entity_associate_user(entity, user, entity_associate_to_user_input=entity_associate_to_user_input)
    except Exception as e:
        print("Exception when calling EntityApi->entity_associate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| This is the uuid of an entity (organization or team). | 
 **user** | **str**| The id (uuid) for a specific user. | 
 **entity_associate_to_user_input** | [**EntityAssociateToUserInput**](EntityAssociateToUserInput.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_disassociate_subscription**
> entity_disassociate_subscription(entity, subscription)

/entity/{entity}/subscriptions/disassociate/{subscription} [POST]

Removes an association between an Entity and a Subscription.

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
    api_instance = pieces_os_client.EntityApi(api_client)
    entity = 'entity_example' # str | This is the uuid of an entity (organization or team).
    subscription = 'subscription_example' # str | This is a identifier that is used to identify a specific subscription

    try:
        # /entity/{entity}/subscriptions/disassociate/{subscription} [POST]
        api_instance.entity_disassociate_subscription(entity, subscription)
    except Exception as e:
        print("Exception when calling EntityApi->entity_disassociate_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| This is the uuid of an entity (organization or team). | 
 **subscription** | **str**| This is a identifier that is used to identify a specific subscription | 

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

# **entity_disassociate_user**
> entity_disassociate_user(entity, user)

/entity/{entity}/users/disassociate/{user} [POST]

Removes an association between an Entity and a User.

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
    api_instance = pieces_os_client.EntityApi(api_client)
    entity = 'entity_example' # str | This is the uuid of an entity (organization or team).
    user = '497f6eca-6276-4993-bfeb-53cbbbba6f08' # str | The id (uuid) for a specific user.

    try:
        # /entity/{entity}/users/disassociate/{user} [POST]
        api_instance.entity_disassociate_user(entity, user)
    except Exception as e:
        print("Exception when calling EntityApi->entity_disassociate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| This is the uuid of an entity (organization or team). | 
 **user** | **str**| The id (uuid) for a specific user. | 

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

# **entity_scores_increment**
> entity_scores_increment(entity, seeded_score_increment=seeded_score_increment)

/entity/{entity}/scores/increment [POST]

This will take in a SeededScoreIncrement and will increment the material relative to the incoming body.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.seeded_score_increment import SeededScoreIncrement
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
    api_instance = pieces_os_client.EntityApi(api_client)
    entity = 'entity_example' # str | This is the uuid of an entity (organization or team).
    seeded_score_increment = pieces_os_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # /entity/{entity}/scores/increment [POST]
        api_instance.entity_scores_increment(entity, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling EntityApi->entity_scores_increment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| This is the uuid of an entity (organization or team). | 
 **seeded_score_increment** | [**SeededScoreIncrement**](SeededScoreIncrement.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entity_update**
> Entity entity_update(entity, transferables=transferables)

/entity/update [POST]

This will update a specific entity.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.entity import Entity
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
    api_instance = pieces_os_client.EntityApi(api_client)
    entity = pieces_os_client.Entity() # Entity | 
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /entity/update [POST]
        api_response = api_instance.entity_update(entity, transferables=transferables)
        print("The response of EntityApi->entity_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->entity_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | [**Entity**](Entity.md)|  | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

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
**403** | Forbidden, we are not allowing updating of an entities via the endpoints |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

