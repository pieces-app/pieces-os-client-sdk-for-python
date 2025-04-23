# pieces_os_client.AnnotationsApi

All URIs are relative to *http://localhost:1000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotations_create_new_annotation**](AnnotationsApi.md#annotations_create_new_annotation) | **POST** /annotations/create | /annotations/create [POST]
[**annotations_delete_specific_annotation**](AnnotationsApi.md#annotations_delete_specific_annotation) | **POST** /annotations/{annotation}/delete | /annotations/{annotation}/delete [POST]
[**annotations_snapshot**](AnnotationsApi.md#annotations_snapshot) | **GET** /annotations | /annotations [GET]
[**annotations_stream_identifiers**](AnnotationsApi.md#annotations_stream_identifiers) | **GET** /annotations/stream/identifiers | /annotations/stream/identifiers [WS]
[**search_annotations**](AnnotationsApi.md#search_annotations) | **POST** /annotations/search | /annotations/search [POST]


# **annotations_create_new_annotation**
> Annotation annotations_create_new_annotation(seeded_annotation=seeded_annotation)

/annotations/create [POST]

This will create an annotation.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.annotation import Annotation
from pieces_os_client.models.seeded_annotation import SeededAnnotation
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
    api_instance = pieces_os_client.AnnotationsApi(api_client)
    seeded_annotation = pieces_os_client.SeededAnnotation() # SeededAnnotation |  (optional)

    try:
        # /annotations/create [POST]
        api_response = api_instance.annotations_create_new_annotation(seeded_annotation=seeded_annotation)
        print("The response of AnnotationsApi->annotations_create_new_annotation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->annotations_create_new_annotation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seeded_annotation** | [**SeededAnnotation**](SeededAnnotation.md)|  | [optional] 

### Return type

[**Annotation**](Annotation.md)

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

# **annotations_delete_specific_annotation**
> annotations_delete_specific_annotation(annotation)

/annotations/{annotation}/delete [POST]

this will delete a specific annotation

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
    api_instance = pieces_os_client.AnnotationsApi(api_client)
    annotation = 'annotation_example' # str | This is a specific annotation uuid.

    try:
        # /annotations/{annotation}/delete [POST]
        api_instance.annotations_delete_specific_annotation(annotation)
    except Exception as e:
        print("Exception when calling AnnotationsApi->annotations_delete_specific_annotation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation** | **str**| This is a specific annotation uuid. | 

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

# **annotations_snapshot**
> Annotations annotations_snapshot(annotation_type_filter=annotation_type_filter)

/annotations [GET]

This will get a snapshot of all the annotations.

This will take an optional filter as a query param.

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.annotations import Annotations
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
    api_instance = pieces_os_client.AnnotationsApi(api_client)
    annotation_type_filter = 'annotation_type_filter_example' # str | This is an AnnotationTypeEnum as a optional filter. (optional)

    try:
        # /annotations [GET]
        api_response = api_instance.annotations_snapshot(annotation_type_filter=annotation_type_filter)
        print("The response of AnnotationsApi->annotations_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->annotations_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_type_filter** | **str**| This is an AnnotationTypeEnum as a optional filter. | [optional] 

### Return type

[**Annotations**](Annotations.md)

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

# **annotations_stream_identifiers**
> StreamedIdentifiers annotations_stream_identifiers()

/annotations/stream/identifiers [WS]

Provides a WebSocket connection that emits changes to your annotation identifiers (UUIDs).

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.streamed_identifiers import StreamedIdentifiers
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
    api_instance = pieces_os_client.AnnotationsApi(api_client)

    try:
        # /annotations/stream/identifiers [WS]
        api_response = api_instance.annotations_stream_identifiers()
        print("The response of AnnotationsApi->annotations_stream_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->annotations_stream_identifiers: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**StreamedIdentifiers**](StreamedIdentifiers.md)

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

# **search_annotations**
> SearchedAnnotations search_annotations(transferables=transferables, search_input=search_input)

/annotations/search [POST]

This will search your annotations for a specific annotation

note: we will just search the annotation value

### Example

* Api Key Authentication (application):
```python
import time
import os
import pieces_os_client
from pieces_os_client.models.search_input import SearchInput
from pieces_os_client.models.searched_annotations import SearchedAnnotations
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
    api_instance = pieces_os_client.AnnotationsApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    search_input = pieces_os_client.SearchInput() # SearchInput |  (optional)

    try:
        # /annotations/search [POST]
        api_response = api_instance.search_annotations(transferables=transferables, search_input=search_input)
        print("The response of AnnotationsApi->search_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnotationsApi->search_annotations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **search_input** | [**SearchInput**](SearchInput.md)|  | [optional] 

### Return type

[**SearchedAnnotations**](SearchedAnnotations.md)

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

