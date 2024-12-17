# pieces_os_client.OSApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**link_provider**](OSApi.md#link_provider) | **POST** /os/link_provider | /os/link_provider [POST]
[**os_applet_launch**](OSApi.md#os_applet_launch) | **POST** /os/applet/launch | /os/applet/launch [POST]
[**os_applet_restart**](OSApi.md#os_applet_restart) | **POST** /os/applet/restart | /os/applet/restart [POST]
[**os_applet_terminate**](OSApi.md#os_applet_terminate) | **POST** /os/applet/terminate | /os/applet/terminate [POST]
[**os_browser_url_open**](OSApi.md#os_browser_url_open) | **POST** /os/browser/url/open | /os/browser/url/open [POST]
[**os_device_information**](OSApi.md#os_device_information) | **GET** /os/device/information | /os/device/information [GET]
[**os_filesystem_file_open**](OSApi.md#os_filesystem_file_open) | **POST** /os/filesystem/file/open | /os/filesystem/file/open [POST]
[**os_filesystem_file_read_streamed**](OSApi.md#os_filesystem_file_read_streamed) | **GET** /os/filesystem/file/read/streamed | /os/filesystem/file/read/streamed [WS]
[**os_filesystem_path_verify**](OSApi.md#os_filesystem_path_verify) | **POST** /os/filesystem/path/verify | /os/filesystem/path/verify [POST]
[**os_filesystem_pick_files**](OSApi.md#os_filesystem_pick_files) | **POST** /os/filesystem/files/pick | /os/filesystem/files/pick [POST]
[**os_filesystem_pick_folders**](OSApi.md#os_filesystem_pick_folders) | **POST** /os/filesystem/folders/pick | /os/filesystem/folders/pick [POST]
[**os_memory_optimize**](OSApi.md#os_memory_optimize) | **POST** /os/memory/optimize | /os/memory/optimize [POST]
[**os_permissions**](OSApi.md#os_permissions) | **GET** /os/permissions | /os/permissions [GET]
[**os_permissions_request**](OSApi.md#os_permissions_request) | **POST** /os/permissions/request | /os/permissions/request [POST]
[**os_restart**](OSApi.md#os_restart) | **GET** /os/restart | Your GET endpoint
[**os_settings_snapshot**](OSApi.md#os_settings_snapshot) | **GET** /os/settings | /os/settings [GET]
[**os_settings_stream**](OSApi.md#os_settings_stream) | **GET** /os/settings/stream | /os/settings/stream [WS]
[**os_settings_update**](OSApi.md#os_settings_update) | **POST** /os/settings/update | /os/settings/update [POST]
[**os_terminate**](OSApi.md#os_terminate) | **POST** /os/terminate | /os/terminate [POST]
[**os_update_check**](OSApi.md#os_update_check) | **POST** /os/update/check | /os/update/check [POST]
[**os_update_check_stream**](OSApi.md#os_update_check_stream) | **GET** /os/update/check/stream | /os/update/check/stream [WS]
[**sign_into_os**](OSApi.md#sign_into_os) | **POST** /os/sign_in | 
[**sign_out_of_os**](OSApi.md#sign_out_of_os) | **POST** /os/sign_out | /os/sign_out [POST]


# **link_provider**
> ReturnedUserProfile link_provider(seeded_external_provider=seeded_external_provider)

/os/link_provider [POST]

This will link an external provider to your current auth0 account.  Will throw errors if your user is not signed in.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.returned_user_profile import ReturnedUserProfile
from pieces_os_client.models.seeded_external_provider import SeededExternalProvider
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
    api_instance = pieces_os_client.OSApi(api_client)
    seeded_external_provider = pieces_os_client.SeededExternalProvider() # SeededExternalProvider |  (optional)

    try:
        # /os/link_provider [POST]
        api_response = api_instance.link_provider(seeded_external_provider=seeded_external_provider)
        print("The response of OSApi->link_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->link_provider: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_external_provider** | [**SeededExternalProvider**](SeededExternalProvider.md)|  | [optional] 

### Return type

[**ReturnedUserProfile**](ReturnedUserProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized, this means your user is not authenticated |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_applet_launch**
> ActiveOSServerApplet os_applet_launch(inactive_os_server_applet=inactive_os_server_applet)

/os/applet/launch [POST]

This will attempt to launch(serve) a micro_application. If one is already spun up we will just return the port number. TODO: take in an application and return a port number at minimum.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.active_os_server_applet import ActiveOSServerApplet
from pieces_os_client.models.inactive_os_server_applet import InactiveOSServerApplet
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
    api_instance = pieces_os_client.OSApi(api_client)
    inactive_os_server_applet = pieces_os_client.InactiveOSServerApplet() # InactiveOSServerApplet |  (optional)

    try:
        # /os/applet/launch [POST]
        api_response = api_instance.os_applet_launch(inactive_os_server_applet=inactive_os_server_applet)
        print("The response of OSApi->os_applet_launch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_applet_launch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inactive_os_server_applet** | [**InactiveOSServerApplet**](InactiveOSServerApplet.md)|  | [optional] 

### Return type

[**ActiveOSServerApplet**](ActiveOSServerApplet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_applet_restart**
> ActiveOSServerApplet os_applet_restart(inactive_os_server_applet=inactive_os_server_applet)

/os/applet/restart [POST]

This will attempt to restart a micro_application.(this will shut down the copilot and then rehost it)

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.active_os_server_applet import ActiveOSServerApplet
from pieces_os_client.models.inactive_os_server_applet import InactiveOSServerApplet
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
    api_instance = pieces_os_client.OSApi(api_client)
    inactive_os_server_applet = pieces_os_client.InactiveOSServerApplet() # InactiveOSServerApplet |  (optional)

    try:
        # /os/applet/restart [POST]
        api_response = api_instance.os_applet_restart(inactive_os_server_applet=inactive_os_server_applet)
        print("The response of OSApi->os_applet_restart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_applet_restart: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inactive_os_server_applet** | [**InactiveOSServerApplet**](InactiveOSServerApplet.md)|  | [optional] 

### Return type

[**ActiveOSServerApplet**](ActiveOSServerApplet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_applet_terminate**
> os_applet_terminate(terminating_os_server_applet=terminating_os_server_applet)

/os/applet/terminate [POST]

This will attempt to shutdown or terminate a specified micro_application.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.terminating_os_server_applet import TerminatingOSServerApplet
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
    api_instance = pieces_os_client.OSApi(api_client)
    terminating_os_server_applet = pieces_os_client.TerminatingOSServerApplet() # TerminatingOSServerApplet |  (optional)

    try:
        # /os/applet/terminate [POST]
        api_instance.os_applet_terminate(terminating_os_server_applet=terminating_os_server_applet)
    except Exception as e:
        print("Exception when calling OSApi->os_applet_terminate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminating_os_server_applet** | [**TerminatingOSServerApplet**](TerminatingOSServerApplet.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_browser_url_open**
> os_browser_url_open(body=body)

/os/browser/url/open [POST]

This will accept a url and launch this in an external browser.

### Example

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


# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.OSApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # /os/browser/url/open [POST]
        api_instance.os_browser_url_open(body=body)
    except Exception as e:
        print("Exception when calling OSApi->os_browser_url_open: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_device_information**
> OSDeviceInformationReturnable os_device_information()

/os/device/information [GET]

This will get information related to your specific device.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.os_device_information_returnable import OSDeviceInformationReturnable
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
    api_instance = pieces_os_client.OSApi(api_client)

    try:
        # /os/device/information [GET]
        api_response = api_instance.os_device_information()
        print("The response of OSApi->os_device_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_device_information: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**OSDeviceInformationReturnable**](OSDeviceInformationReturnable.md)

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

# **os_filesystem_file_open**
> os_filesystem_file_open(body=body)

/os/filesystem/file/open [POST]

This will accept a path and will launch a path in a given finder/file explorer window  note: TODO in the future add an endpoint for open/in || open/with (browser,files,...etc)       && if so we will want /os/open_with/file

### Example

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


# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.OSApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # /os/filesystem/file/open [POST]
        api_instance.os_filesystem_file_open(body=body)
    except Exception as e:
        print("Exception when calling OSApi->os_filesystem_file_open: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_filesystem_file_read_streamed**
> OSFileStreamingRead os_filesystem_file_read_streamed(os_file_streaming_read_attempt=os_file_streaming_read_attempt)

/os/filesystem/file/read/streamed [WS]

This will stream(via a WS the contents of a file back to the client, given a file, it will read the contents and return to the client.  NOTE: will NOT support relative paths. only ABSOLUTE paths. NOTE: needs to be a File.(will not stream a folder) NOTE: we might want to put a limit on the size of the file(IE no more than a GB or something like that??) TODO: would be nice to cancel stream NOTE: for v2 we could have two query params i.e. find which could take in a relative path and or file name and        the other could be compress i.e. streaming a gzip vs the raw bytes..        the caveat here would be mack would need to decompress em.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.os_file_streaming_read import OSFileStreamingRead
from pieces_os_client.models.os_file_streaming_read_attempt import OSFileStreamingReadAttempt
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
    api_instance = pieces_os_client.OSApi(api_client)
    os_file_streaming_read_attempt = pieces_os_client.OSFileStreamingReadAttempt() # OSFileStreamingReadAttempt |  (optional)

    try:
        # /os/filesystem/file/read/streamed [WS]
        api_response = api_instance.os_filesystem_file_read_streamed(os_file_streaming_read_attempt=os_file_streaming_read_attempt)
        print("The response of OSApi->os_filesystem_file_read_streamed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_filesystem_file_read_streamed: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_file_streaming_read_attempt** | [**OSFileStreamingReadAttempt**](OSFileStreamingReadAttempt.md)|  | [optional] 

### Return type

[**OSFileStreamingRead**](OSFileStreamingRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_filesystem_path_verify**
> VerifiedOSFilesystemPath os_filesystem_path_verify(body=body)

/os/filesystem/path/verify [POST]

This will determine in a given path is a file/a directory or invalid.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.verified_os_filesystem_path import VerifiedOSFilesystemPath
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
    api_instance = pieces_os_client.OSApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # /os/filesystem/path/verify [POST]
        api_response = api_instance.os_filesystem_path_verify(body=body)
        print("The response of OSApi->os_filesystem_path_verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_filesystem_path_verify: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

[**VerifiedOSFilesystemPath**](VerifiedOSFilesystemPath.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_filesystem_pick_files**
> List[str] os_filesystem_pick_files(file_picker_input=file_picker_input)

/os/filesystem/files/pick [POST]

This will trigger a filer picker and return the string paths of the files that were selected.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.file_picker_input import FilePickerInput
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
    api_instance = pieces_os_client.OSApi(api_client)
    file_picker_input = pieces_os_client.FilePickerInput() # FilePickerInput |  (optional)

    try:
        # /os/filesystem/files/pick [POST]
        api_response = api_instance.os_filesystem_pick_files(file_picker_input=file_picker_input)
        print("The response of OSApi->os_filesystem_pick_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_filesystem_pick_files: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_picker_input** | [**FilePickerInput**](FilePickerInput.md)|  | [optional] 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_filesystem_pick_folders**
> List[str] os_filesystem_pick_folders()

/os/filesystem/folders/pick [POST]

This will trigger a folder picker and return the string paths of the folders that were selected.

### Example

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


# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.OSApi(api_client)

    try:
        # /os/filesystem/folders/pick [POST]
        api_response = api_instance.os_filesystem_pick_folders()
        print("The response of OSApi->os_filesystem_pick_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_filesystem_pick_folders: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **os_memory_optimize**
> os_memory_optimize()

/os/memory/optimize [POST]

This will optimize memory across PiecesOS.(TODO in the future might want to accept a body, so this will be a POST)

### Example

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


# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.OSApi(api_client)

    try:
        # /os/memory/optimize [POST]
        api_instance.os_memory_optimize()
    except Exception as e:
        print("Exception when calling OSApi->os_memory_optimize: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_permissions**
> OSPermissions os_permissions()

/os/permissions [GET]

This will only work on Macos and Windows.  And will get the permissions of the user's local machine w/ regard to anything needed to effectively run PiecesOS.  Note: this will let us know if we need to tell them to take action to enable any given permissions

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.os_permissions import OSPermissions
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
    api_instance = pieces_os_client.OSApi(api_client)

    try:
        # /os/permissions [GET]
        api_response = api_instance.os_permissions()
        print("The response of OSApi->os_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_permissions: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**OSPermissions**](OSPermissions.md)

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

# **os_permissions_request**
> OSPermissions os_permissions_request(os_permissions=os_permissions)

/os/permissions/request [POST]

This will only work on Macos and Windows.  This will request permissions for the given inputs

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.os_permissions import OSPermissions
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
    api_instance = pieces_os_client.OSApi(api_client)
    os_permissions = pieces_os_client.OSPermissions() # OSPermissions |  (optional)

    try:
        # /os/permissions/request [POST]
        api_response = api_instance.os_permissions_request(os_permissions=os_permissions)
        print("The response of OSApi->os_permissions_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_permissions_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_permissions** | [**OSPermissions**](OSPermissions.md)|  | [optional] 

### Return type

[**OSPermissions**](OSPermissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_restart**
> os_restart()

Your GET endpoint

This will restart PiecesOS, if successfull with return a 204. This is a LOCALOS Only Endpoint.

### Example

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


# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.OSApi(api_client)

    try:
        # Your GET endpoint
        api_instance.os_restart()
    except Exception as e:
        print("Exception when calling OSApi->os_restart: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_settings_snapshot**
> OSServerSettings os_settings_snapshot()

/os/settings [GET]

This is a snapshot of the piecesOS settings

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.os_server_settings import OSServerSettings
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
    api_instance = pieces_os_client.OSApi(api_client)

    try:
        # /os/settings [GET]
        api_response = api_instance.os_settings_snapshot()
        print("The response of OSApi->os_settings_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_settings_snapshot: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**OSServerSettings**](OSServerSettings.md)

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

# **os_settings_stream**
> OSServerSettings os_settings_stream()

/os/settings/stream [WS]

This is a websocket that will emit a change on the update of the OSSettings.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.os_server_settings import OSServerSettings
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
    api_instance = pieces_os_client.OSApi(api_client)

    try:
        # /os/settings/stream [WS]
        api_response = api_instance.os_settings_stream()
        print("The response of OSApi->os_settings_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_settings_stream: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**OSServerSettings**](OSServerSettings.md)

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

# **os_settings_update**
> OSServerSettings os_settings_update(os_server_settings=os_server_settings)

/os/settings/update [POST]

This will ensure that we update the os settings.  This will emit a change via the setting stream as well.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.os_server_settings import OSServerSettings
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
    api_instance = pieces_os_client.OSApi(api_client)
    os_server_settings = pieces_os_client.OSServerSettings() # OSServerSettings |  (optional)

    try:
        # /os/settings/update [POST]
        api_response = api_instance.os_settings_update(os_server_settings=os_server_settings)
        print("The response of OSApi->os_settings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_settings_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os_server_settings** | [**OSServerSettings**](OSServerSettings.md)|  | [optional] 

### Return type

[**OSServerSettings**](OSServerSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_terminate**
> os_terminate()

/os/terminate [POST]

This will force quit PiecesOS

### Example

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


# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.OSApi(api_client)

    try:
        # /os/terminate [POST]
        api_instance.os_terminate()
    except Exception as e:
        print("Exception when calling OSApi->os_terminate: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_update_check**
> OSServerUpdateStatus os_update_check(unchecked_os_server_update=unchecked_os_server_update)

/os/update/check [POST]

This is a helper endpoint that will check the status of an update for PiecesOS. IE if there is an update downloading, if there is one available, but the downloading has not started... etc

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.os_server_update_status import OSServerUpdateStatus
from pieces_os_client.models.unchecked_os_server_update import UncheckedOSServerUpdate
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
    api_instance = pieces_os_client.OSApi(api_client)
    unchecked_os_server_update = pieces_os_client.UncheckedOSServerUpdate() # UncheckedOSServerUpdate |  (optional)

    try:
        # /os/update/check [POST]
        api_response = api_instance.os_update_check(unchecked_os_server_update=unchecked_os_server_update)
        print("The response of OSApi->os_update_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_update_check: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unchecked_os_server_update** | [**UncheckedOSServerUpdate**](UncheckedOSServerUpdate.md)|  | [optional] 

### Return type

[**OSServerUpdateStatus**](OSServerUpdateStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **os_update_check_stream**
> OSServerUpdateStatus os_update_check_stream()

/os/update/check/stream [WS]

This will first kick off the check.  Then will stream the progress.  **TODO lets think about if we want to have a closing NOTE: it is reccommended to use the stream instead of pulling(via the normal check endpoint).

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.os_server_update_status import OSServerUpdateStatus
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
    api_instance = pieces_os_client.OSApi(api_client)

    try:
        # /os/update/check/stream [WS]
        api_response = api_instance.os_update_check_stream()
        print("The response of OSApi->os_update_check_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_update_check_stream: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**OSServerUpdateStatus**](OSServerUpdateStatus.md)

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

# **sign_into_os**
> UserProfile sign_into_os()



A trigger that launches a Sign into OS Server

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.user_profile import UserProfile
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
    api_instance = pieces_os_client.OSApi(api_client)

    try:
        # 
        api_response = api_instance.sign_into_os()
        print("The response of OSApi->sign_into_os:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->sign_into_os: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**UserProfile**](UserProfile.md)

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

# **sign_out_of_os**
> Users sign_out_of_os()

/os/sign_out [POST]

A trigger that signs out a user from the OS

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.users import Users
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
    api_instance = pieces_os_client.OSApi(api_client)

    try:
        # /os/sign_out [POST]
        api_response = api_instance.sign_out_of_os()
        print("The response of OSApi->sign_out_of_os:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->sign_out_of_os: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Users**](Users.md)

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

