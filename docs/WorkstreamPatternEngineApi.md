# pieces_os_client.WorkstreamPatternEngineApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workstream_pattern_engine_create_ingestion**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_create_ingestion) | **POST** /workstream_pattern_engine/ingestions/create | /workstream_pattern_engine/ingestions/create [POST]
[**workstream_pattern_engine_processors_vision_activate**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_activate) | **POST** /workstream_pattern_engine/processors/vision/activate | /workstream_pattern_engine/processors/vision/activate [POST]
[**workstream_pattern_engine_processors_vision_data_clear**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_data_clear) | **POST** /workstream_pattern_engine/processors/vision/data/clear | /workstream_pattern_engine/processors/vision/data/clear [POST]
[**workstream_pattern_engine_processors_vision_deactivate**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_deactivate) | **POST** /workstream_pattern_engine/processors/vision/deactivate | /workstream_pattern_engine/processors/vision/deactivate [POST]
[**workstream_pattern_engine_processors_vision_status**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_status) | **GET** /workstream_pattern_engine/processors/vision/status | /workstream_pattern_engine/processors/vision/status [GET]


# **workstream_pattern_engine_create_ingestion**
> WorkstreamIngestion workstream_pattern_engine_create_ingestion(seeded_workstream_ingestion=seeded_workstream_ingestion)

/workstream_pattern_engine/ingestions/create [POST]

This will take in events from plugins that will be used to drive data to be displayed in the feed.  This is not guaranteed to display information that is taken into this endpoint in the feed.  We take a subset of the information provided in this endpoint + information from the WPE to curated a highly relevant Heads up display of useful materials.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.seeded_workstream_ingestion import SeededWorkstreamIngestion
from pieces_os_client.models.workstream_ingestion import WorkstreamIngestion
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)
    seeded_workstream_ingestion = pieces_os_client.SeededWorkstreamIngestion() # SeededWorkstreamIngestion |  (optional)

    try:
        # /workstream_pattern_engine/ingestions/create [POST]
        api_response = api_instance.workstream_pattern_engine_create_ingestion(seeded_workstream_ingestion=seeded_workstream_ingestion)
        print("The response of WorkstreamPatternEngineApi->workstream_pattern_engine_create_ingestion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_create_ingestion: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_workstream_ingestion** | [**SeededWorkstreamIngestion**](SeededWorkstreamIngestion.md)|  | [optional] 

### Return type

[**WorkstreamIngestion**](WorkstreamIngestion.md)

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

# **workstream_pattern_engine_processors_vision_activate**
> WorkstreamPatternEngineStatus workstream_pattern_engine_processors_vision_activate(workstream_pattern_engine_status=workstream_pattern_engine_status)

/workstream_pattern_engine/processors/vision/activate [POST]

This will activate your Workstream Pattern Engine. This is used to aggregate information on your user's desktop, specifically recording the application in focus and aggregating relevant context that will then be used to ground the copilot conversations, as well as the feed.  Note: required to be a beta user to use this feature until this is live(roughly mid to late April)

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_pattern_engine_status import WorkstreamPatternEngineStatus
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)
    workstream_pattern_engine_status = pieces_os_client.WorkstreamPatternEngineStatus() # WorkstreamPatternEngineStatus |  (optional)

    try:
        # /workstream_pattern_engine/processors/vision/activate [POST]
        api_response = api_instance.workstream_pattern_engine_processors_vision_activate(workstream_pattern_engine_status=workstream_pattern_engine_status)
        print("The response of WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_activate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_activate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_pattern_engine_status** | [**WorkstreamPatternEngineStatus**](WorkstreamPatternEngineStatus.md)|  | [optional] 

### Return type

[**WorkstreamPatternEngineStatus**](WorkstreamPatternEngineStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden, this is not available for non-beta used until mid to late April. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workstream_pattern_engine_processors_vision_data_clear**
> workstream_pattern_engine_processors_vision_data_clear(workstream_pattern_engine_data_cleanup_request=workstream_pattern_engine_data_cleanup_request)

/workstream_pattern_engine/processors/vision/data/clear [POST]

This will clear the data for the Workstream Pattern Engine, specifically for our vision data.  This boy will accept ranges of time that the user wants to remove the processing from.

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_pattern_engine_data_cleanup_request import WorkstreamPatternEngineDataCleanupRequest
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)
    workstream_pattern_engine_data_cleanup_request = pieces_os_client.WorkstreamPatternEngineDataCleanupRequest() # WorkstreamPatternEngineDataCleanupRequest |  (optional)

    try:
        # /workstream_pattern_engine/processors/vision/data/clear [POST]
        api_instance.workstream_pattern_engine_processors_vision_data_clear(workstream_pattern_engine_data_cleanup_request=workstream_pattern_engine_data_cleanup_request)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_data_clear: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_pattern_engine_data_cleanup_request** | [**WorkstreamPatternEngineDataCleanupRequest**](WorkstreamPatternEngineDataCleanupRequest.md)|  | [optional] 

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
**403** | Forbidden, this is not available for non-beta used until mid to late April. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workstream_pattern_engine_processors_vision_deactivate**
> WorkstreamPatternEngineStatus workstream_pattern_engine_processors_vision_deactivate(workstream_pattern_engine_status=workstream_pattern_engine_status)

/workstream_pattern_engine/processors/vision/deactivate [POST]

This will deactivate your Workstream Pattern Engine. This is used to aggregate information on your user's desktop, specifically recording the application in focus and aggregating relevant context that will then be used to ground the copilot conversations, as well as the feed.  Note: required to be a beta user to use this feature until this is live(roughly mid to late April)

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_pattern_engine_status import WorkstreamPatternEngineStatus
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)
    workstream_pattern_engine_status = pieces_os_client.WorkstreamPatternEngineStatus() # WorkstreamPatternEngineStatus |  (optional)

    try:
        # /workstream_pattern_engine/processors/vision/deactivate [POST]
        api_response = api_instance.workstream_pattern_engine_processors_vision_deactivate(workstream_pattern_engine_status=workstream_pattern_engine_status)
        print("The response of WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_deactivate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_deactivate: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_pattern_engine_status** | [**WorkstreamPatternEngineStatus**](WorkstreamPatternEngineStatus.md)|  | [optional] 

### Return type

[**WorkstreamPatternEngineStatus**](WorkstreamPatternEngineStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden, this is not available for non-beta used until mid to late April. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workstream_pattern_engine_processors_vision_status**
> WorkstreamPatternEngineStatus workstream_pattern_engine_processors_vision_status()

/workstream_pattern_engine/processors/vision/status [GET]

This will get a snapshot of the status your Workstream Pattern Engine. This is used to aggregate information on your user's desktop, specifically recording the application in focus and aggregating relevant context that will then be used to ground the copilot conversations, as well as the feed.  Note: required to be a beta user to use this feature until this is live(roughly mid to late April)

### Example

```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_pattern_engine_status import WorkstreamPatternEngineStatus
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)

    try:
        # /workstream_pattern_engine/processors/vision/status [GET]
        api_response = api_instance.workstream_pattern_engine_processors_vision_status()
        print("The response of WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_status: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkstreamPatternEngineStatus**](WorkstreamPatternEngineStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden, this is not available for non-beta used until mid to late April. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

