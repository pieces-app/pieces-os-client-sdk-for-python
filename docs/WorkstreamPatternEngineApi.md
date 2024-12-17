# pieces_os_client.WorkstreamPatternEngineApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workstream_pattern_engine_create_ingestion**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_create_ingestion) | **POST** /workstream_pattern_engine/ingestions/create | /workstream_pattern_engine/ingestions/create [POST]
[**workstream_pattern_engine_processors_sources**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_sources) | **GET** /workstream_pattern_engine/processors/sources | /workstream_pattern_engine/processors/sources [GET]
[**workstream_pattern_engine_processors_vision_activate**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_activate) | **POST** /workstream_pattern_engine/processors/vision/activate | /workstream_pattern_engine/processors/vision/activate [POST]
[**workstream_pattern_engine_processors_vision_calibration_capture**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_calibration_capture) | **POST** /workstream_pattern_engine/processors/vision/calibration/capture | /workstream_pattern_engine/processors/vision/calibration/capture [POST]
[**workstream_pattern_engine_processors_vision_calibrations_focused**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_calibrations_focused) | **GET** /workstream_pattern_engine/processors/vision/calibrations/focused | /workstream_pattern_engine/processors/vision/calibrations/focused [GET]
[**workstream_pattern_engine_processors_vision_calibrations_snapshot**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_calibrations_snapshot) | **GET** /workstream_pattern_engine/processors/vision/calibrations | /workstream_pattern_engine/processors/vision/calibrations [GET]
[**workstream_pattern_engine_processors_vision_data_clear**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_data_clear) | **POST** /workstream_pattern_engine/processors/vision/data/clear | /workstream_pattern_engine/processors/vision/data/clear [POST]
[**workstream_pattern_engine_processors_vision_deactivate**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_deactivate) | **POST** /workstream_pattern_engine/processors/vision/deactivate | /workstream_pattern_engine/processors/vision/deactivate [POST]
[**workstream_pattern_engine_processors_vision_event_delete_specific_vision_event**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_event_delete_specific_vision_event) | **POST** /workstream_pattern_engine/processors/vision/data/events/{vision_event}/delete | /workstream_pattern_engine/processors/vision/events/{vision_event}/delete [POST]
[**workstream_pattern_engine_processors_vision_events_scoped_delete**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_events_scoped_delete) | **POST** /workstream_pattern_engine/processors/vision/data/events/scoped_delete | /workstream_pattern_engine/processors/vision/events/scoped_delete [POST]
[**workstream_pattern_engine_processors_vision_events_search**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_events_search) | **POST** /workstream_pattern_engine/processors/vision/data/events/search | /workstream_pattern_engine/processors/vision/data/events/search [POST]
[**workstream_pattern_engine_processors_vision_events_snapshot**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_events_snapshot) | **GET** /workstream_pattern_engine/processors/vision/data/events | /workstream_pattern_engine/processors/vision/data/events [GET]
[**workstream_pattern_engine_processors_vision_events_specific_snapshot**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_events_specific_snapshot) | **GET** /workstream_pattern_engine/processors/vision/data/events/{vision_event} | /workstream_pattern_engine/processors/vision/data/events/{vision_event} [GET]
[**workstream_pattern_engine_processors_vision_metadata**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_metadata) | **GET** /workstream_pattern_engine/processors/vision/metadata | /workstream_pattern_engine/processors/vision/metadata [GET]
[**workstream_pattern_engine_processors_vision_status**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_status) | **GET** /workstream_pattern_engine/processors/vision/status | /workstream_pattern_engine/processors/vision/status [GET]
[**workstream_pattern_engine_processors_vision_status_stream**](WorkstreamPatternEngineApi.md#workstream_pattern_engine_processors_vision_status_stream) | **GET** /workstream_pattern_engine/processors/vision/status/stream | /workstream_pattern_engine/processors/vision/status/steam [WS]


# **workstream_pattern_engine_create_ingestion**
> WorkstreamIngestion workstream_pattern_engine_create_ingestion(seeded_workstream_ingestion=seeded_workstream_ingestion)

/workstream_pattern_engine/ingestions/create [POST]

This will take in events from plugins that will be used to drive data to be displayed in the feed.  This is not guaranteed to display information that is taken into this endpoint in the feed.  We take a subset of the information provided in this endpoint + information from the WPE to curated a highly relevant Heads up display of useful materials.

### Example

* Api Key Authentication (application):
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

# **workstream_pattern_engine_processors_sources**
> WorkstreamPatternEngineSources workstream_pattern_engine_processors_sources()

/workstream_pattern_engine/processors/sources [GET]

This will return all of the applications(focused windows) that have events saved within WPE qdrant collection.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_pattern_engine_sources import WorkstreamPatternEngineSources
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)

    try:
        # /workstream_pattern_engine/processors/sources [GET]
        api_response = api_instance.workstream_pattern_engine_processors_sources()
        print("The response of WorkstreamPatternEngineApi->workstream_pattern_engine_processors_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_sources: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkstreamPatternEngineSources**](WorkstreamPatternEngineSources.md)

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

# **workstream_pattern_engine_processors_vision_activate**
> WorkstreamPatternEngineStatus workstream_pattern_engine_processors_vision_activate(workstream_pattern_engine_status=workstream_pattern_engine_status)

/workstream_pattern_engine/processors/vision/activate [POST]

This will activate your Workstream Pattern Engine. This is used to aggregate information on your user's desktop, specifically recording the application in focus and aggregating relevant context that will then be used to ground the copilot conversations, as well as the feed.  Note: required to be a beta user to use this feature until this is live(roughly mid to late April)

### Example

* Api Key Authentication (application):
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

[application](../README.md#application)

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

# **workstream_pattern_engine_processors_vision_calibration_capture**
> WorkstreamPatternEngineVisionCalibration workstream_pattern_engine_processors_vision_calibration_capture()

/workstream_pattern_engine/processors/vision/calibration/capture [POST]

This will attempt to capture the copilot/feed/xyz dimensions of current focused window  note: in the future we can make a differentiation of the dimensions based on the type of qrCode.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_pattern_engine_vision_calibration import WorkstreamPatternEngineVisionCalibration
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)

    try:
        # /workstream_pattern_engine/processors/vision/calibration/capture [POST]
        api_response = api_instance.workstream_pattern_engine_processors_vision_calibration_capture()
        print("The response of WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_calibration_capture:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_calibration_capture: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkstreamPatternEngineVisionCalibration**](WorkstreamPatternEngineVisionCalibration.md)

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

# **workstream_pattern_engine_processors_vision_calibrations_focused**
> WorkstreamPatternEngineVisionCalibration workstream_pattern_engine_processors_vision_calibrations_focused()

/workstream_pattern_engine/processors/vision/calibrations/focused [GET]

This will get the copilot/feed/xyz dimensions of the focused window.  This endpoint will attempt to do the following: 1. get the focus window 2. we will do a lookup to see if we have the copilot/feed/xyz dimension for this window if not we will return null if so we will return the dimensions as well as when the dimensions were taken  note: in the future we can make a differentiation of the dimensions based on the type of qrCode. note: no need to pass in the window name: b/c we will just get the focused window note: we will also return the window name in the returnable so the dev can verify this is the window of the plugin.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_pattern_engine_vision_calibration import WorkstreamPatternEngineVisionCalibration
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)

    try:
        # /workstream_pattern_engine/processors/vision/calibrations/focused [GET]
        api_response = api_instance.workstream_pattern_engine_processors_vision_calibrations_focused()
        print("The response of WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_calibrations_focused:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_calibrations_focused: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkstreamPatternEngineVisionCalibration**](WorkstreamPatternEngineVisionCalibration.md)

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

# **workstream_pattern_engine_processors_vision_calibrations_snapshot**
> WorkstreamPatternEngineVisionCalibrations workstream_pattern_engine_processors_vision_calibrations_snapshot()

/workstream_pattern_engine/processors/vision/calibrations [GET]

This will return a snapshot of all of our captured copilot window Dimensions   note: this will return many captures note: will want to add type of calibration for this specific dimension(ie copilot/feed/xyz) note: in the future we can make a differentiation of the dimensions based on the type of qrCode.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_pattern_engine_vision_calibrations import WorkstreamPatternEngineVisionCalibrations
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)

    try:
        # /workstream_pattern_engine/processors/vision/calibrations [GET]
        api_response = api_instance.workstream_pattern_engine_processors_vision_calibrations_snapshot()
        print("The response of WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_calibrations_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_calibrations_snapshot: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkstreamPatternEngineVisionCalibrations**](WorkstreamPatternEngineVisionCalibrations.md)

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

# **workstream_pattern_engine_processors_vision_data_clear**
> workstream_pattern_engine_processors_vision_data_clear(workstream_pattern_engine_data_cleanup_request=workstream_pattern_engine_data_cleanup_request)

/workstream_pattern_engine/processors/vision/data/clear [POST]

This will clear the data for the Workstream Pattern Engine, specifically for our vision data.  This boy will accept ranges of time that the user wants to remove the processing from.

### Example

* Api Key Authentication (application):
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

[application](../README.md#application)

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

* Api Key Authentication (application):
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

[application](../README.md#application)

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

# **workstream_pattern_engine_processors_vision_event_delete_specific_vision_event**
> workstream_pattern_engine_processors_vision_event_delete_specific_vision_event(vision_event)

/workstream_pattern_engine/processors/vision/events/{vision_event}/delete [POST]

This will delete a single event.

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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)
    vision_event = 'vision_event_example' # str | This is a identifier that is used to identify a specific WPE_vision event.

    try:
        # /workstream_pattern_engine/processors/vision/events/{vision_event}/delete [POST]
        api_instance.workstream_pattern_engine_processors_vision_event_delete_specific_vision_event(vision_event)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_event_delete_specific_vision_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vision_event** | **str**| This is a identifier that is used to identify a specific WPE_vision event. | 

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

# **workstream_pattern_engine_processors_vision_events_scoped_delete**
> FlattenedWorkstreamPatternEngineVisionEvents workstream_pattern_engine_processors_vision_events_scoped_delete(workstream_pattern_engine_vision_event_deletions=workstream_pattern_engine_vision_event_deletions)

/workstream_pattern_engine/processors/vision/events/scoped_delete [POST]

This will remove the UUIDs that were removed from the qdrant event.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.flattened_workstream_pattern_engine_vision_events import FlattenedWorkstreamPatternEngineVisionEvents
from pieces_os_client.models.workstream_pattern_engine_vision_event_deletions import WorkstreamPatternEngineVisionEventDeletions
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)
    workstream_pattern_engine_vision_event_deletions = pieces_os_client.WorkstreamPatternEngineVisionEventDeletions() # WorkstreamPatternEngineVisionEventDeletions |  (optional)

    try:
        # /workstream_pattern_engine/processors/vision/events/scoped_delete [POST]
        api_response = api_instance.workstream_pattern_engine_processors_vision_events_scoped_delete(workstream_pattern_engine_vision_event_deletions=workstream_pattern_engine_vision_event_deletions)
        print("The response of WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_events_scoped_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_events_scoped_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workstream_pattern_engine_vision_event_deletions** | [**WorkstreamPatternEngineVisionEventDeletions**](WorkstreamPatternEngineVisionEventDeletions.md)|  | [optional] 

### Return type

[**FlattenedWorkstreamPatternEngineVisionEvents**](FlattenedWorkstreamPatternEngineVisionEvents.md)

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

# **workstream_pattern_engine_processors_vision_events_search**
> SearchedWorkstreamPatternEngineVisionEvents workstream_pattern_engine_processors_vision_events_search(transferables=transferables, search_input=search_input)

/workstream_pattern_engine/processors/vision/data/events/search [POST]

This will search your WPE events and will return a list of events that match the query/timestamp range/list of applications

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.search_input import SearchInput
from pieces_os_client.models.searched_workstream_pattern_engine_vision_events import SearchedWorkstreamPatternEngineVisionEvents
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    search_input = pieces_os_client.SearchInput() # SearchInput |  (optional)

    try:
        # /workstream_pattern_engine/processors/vision/data/events/search [POST]
        api_response = api_instance.workstream_pattern_engine_processors_vision_events_search(transferables=transferables, search_input=search_input)
        print("The response of WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_events_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_events_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **search_input** | [**SearchInput**](SearchInput.md)|  | [optional] 

### Return type

[**SearchedWorkstreamPatternEngineVisionEvents**](SearchedWorkstreamPatternEngineVisionEvents.md)

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

# **workstream_pattern_engine_processors_vision_events_snapshot**
> WorkstreamPatternEngineVisionEvents workstream_pattern_engine_processors_vision_events_snapshot(transferables=transferables)

/workstream_pattern_engine/processors/vision/data/events [GET]

This will return a snapshot of all of the WPE qdrant events  note: if the transferables: are true then we will provide values for each of our events otherwise       we will just provide basic metadata

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_pattern_engine_vision_events import WorkstreamPatternEngineVisionEvents
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /workstream_pattern_engine/processors/vision/data/events [GET]
        api_response = api_instance.workstream_pattern_engine_processors_vision_events_snapshot(transferables=transferables)
        print("The response of WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_events_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_events_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**WorkstreamPatternEngineVisionEvents**](WorkstreamPatternEngineVisionEvents.md)

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

# **workstream_pattern_engine_processors_vision_events_specific_snapshot**
> WorkstreamPatternEngineVisionEvent workstream_pattern_engine_processors_vision_events_specific_snapshot(vision_event, transferables=transferables)

/workstream_pattern_engine/processors/vision/data/events/{vision_event} [GET]

This will return a specific event from the WPE.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_pattern_engine_vision_event import WorkstreamPatternEngineVisionEvent
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)
    vision_event = 'vision_event_example' # str | This is a identifier that is used to identify a specific WPE_vision event.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /workstream_pattern_engine/processors/vision/data/events/{vision_event} [GET]
        api_response = api_instance.workstream_pattern_engine_processors_vision_events_specific_snapshot(vision_event, transferables=transferables)
        print("The response of WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_events_specific_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_events_specific_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vision_event** | **str**| This is a identifier that is used to identify a specific WPE_vision event. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**WorkstreamPatternEngineVisionEvent**](WorkstreamPatternEngineVisionEvent.md)

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

# **workstream_pattern_engine_processors_vision_metadata**
> WorkstreamPatternEngineVisionMetadata workstream_pattern_engine_processors_vision_metadata()

/workstream_pattern_engine/processors/vision/metadata [GET]

This is an endpoint that will return the metadata of the vision data (WPE qdrant size)

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.workstream_pattern_engine_vision_metadata import WorkstreamPatternEngineVisionMetadata
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)

    try:
        # /workstream_pattern_engine/processors/vision/metadata [GET]
        api_response = api_instance.workstream_pattern_engine_processors_vision_metadata()
        print("The response of WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_metadata: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkstreamPatternEngineVisionMetadata**](WorkstreamPatternEngineVisionMetadata.md)

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

# **workstream_pattern_engine_processors_vision_status**
> WorkstreamPatternEngineStatus workstream_pattern_engine_processors_vision_status()

/workstream_pattern_engine/processors/vision/status [GET]

This will get a snapshot of the status your Workstream Pattern Engine. This is used to aggregate information on your user's desktop, specifically recording the application in focus and aggregating relevant context that will then be used to ground the copilot conversations, as well as the feed.  Note: required to be a beta user to use this feature until this is live(roughly mid to late April)

### Example

* Api Key Authentication (application):
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

[application](../README.md#application)

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

# **workstream_pattern_engine_processors_vision_status_stream**
> WorkstreamPatternEngineStatus workstream_pattern_engine_processors_vision_status_stream()

/workstream_pattern_engine/processors/vision/status/steam [WS]

This is a websocket for the status of the workstream pattern engine for vision.  This will emit an event when this is first connected to, and will emit an event when every this value changes  This will emit a \"WorkstreamPatternEngineStatus\" Model.

### Example

* Api Key Authentication (application):
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
    api_instance = pieces_os_client.WorkstreamPatternEngineApi(api_client)

    try:
        # /workstream_pattern_engine/processors/vision/status/steam [WS]
        api_response = api_instance.workstream_pattern_engine_processors_vision_status_stream()
        print("The response of WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_status_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkstreamPatternEngineApi->workstream_pattern_engine_processors_vision_status_stream: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkstreamPatternEngineStatus**](WorkstreamPatternEngineStatus.md)

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

