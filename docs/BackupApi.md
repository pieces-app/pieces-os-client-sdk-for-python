# pieces_os_client.BackupApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup**](BackupApi.md#backup) | **POST** /backup | /backup [POST]
[**backup_asset**](BackupApi.md#backup_asset) | **POST** /backup/asset | /backup/asset [POST]
[**backup_restore_specific_backup**](BackupApi.md#backup_restore_specific_backup) | **POST** /backup/{backup}/restore | /backup/{backup}/restore [POST]
[**backup_restore_specific_backup_streamed**](BackupApi.md#backup_restore_specific_backup_streamed) | **POST** /backup/{backup}/restore/streamed | /backup/{backup}/restore/streamed [POST]
[**backup_restore_specific_backup_streamed_websocket**](BackupApi.md#backup_restore_specific_backup_streamed_websocket) | **GET** /backup/{backup}/restore/streamed/websocket | /backup/{backup}/restore/streamed/websocket [WS]
[**backup_specific_backup_snapshot**](BackupApi.md#backup_specific_backup_snapshot) | **GET** /backup/{backup} | /backup/{backup} [GET]
[**backup_specific_creation_cancel**](BackupApi.md#backup_specific_creation_cancel) | **POST** /backup/{backup}/creation/cancel | /backup/{backup}/creation/cancel [POST]
[**backup_specific_creation_status**](BackupApi.md#backup_specific_creation_status) | **GET** /backup/{backup}/creation/status | /backup/{backup}/creation/status [GET]
[**backup_specific_restoration_cancel**](BackupApi.md#backup_specific_restoration_cancel) | **POST** /backup/{backup}/restoration/cancel | /backup/{backup}/restoration/cancel [POST]
[**backup_specific_restoration_status**](BackupApi.md#backup_specific_restoration_status) | **GET** /backup/{backup}/restoration/status | /backup/{backup}/restoration/status [GET]


# **backup**
> backup(assets=assets)

/backup [POST]



### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.assets import Assets
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
    api_instance = pieces_os_client.BackupApi(api_client)
    assets = pieces_os_client.Assets() # Assets |  (optional)

    try:
        # /backup [POST]
        api_instance.backup(assets=assets)
    except Exception as e:
        print("Exception when calling BackupApi->backup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assets** | [**Assets**](Assets.md)|  | [optional] 

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
**505** | HTTP Version Not Supported, This means that your user need to update their local os, or they cannot Backup to the Cloud. |  -  |
**511** | Network Authentication Required, This means that you user needs to be authenticated with OS inorder to backup. The User also need to be connected to their cloud to backup.(If either of the 2 are not connected we will return a 511)  TODO thinking about returning a more comprehensive value for digestion on the recieving side. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_asset**
> backup_asset(asset=asset)

/backup/asset [POST]

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.asset import Asset
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
    api_instance = pieces_os_client.BackupApi(api_client)
    asset = pieces_os_client.Asset() # Asset |  (optional)

    try:
        # /backup/asset [POST]
        api_instance.backup_asset(asset=asset)
    except Exception as e:
        print("Exception when calling BackupApi->backup_asset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**Asset**](Asset.md)|  | [optional] 

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
**505** | HTTP Version Not Supported, This means that your user need to update their local os, or they cannot Backup to the Cloud. |  -  |
**511** | Network Authentication Required, This means that you user needs to be authenticated with OS inorder to backup. The User also need to be connected to their cloud to backup.(If either of the 2 are not connected we will return a 511)  TODO thinking about returning a more comprehensive value for digestion on the recieving side. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_restore_specific_backup**
> Backup backup_restore_specific_backup(backup, backup2=backup2)

/backup/{backup}/restore [POST]

Given a backup identifier version_timestamp.  we will restore a given backup from the cloud and override your local database!!!  NOTE!!!! This will NOT sync, ie all local snippets will get replaced with the restored database.

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
    api_instance = pieces_os_client.BackupApi(api_client)
    backup = 'backup_example' # str | This is a identifier that is used to identify a specific backup.(version_timestamp)
    backup2 = pieces_os_client.Backup() # Backup |  (optional)

    try:
        # /backup/{backup}/restore [POST]
        api_response = api_instance.backup_restore_specific_backup(backup, backup2=backup2)
        print("The response of BackupApi->backup_restore_specific_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->backup_restore_specific_backup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup** | **str**| This is a identifier that is used to identify a specific backup.(version_timestamp) | 
 **backup2** | [**Backup**](Backup.md)|  | [optional] 

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

# **backup_restore_specific_backup_streamed**
> BackupStreamedProgress backup_restore_specific_backup_streamed(backup, backup2=backup2)

/backup/{backup}/restore/streamed [POST]

This take a local database and ensure that it is backed up to the cloud.  NOTE: This is a streamed version of the /backups/<backup>/restore. and Since the Generator is unable to generate a streamed endpoint. this is a place holder, and will need to be implemented isolated from the code generator.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.backup import Backup
from pieces_os_client.models.backup_streamed_progress import BackupStreamedProgress
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
    api_instance = pieces_os_client.BackupApi(api_client)
    backup = 'backup_example' # str | This is a identifier that is used to identify a specific backup.(version_timestamp)
    backup2 = pieces_os_client.Backup() # Backup |  (optional)

    try:
        # /backup/{backup}/restore/streamed [POST]
        api_response = api_instance.backup_restore_specific_backup_streamed(backup, backup2=backup2)
        print("The response of BackupApi->backup_restore_specific_backup_streamed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->backup_restore_specific_backup_streamed: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup** | **str**| This is a identifier that is used to identify a specific backup.(version_timestamp) | 
 **backup2** | [**Backup**](Backup.md)|  | [optional] 

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
**511** | Authentication Required, This means that you user needs to be authenticated with OS in order to change the beta status |  -  |
**505** | HTTP Version Not Supported, This means that your user needs to update their local os, or they cannot perform backup operation with the cloud |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_restore_specific_backup_streamed_websocket**
> BackupStreamedProgress backup_restore_specific_backup_streamed_websocket(backup, backup2=backup2)

/backup/{backup}/restore/streamed/websocket [WS]

WEBOCKET IMPLEMENTATION: This take a local database and ensure that it is backed up to the cloud.  NOTE: This is a streamed version of the /backups/<backup>/restore. and Since the Generator is unable to generate a streamed endpoint. this is a place holder, and will need to be implemented isolated from the code generator.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.backup import Backup
from pieces_os_client.models.backup_streamed_progress import BackupStreamedProgress
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
    api_instance = pieces_os_client.BackupApi(api_client)
    backup = 'backup_example' # str | This is a identifier that is used to identify a specific backup.(version_timestamp)
    backup2 = pieces_os_client.Backup() # Backup |  (optional)

    try:
        # /backup/{backup}/restore/streamed/websocket [WS]
        api_response = api_instance.backup_restore_specific_backup_streamed_websocket(backup, backup2=backup2)
        print("The response of BackupApi->backup_restore_specific_backup_streamed_websocket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->backup_restore_specific_backup_streamed_websocket: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup** | **str**| This is a identifier that is used to identify a specific backup.(version_timestamp) | 
 **backup2** | [**Backup**](Backup.md)|  | [optional] 

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
**511** | Authentication Required, This means that you user needs to be authenticated with OS in order to change the beta status |  -  |
**505** | HTTP Version Not Supported, This means that your user needs to update their local os, or they cannot perform backup operation with the cloud |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_specific_backup_snapshot**
> Backup backup_specific_backup_snapshot(backup)

/backup/{backup} [GET]

This will just get the metadata associated with a specific backup.

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
    api_instance = pieces_os_client.BackupApi(api_client)
    backup = 'backup_example' # str | This is a identifier that is used to identify a specific backup.(version_timestamp)

    try:
        # /backup/{backup} [GET]
        api_response = api_instance.backup_specific_backup_snapshot(backup)
        print("The response of BackupApi->backup_specific_backup_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->backup_specific_backup_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup** | **str**| This is a identifier that is used to identify a specific backup.(version_timestamp) | 

### Return type

[**Backup**](Backup.md)

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
**511** | Authentication Required, This means that you user needs to be authenticated with OS in order to change the beta status |  -  |
**505** | HTTP Version Not Supported, This means that your user needs to update their local os, or they cannot perform backup operation with the cloud |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_specific_creation_cancel**
> backup_specific_creation_cancel(backup)

/backup/{backup}/creation/cancel [POST]

This is Going to cancel a create backup (streamed) or not streamed that is currently in progress.  This will throw a 500 if there is not a backup in progress.  TODO: ADD mofe DESCRIPITON To this.

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
    api_instance = pieces_os_client.BackupApi(api_client)
    backup = 'backup_example' # str | This is a identifier that is used to identify a specific backup.(version_timestamp)

    try:
        # /backup/{backup}/creation/cancel [POST]
        api_instance.backup_specific_creation_cancel(backup)
    except Exception as e:
        print("Exception when calling BackupApi->backup_specific_creation_cancel: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup** | **str**| This is a identifier that is used to identify a specific backup.(version_timestamp) | 

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

# **backup_specific_creation_status**
> BackupStatus backup_specific_creation_status(backup)

/backup/{backup}/creation/status [GET]

TODO add a description:

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.backup_status import BackupStatus
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
    api_instance = pieces_os_client.BackupApi(api_client)
    backup = 'backup_example' # str | This is a identifier that is used to identify a specific backup.(version_timestamp)

    try:
        # /backup/{backup}/creation/status [GET]
        api_response = api_instance.backup_specific_creation_status(backup)
        print("The response of BackupApi->backup_specific_creation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->backup_specific_creation_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup** | **str**| This is a identifier that is used to identify a specific backup.(version_timestamp) | 

### Return type

[**BackupStatus**](BackupStatus.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Internal Server Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_specific_restoration_cancel**
> backup_specific_restoration_cancel(backup, backup2=backup2)

/backup/{backup}/restoration/cancel [POST]

This will cancel a Restoration that is in progress and restore to the original database.  Note: if there is not a restore in progress we will return a 500.  TODO add

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
    api_instance = pieces_os_client.BackupApi(api_client)
    backup = 'backup_example' # str | This is a identifier that is used to identify a specific backup.(version_timestamp)
    backup2 = pieces_os_client.Backup() # Backup |  (optional)

    try:
        # /backup/{backup}/restoration/cancel [POST]
        api_instance.backup_specific_restoration_cancel(backup, backup2=backup2)
    except Exception as e:
        print("Exception when calling BackupApi->backup_specific_restoration_cancel: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_specific_restoration_status**
> BackupStatus backup_specific_restoration_status(backup)

/backup/{backup}/restoration/status [GET]

TODO add a description:

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.backup_status import BackupStatus
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
    api_instance = pieces_os_client.BackupApi(api_client)
    backup = 'backup_example' # str | This is a identifier that is used to identify a specific backup.(version_timestamp)

    try:
        # /backup/{backup}/restoration/status [GET]
        api_response = api_instance.backup_specific_restoration_status(backup)
        print("The response of BackupApi->backup_specific_restoration_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->backup_specific_restoration_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup** | **str**| This is a identifier that is used to identify a specific backup.(version_timestamp) | 

### Return type

[**BackupStatus**](BackupStatus.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Internal Server Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

