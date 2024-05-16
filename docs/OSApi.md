# pieces_os_client.OSApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**link_provider**](OSApi.md#link_provider) | **POST** /os/link_provider | /os/link_provider [POST]
[**os_device_information**](OSApi.md#os_device_information) | **GET** /os/device/information | /os/device/information [GET]
[**os_permissions**](OSApi.md#os_permissions) | **GET** /os/permissions | /os/permissions [GET]
[**os_permissions_request**](OSApi.md#os_permissions_request) | **POST** /os/permissions/request | /os/permissions/request [POST]
[**os_restart**](OSApi.md#os_restart) | **GET** /os/restart | Your GET endpoint
[**os_update_check**](OSApi.md#os_update_check) | **POST** /os/update/check | /os/update/check [POST]
[**pick_files**](OSApi.md#pick_files) | **POST** /os/files/pick | /os/files/pick [POST]
[**pick_folders**](OSApi.md#pick_folders) | **POST** /os/folders/pick | /os/folders/pick [POST]
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

# **os_update_check**
> CheckedOSUpdate os_update_check(unchecked_os_update=unchecked_os_update)

/os/update/check [POST]

This is a helper endpoint that will check the status of an update for PiecesOS. IE if there is an update downloading, if there is one available, but the downloading has not started... etc

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.checked_os_update import CheckedOSUpdate
from pieces_os_client.models.unchecked_os_update import UncheckedOSUpdate
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
    unchecked_os_update = pieces_os_client.UncheckedOSUpdate() # UncheckedOSUpdate |  (optional)

    try:
        # /os/update/check [POST]
        api_response = api_instance.os_update_check(unchecked_os_update=unchecked_os_update)
        print("The response of OSApi->os_update_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->os_update_check: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unchecked_os_update** | [**UncheckedOSUpdate**](UncheckedOSUpdate.md)|  | [optional] 

### Return type

[**CheckedOSUpdate**](CheckedOSUpdate.md)

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

# **pick_files**
> List[str] pick_files(file_picker_input=file_picker_input)

/os/files/pick [POST]

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
        # /os/files/pick [POST]
        api_response = api_instance.pick_files(file_picker_input=file_picker_input)
        print("The response of OSApi->pick_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->pick_files: %s\n" % e)
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

# **pick_folders**
> List[str] pick_folders()

/os/folders/pick [POST]

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
        # /os/folders/pick [POST]
        api_response = api_instance.pick_folders()
        print("The response of OSApi->pick_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSApi->pick_folders: %s\n" % e)
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

