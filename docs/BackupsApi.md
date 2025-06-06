# pieces_os_client.BackupsApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backups_create_new_backup**](BackupsApi.md#backups_create_new_backup) | **POST** /backups/create | /backups/create [POST]
[**backups_create_new_backup_streamed**](BackupsApi.md#backups_create_new_backup_streamed) | **POST** /backups/create/streamed | /backups/create/streamed [POST]
[**backups_create_new_backup_streamed_websocket**](BackupsApi.md#backups_create_new_backup_streamed_websocket) | **GET** /backups/create/streamed/websocket | /backups/create/streamed/websocket [WS]
[**backups_delete_specific_backup**](BackupsApi.md#backups_delete_specific_backup) | **POST** /backups/{backup}/delete | /backups/{backup}/delete [POST]
[**backups_snapshot**](BackupsApi.md#backups_snapshot) | **GET** /backups | /backups [GET]
[**backups_streamed_progress**](BackupsApi.md#backups_streamed_progress) | **GET** /backups/streamed/progress | /backups/streamed/progress [WS]


# **backups_create_new_backup**
> Backup backups_create_new_backup(seeded_backup=seeded_backup)

/backups/create [POST]

This take a local database and ensure that it is backed up to the cloud.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.backup import Backup
from pieces_os_client.models.seeded_backup import SeededBackup
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
    api_instance = pieces_os_client.BackupsApi(api_client)
    seeded_backup = pieces_os_client.SeededBackup() # SeededBackup |  (optional)

    try:
        # /backups/create [POST]
        api_response = api_instance.backups_create_new_backup(seeded_backup=seeded_backup)
        print("The response of BackupsApi->backups_create_new_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->backups_create_new_backup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_backup** | [**SeededBackup**](SeededBackup.md)|  | [optional] 

### Return type

[**Backup**](Backup.md)

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
**511** | Authentication Required, This means that you user needs to be authenticated with OS in order to perform this action |  -  |
**505** | HTTP Version Not Supported, This means that your user needs to update their local os, or they cannot perform backup operations with the cloud |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backups_create_new_backup_streamed**
> BackupStreamedProgress backups_create_new_backup_streamed(seeded_backup=seeded_backup)

/backups/create/streamed [POST]

This take a local database and ensure that it is backed up to the cloud.

NOTE: This is a streamed version of the /backups/create. and Since the Generator is unable to generate a streamed endpoint. this is a place holder, and will need to be implemented isolated from the code generator.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.backup_streamed_progress import BackupStreamedProgress
from pieces_os_client.models.seeded_backup import SeededBackup
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
    api_instance = pieces_os_client.BackupsApi(api_client)
    seeded_backup = pieces_os_client.SeededBackup() # SeededBackup |  (optional)

    try:
        # /backups/create/streamed [POST]
        api_response = api_instance.backups_create_new_backup_streamed(seeded_backup=seeded_backup)
        print("The response of BackupsApi->backups_create_new_backup_streamed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->backups_create_new_backup_streamed: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_backup** | [**SeededBackup**](SeededBackup.md)|  | [optional] 

### Return type

[**BackupStreamedProgress**](BackupStreamedProgress.md)

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
**511** | Authentication Required, This means that you user needs to be authenticated with OS in order to perform this action |  -  |
**505** | HTTP Version Not Supported, This means that your user needs to update their local os, or they cannot perform backup operation with the cloud |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backups_create_new_backup_streamed_websocket**
> BackupStreamedProgress backups_create_new_backup_streamed_websocket(seeded_backup=seeded_backup)

/backups/create/streamed/websocket [WS]

WEBSOCKET VERSION! This take a local database and ensure that it is backed up to the cloud.

NOTE: This is a streamed version of the /backups/create. and Since the Generator is unable to generate a streamed endpoint. this is a place holder, and will need to be implemented isolated from the code generator.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.backup_streamed_progress import BackupStreamedProgress
from pieces_os_client.models.seeded_backup import SeededBackup
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
    api_instance = pieces_os_client.BackupsApi(api_client)
    seeded_backup = pieces_os_client.SeededBackup() # SeededBackup |  (optional)

    try:
        # /backups/create/streamed/websocket [WS]
        api_response = api_instance.backups_create_new_backup_streamed_websocket(seeded_backup=seeded_backup)
        print("The response of BackupsApi->backups_create_new_backup_streamed_websocket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->backups_create_new_backup_streamed_websocket: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_backup** | [**SeededBackup**](SeededBackup.md)|  | [optional] 

### Return type

[**BackupStreamedProgress**](BackupStreamedProgress.md)

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
**511** | Authentication Required, This means that you user needs to be authenticated with OS in order to perform this action |  -  |
**505** | HTTP Version Not Supported, This means that your user needs to update their local os, or they cannot perform backup operation with the cloud |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backups_delete_specific_backup**
> backups_delete_specific_backup(backup, backup2=backup2)

/backups/{backup}/delete [POST]

This will delete a specific backup from the cloud.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.backup import Backup
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
    api_instance = pieces_os_client.BackupsApi(api_client)
    backup = 'backup_example' # str | This is a identifier that is used to identify a specific backup.(version_timestamp)
    backup2 = pieces_os_client.Backup() # Backup |  (optional)

    try:
        # /backups/{backup}/delete [POST]
        api_instance.backups_delete_specific_backup(backup, backup2=backup2)
    except Exception as e:
        print("Exception when calling BackupsApi->backups_delete_specific_backup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup** | **str**| This is a identifier that is used to identify a specific backup.(version_timestamp) | 
 **backup2** | [**Backup**](Backup.md)|  | [optional] 

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
**511** | Authentication Required, This means that you user needs to be authenticated with OS in order to perform this action |  -  |
**505** | HTTP Version Not Supported, This means that your user needs to update their local os, or they cannot perform backup operation with the cloud |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backups_snapshot**
> Backups backups_snapshot()

/backups [GET]

This will get a snapshot of Backsup within the cloud.

This endpoint requires our user to be authenticated and connected to the cloud.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.backups import Backups
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
    api_instance = pieces_os_client.BackupsApi(api_client)

    try:
        # /backups [GET]
        api_response = api_instance.backups_snapshot()
        print("The response of BackupsApi->backups_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->backups_snapshot: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Backups**](Backups.md)

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
**511** | Authentication Required, This means that you user needs to be authenticated with OS in order to perform this action |  -  |
**505** | HTTP Version Not Supported, This means that your user needs to update their local os, or they cannot perform backup operations with the cloud |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backups_streamed_progress**
> BackupsStreamedProgress backups_streamed_progress()

/backups/streamed/progress [WS]

This endpoint is a Websocket, that will list all the current websockets that are in progress, this will emit changes as there are changes with the backups or restores in progress.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.backups_streamed_progress import BackupsStreamedProgress
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
    api_instance = pieces_os_client.BackupsApi(api_client)

    try:
        # /backups/streamed/progress [WS]
        api_response = api_instance.backups_streamed_progress()
        print("The response of BackupsApi->backups_streamed_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupsApi->backups_streamed_progress: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**BackupsStreamedProgress**](BackupsStreamedProgress.md)

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

