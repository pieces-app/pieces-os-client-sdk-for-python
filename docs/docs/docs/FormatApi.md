# openapi_client.FormatApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**format_analysis**](FormatApi.md#format_analysis) | **GET** /format/{format}/analysis | /format/{format}/analysis [GET]
[**format_reclassify**](FormatApi.md#format_reclassify) | **POST** /format/reclassify | /format/reclassify [POST]
[**format_snapshot**](FormatApi.md#format_snapshot) | **GET** /format/{format} | /format/{format} [GET] Scoped to Format
[**format_update_value**](FormatApi.md#format_update_value) | **POST** /format/update/value | [POST] /format/update/value
[**format_usage_event**](FormatApi.md#format_usage_event) | **POST** /format/usage/event | /format/usage/event [POST] Scoped to Format


# **format_analysis**
> Analysis format_analysis(format)

/format/{format}/analysis [GET]

This will get an analysis from a format's id.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.analysis import Analysis
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
    api_instance = openapi_client.FormatApi(api_client)
    format = '102ff265-fdfb-4142-8d94-4932d400199c' # str | The id (uuid) for a specific format.

    try:
        # /format/{format}/analysis [GET]
        api_response = api_instance.format_analysis(format)
        print("The response of FormatApi->format_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormatApi->format_analysis: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| The id (uuid) for a specific format. | 

### Return type

[**Analysis**](Analysis.md)

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

# **format_reclassify**
> Format format_reclassify(transferable=transferable, format_reclassification=format_reclassification)

/format/reclassify [POST]

This endpoint will be used to reclassify a single Format.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.format import Format
from openapi_client.models.format_reclassification import FormatReclassification
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
    api_instance = openapi_client.FormatApi(api_client)
    transferable = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    format_reclassification = openapi_client.FormatReclassification() # FormatReclassification |  (optional)

    try:
        # /format/reclassify [POST]
        api_response = api_instance.format_reclassify(transferable=transferable, format_reclassification=format_reclassification)
        print("The response of FormatApi->format_reclassify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormatApi->format_reclassify: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferable** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **format_reclassification** | [**FormatReclassification**](FormatReclassification.md)|  | [optional] 

### Return type

[**Format**](Format.md)

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

# **format_snapshot**
> Format format_snapshot(format, transferable=transferable)

/format/{format} [GET] Scoped to Format

Get a snapshot of a specific format.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.format import Format
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
    api_instance = openapi_client.FormatApi(api_client)
    format = '102ff265-fdfb-4142-8d94-4932d400199c' # str | The id (uuid) for a specific format.
    transferable = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /format/{format} [GET] Scoped to Format
        api_response = api_instance.format_snapshot(format, transferable=transferable)
        print("The response of FormatApi->format_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormatApi->format_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| The id (uuid) for a specific format. | 
 **transferable** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Format**](Format.md)

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

# **format_update_value**
> Format format_update_value(transferable=transferable, format=format)

[POST] /format/update/value

This will update a format's value, ie, a formats fragment or file depending on what is provided.  code/text fragment behavior: If this format is an asset.preview.base we will update the asset.original's value. if this format is an asset.preview.original we will update the asset.preview.base's value.  code/text file behavior: If the the format that is update is the asset.preview.base is a fragment and the asset.original is file then we will update the asset.original's value to be bytes or string respectively. This goes the same for orignal to preview but will be go the reverse order so if the original is a file we will update the preview base's fragment string.  image fragment/file: We will not modify preview -> orignal or original -> preview here. so there are zero side effects in this case, and will update as normal. (this will be the case for all other value updates.)

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.format import Format
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
    api_instance = openapi_client.FormatApi(api_client)
    transferable = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    format = openapi_client.Format() # Format | This is the format that you want to update. (optional)

    try:
        # [POST] /format/update/value
        api_response = api_instance.format_update_value(transferable=transferable, format=format)
        print("The response of FormatApi->format_update_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormatApi->format_update_value: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferable** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **format** | [**Format**](Format.md)| This is the format that you want to update. | [optional] 

### Return type

[**Format**](Format.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK, you will get an updated format. |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **format_usage_event**
> TrackedFormatEvent format_usage_event(seeded_tracked_format_event=seeded_tracked_format_event)

/format/usage/event [POST] Scoped to Format

This is an analytics endpoint that will enable us to know when a user has copied/downloaded/beamed/viewed a format.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.seeded_tracked_format_event import SeededTrackedFormatEvent
from openapi_client.models.tracked_format_event import TrackedFormatEvent
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
    api_instance = openapi_client.FormatApi(api_client)
    seeded_tracked_format_event = openapi_client.SeededTrackedFormatEvent() # SeededTrackedFormatEvent | This is a SeededTrackedFormatEvent, per tracked event:) (optional)

    try:
        # /format/usage/event [POST] Scoped to Format
        api_response = api_instance.format_usage_event(seeded_tracked_format_event=seeded_tracked_format_event)
        print("The response of FormatApi->format_usage_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormatApi->format_usage_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_tracked_format_event** | [**SeededTrackedFormatEvent**](SeededTrackedFormatEvent.md)| This is a SeededTrackedFormatEvent, per tracked event:) | [optional] 

### Return type

[**TrackedFormatEvent**](TrackedFormatEvent.md)

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

