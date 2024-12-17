# pieces_os_client.ConnectorApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect**](ConnectorApi.md#connect) | **POST** /connect | /connect [POST]
[**intention**](ConnectorApi.md#intention) | **POST** /{application}/intention | /{application}/intention [POST]
[**onboarded**](ConnectorApi.md#onboarded) | **POST** /{application}/onboarded | /onboarded [POST]
[**react**](ConnectorApi.md#react) | **POST** /{application}/reaction | /{application}/reaction [POST]
[**suggest**](ConnectorApi.md#suggest) | **POST** /{application}/suggestion | /{application}/suggestion [POST]
[**track**](ConnectorApi.md#track) | **POST** /{application}/track | /{application}/track [POST]


# **connect**
> Context connect(seeded_connector_connection=seeded_connector_connection)

/connect [POST]

Abstracts a bootup/connection for a specific context.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.context import Context
from pieces_os_client.models.seeded_connector_connection import SeededConnectorConnection
from pieces_os_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:1000
# See configuration.py for a list of all supported configuration parameters.
configuration = pieces_os_client.Configuration(
    host = "http://localhost:1000"
)


# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.ConnectorApi(api_client)
    seeded_connector_connection = pieces_os_client.SeededConnectorConnection() # SeededConnectorConnection |  (optional)

    try:
        # /connect [POST]
        api_response = api_instance.connect(seeded_connector_connection=seeded_connector_connection)
        print("The response of ConnectorApi->connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->connect: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_connector_connection** | [**SeededConnectorConnection**](SeededConnectorConnection.md)|  | [optional] 

### Return type

[**Context**](Context.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request, Application Failed to connect, Please ensure this is a valid integration. This happens in the case a developer provides and incorrect {application} (applicationId) within the route that doest match a preregisterd integration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intention**
> str intention(application, seeded_connector_asset=seeded_connector_asset)

/{application}/intention [POST]

Allows you to send a SeededAsset for future comparison.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.seeded_connector_asset import SeededConnectorAsset
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
    api_instance = pieces_os_client.ConnectorApi(api_client)
    application = 'application_example' # str | 
    seeded_connector_asset = pieces_os_client.SeededConnectorAsset() # SeededConnectorAsset |  (optional)

    try:
        # /{application}/intention [POST]
        api_response = api_instance.intention(application, seeded_connector_asset=seeded_connector_asset)
        print("The response of ConnectorApi->intention:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->intention: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**|  | 
 **seeded_connector_asset** | [**SeededConnectorAsset**](SeededConnectorAsset.md)|  | [optional] 

### Return type

**str**

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request, Application Failed to connect, Please ensure this is a valid integration. This happens in the case a developer provides and incorrect {application} (applicationId) within the route that doest match a preregisterd integration. |  -  |
**401** | Unauthorized, you will get this in the case that you are trying to ping Pieces_OS but havnt connected yet.\&quot;/connect was not called for your application.\&quot; |  -  |
**500** | Internal Server Error:  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onboarded**
> str onboarded(application, body=body)

/onboarded [POST]

A central endpoint to manage updates to the onboarding process.

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
    api_instance = pieces_os_client.ConnectorApi(api_client)
    application = 'application_example' # str | This is a uuid that represents an application
    body = True # bool | Whether or not that application has been onboarded. (optional)

    try:
        # /onboarded [POST]
        api_response = api_instance.onboarded(application, body=body)
        print("The response of ConnectorApi->onboarded:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->onboarded: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| This is a uuid that represents an application | 
 **body** | **bool**| Whether or not that application has been onboarded. | [optional] 

### Return type

**str**

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK, This will just return a string of \&quot;OK\&quot;. |  -  |
**400** | Bad Request, Application Failed to connect, Please ensure this is a valid integration. This happens in the case a developer provides and incorrect {application} (applicationId) within the route that doest match a preregisterd integration. |  -  |
**401** | Unauthorized, you will get this in the case that you are trying to ping Pieces_OS but havnt connected yet.\&quot;/connect was not called for your application.\&quot; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **react**
> str react(application, reaction=reaction)

/{application}/reaction [POST]

This will respond to the output generated by the /suggest endpoint.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.reaction import Reaction
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
    api_instance = pieces_os_client.ConnectorApi(api_client)
    application = 'application_example' # str | 
    reaction = pieces_os_client.Reaction() # Reaction | ** This body will need to be modified. (optional)

    try:
        # /{application}/reaction [POST]
        api_response = api_instance.react(application, reaction=reaction)
        print("The response of ConnectorApi->react:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->react: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**|  | 
 **reaction** | [**Reaction**](Reaction.md)| ** This body will need to be modified. | [optional] 

### Return type

**str**

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This string will either (1) be a string of the AssetUid or (2) will be a generic string of &#39;OK&#39; if the asset was not saved and &#39;OK&#39; if the result was just used to send information about the a suggested reuse. |  -  |
**400** | Bad Request, Application Failed to connect, Please ensure this is a valid integration. This happens in the case a developer provides and incorrect {application} (applicationId) within the route that doest match a preregisterd integration. |  -  |
**401** | Unauthorized, you will get this in the case that you are trying to ping Pieces_OS but havnt connected yet.\&quot;/connect was not called for your application.\&quot; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggest**
> Suggestion suggest(application, seeded_connector_creation=seeded_connector_creation)

/{application}/suggestion [POST]

Invoked whenever a code snippet is copied from an integration. For instance, if a JetBrains user copies code, this endpoint can be called to assess whether to suggest reusing a piece (if reuse is true, the endpoint provides assets that the user may consider using), saving the code snippet, or taking no action.   **Note: This endpoint could potentially accept a SeededFormat for the request body if required.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.seeded_connector_creation import SeededConnectorCreation
from pieces_os_client.models.suggestion import Suggestion
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
    api_instance = pieces_os_client.ConnectorApi(api_client)
    application = 'application_example' # str | 
    seeded_connector_creation = pieces_os_client.SeededConnectorCreation() # SeededConnectorCreation | This is the Snippet that we will compare to all the saved assets to determine what we want to do with it! (optional)

    try:
        # /{application}/suggestion [POST]
        api_response = api_instance.suggest(application, seeded_connector_creation=seeded_connector_creation)
        print("The response of ConnectorApi->suggest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->suggest: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**|  | 
 **seeded_connector_creation** | [**SeededConnectorCreation**](SeededConnectorCreation.md)| This is the Snippet that we will compare to all the saved assets to determine what we want to do with it! | [optional] 

### Return type

[**Suggestion**](Suggestion.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request, Application Failed to connect, Please ensure this is a valid integration. This happens in the case a developer provides and incorrect {application} (applicationId) within the route that doest match a preregisterd integration. |  -  |
**401** | Unauthorized, you will get this in the case that you are trying to ping Pieces_OS but havnt connected yet.\&quot;/connect was not called for your application.\&quot; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track**
> str track(application, seeded_connector_tracking=seeded_connector_tracking)

/{application}/track [POST]

Abstracts the process of packaging segments on a per-context basis.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.seeded_connector_tracking import SeededConnectorTracking
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
    api_instance = pieces_os_client.ConnectorApi(api_client)
    application = 'application_example' # str | This is a uuid that represents an application
    seeded_connector_tracking = pieces_os_client.SeededConnectorTracking() # SeededConnectorTracking | The body is able to take in several properties  (optional)

    try:
        # /{application}/track [POST]
        api_response = api_instance.track(application, seeded_connector_tracking=seeded_connector_tracking)
        print("The response of ConnectorApi->track:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->track: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| This is a uuid that represents an application | 
 **seeded_connector_tracking** | [**SeededConnectorTracking**](SeededConnectorTracking.md)| The body is able to take in several properties  | [optional] 

### Return type

**str**

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK, This will jsut return a string of \&quot;OK\&quot;. |  -  |
**400** | Bad Request, Application Failed to connect, Please ensure this is a valid integration. This happens in the case a developer provides and incorrect {application} (applicationId) within the route that doest match a preregisterd integration. |  -  |
**401** | Unauthorized, you will get this in the case that you are trying to ping Pieces_OS but havnt connected yet.\&quot;/connect was not called for your application.\&quot; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

