# openapi_client.AnnotationsApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotations_create_new_annotation**](AnnotationsApi.md#annotations_create_new_annotation) | **POST** /annotations/create | /annotations/create [POST]
[**annotations_delete_specific_annotation**](AnnotationsApi.md#annotations_delete_specific_annotation) | **POST** /annotations/{annotation}/delete | /annotations/{annotation}/delete [POST]
[**annotations_snapshot**](AnnotationsApi.md#annotations_snapshot) | **GET** /annotations | /annotations [GET]


# **annotations_create_new_annotation**
> Annotation annotations_create_new_annotation(seeded_annotation=seeded_annotation)

/annotations/create [POST]

This will create an annotation.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.annotation import Annotation
from openapi_client.models.seeded_annotation import SeededAnnotation
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
    api_instance = openapi_client.AnnotationsApi(api_client)
    seeded_annotation = openapi_client.SeededAnnotation() # SeededAnnotation |  (optional)

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

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

```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.AnnotationsApi(api_client)
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

# **annotations_snapshot**
> Annotations annotations_snapshot(annotation_type_filter=annotation_type_filter)

/annotations [GET]

This will get a snapshot of all the annotations.  This will take an optional filter as a query param.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.annotations import Annotations
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
    api_instance = openapi_client.AnnotationsApi(api_client)
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

