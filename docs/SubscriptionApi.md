# pieces_os_client.SubscriptionApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_associate_entity**](SubscriptionApi.md#subscription_associate_entity) | **POST** /subscription/{subscription}/entities/associate/{entity} | /subscription/{subscription}/entities/associate/{entity} [POST]
[**subscription_disassociate_entity**](SubscriptionApi.md#subscription_disassociate_entity) | **POST** /subscription/{subscription}/entities/disassociate/{entity} | /subscription/{subscription}/entities/disassociate/{entity} [POST]
[**subscription_scores_increment**](SubscriptionApi.md#subscription_scores_increment) | **POST** /subscription/{subscription}/scores/increment | /subscription/{subscription}/scores/increment [POST]
[**subscription_update**](SubscriptionApi.md#subscription_update) | **POST** /subscription/update | /subscription/update [POST]
[**subscriptions_specific_subscription_snapshot**](SubscriptionApi.md#subscriptions_specific_subscription_snapshot) | **GET** /subscription/{subscription} | /subscription/{subscription} [GET]


# **subscription_associate_entity**
> subscription_associate_entity(subscription, entity, entity_associate_to_subscription_input=entity_associate_to_subscription_input)

/subscription/{subscription}/entities/associate/{entity} [POST]

Creates an association between a Subscription and an Entity.

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
    api_instance = pieces_os_client.SubscriptionApi(api_client)
    subscription = 'subscription_example' # str | This is a identifier that is used to identify a specific subscription
    entity = 'entity_example' # str | This is the uuid of an entity (organization or team).
    entity_associate_to_subscription_input = pieces_os_client.EntityAssociateToSubscriptionInput() # EntityAssociateToSubscriptionInput |  (optional)

    try:
        # /subscription/{subscription}/entities/associate/{entity} [POST]
        api_instance.subscription_associate_entity(subscription, entity, entity_associate_to_subscription_input=entity_associate_to_subscription_input)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscription_associate_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | **str**| This is a identifier that is used to identify a specific subscription | 
 **entity** | **str**| This is the uuid of an entity (organization or team). | 
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

# **subscription_disassociate_entity**
> subscription_disassociate_entity(subscription, entity)

/subscription/{subscription}/entities/disassociate/{entity} [POST]

Removes an association between a Subscription and an Entity.

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
    api_instance = pieces_os_client.SubscriptionApi(api_client)
    subscription = 'subscription_example' # str | This is a identifier that is used to identify a specific subscription
    entity = 'entity_example' # str | This is the uuid of an entity (organization or team).

    try:
        # /subscription/{subscription}/entities/disassociate/{entity} [POST]
        api_instance.subscription_disassociate_entity(subscription, entity)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscription_disassociate_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | **str**| This is a identifier that is used to identify a specific subscription | 
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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_scores_increment**
> subscription_scores_increment(subscription, seeded_score_increment=seeded_score_increment)

/subscription/{subscription}/scores/increment [POST]

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
    api_instance = pieces_os_client.SubscriptionApi(api_client)
    subscription = 'subscription_example' # str | This is a identifier that is used to identify a specific subscription
    seeded_score_increment = pieces_os_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # /subscription/{subscription}/scores/increment [POST]
        api_instance.subscription_scores_increment(subscription, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscription_scores_increment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | **str**| This is a identifier that is used to identify a specific subscription | 
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

# **subscription_update**
> Subscription subscription_update(transferables=transferables, subscription=subscription)

/subscription/update [POST]

This will update a specific subscription.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.subscription import Subscription
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
    api_instance = pieces_os_client.SubscriptionApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    subscription = pieces_os_client.Subscription() # Subscription |  (optional)

    try:
        # /subscription/update [POST]
        api_response = api_instance.subscription_update(transferables=transferables, subscription=subscription)
        print("The response of SubscriptionApi->subscription_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscription_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **subscription** | [**Subscription**](Subscription.md)|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

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

# **subscriptions_specific_subscription_snapshot**
> Subscription subscriptions_specific_subscription_snapshot(subscription, transferables=transferables)

/subscription/{subscription} [GET]

This will get a specific subscription.

### Example

* Api Key Authentication (application):

```python
import pieces_os_client
from pieces_os_client.models.subscription import Subscription
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
    api_instance = pieces_os_client.SubscriptionApi(api_client)
    subscription = 'subscription_example' # str | This is a identifier that is used to identify a specific subscription
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /subscription/{subscription} [GET]
        api_response = api_instance.subscriptions_specific_subscription_snapshot(subscription, transferables=transferables)
        print("The response of SubscriptionApi->subscriptions_specific_subscription_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_specific_subscription_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | **str**| This is a identifier that is used to identify a specific subscription | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**410** | Subscription not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

