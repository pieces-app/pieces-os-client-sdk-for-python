# pieces_os_client.ApplicationsApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_external_related**](ApplicationsApi.md#applications_external_related) | **GET** /applications/external/related | /applications/external/related [GET]
[**applications_external_snapshot**](ApplicationsApi.md#applications_external_snapshot) | **GET** /applications/external | /applications/external [GET]
[**applications_register**](ApplicationsApi.md#applications_register) | **POST** /applications/register | /applications/register [POST]
[**applications_session_close**](ApplicationsApi.md#applications_session_close) | **POST** /applications/session/close | /applications/session/close [POST]
[**applications_session_open**](ApplicationsApi.md#applications_session_open) | **POST** /applications/session/open | /applications/session/open [POST]
[**applications_session_snapshot**](ApplicationsApi.md#applications_session_snapshot) | **GET** /applications/sessions/{session} | /applications/sessions/{session} [GET]
[**applications_snapshot**](ApplicationsApi.md#applications_snapshot) | **GET** /applications | /applications [GET]
[**applications_specific_application_snapshot**](ApplicationsApi.md#applications_specific_application_snapshot) | **GET** /applications/{application} | /applications/{application} [GET]
[**applications_usage_engagement_interaction**](ApplicationsApi.md#applications_usage_engagement_interaction) | **POST** /applications/usage/engagement/interaction | /applications/usage/engagement/interaction [POST] Scoped to Apps
[**applications_usage_engagement_keyboard**](ApplicationsApi.md#applications_usage_engagement_keyboard) | **POST** /applications/usage/engagement/keyboard | /applications/usage/engagement/keyboard [POST] Scoped to Apps
[**applications_usage_installation**](ApplicationsApi.md#applications_usage_installation) | **POST** /applications/usage/installation | /applications/usage/installation [POST]
[**post_applications_usage_updated**](ApplicationsApi.md#post_applications_usage_updated) | **POST** /applications/usage/updated | /applications/usage/updated [POST]


# **applications_external_related**
> DetectedExternalApplications applications_external_related()

/applications/external/related [GET]

Retrieves a list of external applications installed on the user's machine that have potential integrations with Pieces, including those not yet installed by the user and those anticipated to be supported in the future.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.detected_external_applications import DetectedExternalApplications
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)

    try:
        # /applications/external/related [GET]
        api_response = api_instance.applications_external_related()
        print("The response of ApplicationsApi->applications_external_related:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_external_related: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**DetectedExternalApplications**](DetectedExternalApplications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_external_snapshot**
> DetectedExternalApplications applications_external_snapshot()

/applications/external [GET]

Provides a snapshot of all external applications detected on the user's machine, such as Microsoft Teams classic, Google Chat, Obsidian, etc.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.detected_external_applications import DetectedExternalApplications
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)

    try:
        # /applications/external [GET]
        api_response = api_instance.applications_external_snapshot()
        print("The response of ApplicationsApi->applications_external_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_external_snapshot: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**DetectedExternalApplications**](DetectedExternalApplications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_register**
> Application applications_register(application=application)

/applications/register [POST]

Registers a new application within the Pieces ecosystem.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.application import Application
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)
    application = pieces_os_client.Application() # Application | This will accept a application. (optional)

    try:
        # /applications/register [POST]
        api_response = api_instance.applications_register(application=application)
        print("The response of ApplicationsApi->applications_register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_register: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | [**Application**](Application.md)| This will accept a application. | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_session_close**
> Session applications_session_close(body=body)

/applications/session/close [POST]

Closes an active session, identified by a session UUID, marking the end of the user's current interaction with the Pieces application.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.session import Session
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)
    body = 'body_example' # str | This will accept a required session uuid. (optional)

    try:
        # /applications/session/close [POST]
        api_response = api_instance.applications_session_close(body=body)
        print("The response of ApplicationsApi->applications_session_close:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_session_close: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| This will accept a required session uuid. | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_session_open**
> Session applications_session_open()

/applications/session/open [POST]

Initiates a new session, marking the start of a user's interaction with the Pieces application.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.session import Session
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)

    try:
        # /applications/session/open [POST]
        api_response = api_instance.applications_session_open()
        print("The response of ApplicationsApi->applications_session_open:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_session_open: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_session_snapshot**
> Session applications_session_snapshot(session)

/applications/sessions/{session} [GET]

Fetches detailed information about a specific session, identified by a session UUID, including application usage and engagement data.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.session import Session
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)
    session = 'session_example' # str | This is a uuid that points to a session.

    try:
        # /applications/sessions/{session} [GET]
        api_response = api_instance.applications_session_snapshot(session)
        print("The response of ApplicationsApi->applications_session_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_session_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | **str**| This is a uuid that points to a session. | 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_snapshot**
> Applications applications_snapshot()

/applications [GET]

Retrieves a comprehensive overview of all applications tracked by the Pieces system, including status, version, and engagement metrics.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.applications import Applications
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)

    try:
        # /applications [GET]
        api_response = api_instance.applications_snapshot()
        print("The response of ApplicationsApi->applications_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_snapshot: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Applications**](Applications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_specific_application_snapshot**
> Application applications_specific_application_snapshot(application)

/applications/{application} [GET]

Obtains a snapshot with information about a specific application, identified by its UUID.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.application import Application
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)
    application = 'application_example' # str | This is a uuid that represents an application

    try:
        # /applications/{application} [GET]
        api_response = api_instance.applications_specific_application_snapshot(application)
        print("The response of ApplicationsApi->applications_specific_application_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_specific_application_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| This is a uuid that represents an application | 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_usage_engagement_interaction**
> TrackedInteractionEvent applications_usage_engagement_interaction(seeded_tracked_interaction_event=seeded_tracked_interaction_event)

/applications/usage/engagement/interaction [POST] Scoped to Apps

Records user interaction events within applications, such as clicks or taps, to analyze engagement patterns and user behavior.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.seeded_tracked_interaction_event import SeededTrackedInteractionEvent
from pieces_os_client.models.tracked_interaction_event import TrackedInteractionEvent
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)
    seeded_tracked_interaction_event = pieces_os_client.SeededTrackedInteractionEvent() # SeededTrackedInteractionEvent |  (optional)

    try:
        # /applications/usage/engagement/interaction [POST] Scoped to Apps
        api_response = api_instance.applications_usage_engagement_interaction(seeded_tracked_interaction_event=seeded_tracked_interaction_event)
        print("The response of ApplicationsApi->applications_usage_engagement_interaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_usage_engagement_interaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_tracked_interaction_event** | [**SeededTrackedInteractionEvent**](SeededTrackedInteractionEvent.md)|  | [optional] 

### Return type

[**TrackedInteractionEvent**](TrackedInteractionEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_usage_engagement_keyboard**
> TrackedKeyboardEvent applications_usage_engagement_keyboard(seeded_tracked_keyboard_event=seeded_tracked_keyboard_event)

/applications/usage/engagement/keyboard [POST] Scoped to Apps

Captures keyboard interaction events, including shortcuts, within applications to monitor user engagement and productivity enhancements.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.seeded_tracked_keyboard_event import SeededTrackedKeyboardEvent
from pieces_os_client.models.tracked_keyboard_event import TrackedKeyboardEvent
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)
    seeded_tracked_keyboard_event = pieces_os_client.SeededTrackedKeyboardEvent() # SeededTrackedKeyboardEvent |  (optional)

    try:
        # /applications/usage/engagement/keyboard [POST] Scoped to Apps
        api_response = api_instance.applications_usage_engagement_keyboard(seeded_tracked_keyboard_event=seeded_tracked_keyboard_event)
        print("The response of ApplicationsApi->applications_usage_engagement_keyboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_usage_engagement_keyboard: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_tracked_keyboard_event** | [**SeededTrackedKeyboardEvent**](SeededTrackedKeyboardEvent.md)|  | [optional] 

### Return type

[**TrackedKeyboardEvent**](TrackedKeyboardEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_usage_installation**
> applications_usage_installation(tracked_application_install=tracked_application_install)

/applications/usage/installation [POST]

Logs the installation events of the Pieces application.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.tracked_application_install import TrackedApplicationInstall
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)
    tracked_application_install = pieces_os_client.TrackedApplicationInstall() # TrackedApplicationInstall |  (optional)

    try:
        # /applications/usage/installation [POST]
        api_instance.applications_usage_installation(tracked_application_install=tracked_application_install)
    except Exception as e:
        print("Exception when calling ApplicationsApi->applications_usage_installation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracked_application_install** | [**TrackedApplicationInstall**](TrackedApplicationInstall.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_applications_usage_updated**
> post_applications_usage_updated(tracked_application_update=tracked_application_update)

/applications/usage/updated [POST]

Tracks updates to the Pieces application, including version changes.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.tracked_application_update import TrackedApplicationUpdate
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
    api_instance = pieces_os_client.ApplicationsApi(api_client)
    tracked_application_update = pieces_os_client.TrackedApplicationUpdate() # TrackedApplicationUpdate | Sending over the previous application version, the current version, and the user. (optional)

    try:
        # /applications/usage/updated [POST]
        api_instance.post_applications_usage_updated(tracked_application_update=tracked_application_update)
    except Exception as e:
        print("Exception when calling ApplicationsApi->post_applications_usage_updated: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracked_application_update** | [**TrackedApplicationUpdate**](TrackedApplicationUpdate.md)| Sending over the previous application version, the current version, and the user. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

