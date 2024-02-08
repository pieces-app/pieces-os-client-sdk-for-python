# openapi_client.DatabaseApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**database_export**](DatabaseApi.md#database_export) | **GET** /database/export | Your GET endpoint
[**database_import**](DatabaseApi.md#database_import) | **POST** /database/import | /database/import [POST]


# **database_export**
> ExportedDatabase database_export()

Your GET endpoint

This is going to export your current database.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.exported_database import ExportedDatabase
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatabaseApi(api_client)

    try:
        # Your GET endpoint
        api_response = api_instance.database_export()
        print("The response of DatabaseApi->database_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApi->database_export: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ExportedDatabase**](ExportedDatabase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **database_import**
> database_import(exported_database=exported_database)

/database/import [POST]

This is going to take in a database, and merge it with the current database. This will revert your database back to it original form if this request fails.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.exported_database import ExportedDatabase
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatabaseApi(api_client)
    exported_database = openapi_client.ExportedDatabase() # ExportedDatabase |  (optional)

    try:
        # /database/import [POST]
        api_instance.database_import(exported_database=exported_database)
    except Exception as e:
        print("Exception when calling DatabaseApi->database_import: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exported_database** | [**ExportedDatabase**](ExportedDatabase.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**500** | Internal Server Error |  -  |
**505** | HTTP Version Not Supported, This means that your user need to update their local os, and they cannot create a shareable link. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

