# openapi_client.DiscoveryApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discovery_discover_assets**](DiscoveryApi.md#discovery_discover_assets) | **POST** /discovery/discover/assets | /discovery/discover/assets [POST]
[**discovery_discover_assets_html**](DiscoveryApi.md#discovery_discover_assets_html) | **POST** /discovery/discover/assets/html | /discovery/discover/assets/html[POST]
[**discovery_discover_sensitives**](DiscoveryApi.md#discovery_discover_sensitives) | **POST** /discovery/discover/sensitives | /discovery/discover/sensitives [POST]
[**discovery_discover_tags_related**](DiscoveryApi.md#discovery_discover_tags_related) | **POST** /discovery/discover/tags/related | /discovery/discover/tags/related [POST]


# **discovery_discover_assets**
> DiscoveredAssets discovery_discover_assets(automatic=automatic, seeded_discoverable_assets=seeded_discoverable_assets)

/discovery/discover/assets [POST]

This is the endpoint used for bulk import. In both cases of the bulk import flow, fragments or files. When we already have \"snippets\" or fragments to discover and now our job is to check if they are actually valid snippets(clustering). Otherwise, we should have a file to parse && snippitize and then run through the clustering.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.discovered_assets import DiscoveredAssets
from openapi_client.models.seeded_discoverable_assets import SeededDiscoverableAssets
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
    api_instance = openapi_client.DiscoveryApi(api_client)
    automatic = True # bool | For most cases set to true. If this is set to true we will handle the behavior automically or else we will not proactively handle specific behavior but we will let the developer decide the behavior. (optional) (default to True)
    seeded_discoverable_assets = openapi_client.SeededDiscoverableAssets() # SeededDiscoverableAssets | The discovery/discover/assets endpoint will accept seededDiscoverableAssets, that represetns an iterable of multiple fragments or files. (optional)

    try:
        # /discovery/discover/assets [POST]
        api_response = api_instance.discovery_discover_assets(automatic=automatic, seeded_discoverable_assets=seeded_discoverable_assets)
        print("The response of DiscoveryApi->discovery_discover_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->discovery_discover_assets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automatic** | **bool**| For most cases set to true. If this is set to true we will handle the behavior automically or else we will not proactively handle specific behavior but we will let the developer decide the behavior. | [optional] [default to True]
 **seeded_discoverable_assets** | [**SeededDiscoverableAssets**](SeededDiscoverableAssets.md)| The discovery/discover/assets endpoint will accept seededDiscoverableAssets, that represetns an iterable of multiple fragments or files. | [optional] 

### Return type

[**DiscoveredAssets**](DiscoveredAssets.md)

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

# **discovery_discover_assets_html**
> DiscoveredHtmlWebpages discovery_discover_assets_html(automatic=automatic, seeded_discoverable_html_webpages=seeded_discoverable_html_webpages)

/discovery/discover/assets/html[POST]

This is the discover discover assets html endpoint. The goal of this endpoint is to either take an iterable of urls and pages(an html string) and extract all the assets from the iterable.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.discovered_html_webpages import DiscoveredHtmlWebpages
from openapi_client.models.seeded_discoverable_html_webpages import SeededDiscoverableHtmlWebpages
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
    api_instance = openapi_client.DiscoveryApi(api_client)
    automatic = True # bool | For most cases set to true. If this is set to true we will handle the behavior automically or else we will not proactively handle specific behavior but we will let the developer decide the behavior. (optional) (default to True)
    seeded_discoverable_html_webpages = openapi_client.SeededDiscoverableHtmlWebpages() # SeededDiscoverableHtmlWebpages |  (optional)

    try:
        # /discovery/discover/assets/html[POST]
        api_response = api_instance.discovery_discover_assets_html(automatic=automatic, seeded_discoverable_html_webpages=seeded_discoverable_html_webpages)
        print("The response of DiscoveryApi->discovery_discover_assets_html:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->discovery_discover_assets_html: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automatic** | **bool**| For most cases set to true. If this is set to true we will handle the behavior automically or else we will not proactively handle specific behavior but we will let the developer decide the behavior. | [optional] [default to True]
 **seeded_discoverable_html_webpages** | [**SeededDiscoverableHtmlWebpages**](SeededDiscoverableHtmlWebpages.md)|  | [optional] 

### Return type

[**DiscoveredHtmlWebpages**](DiscoveredHtmlWebpages.md)

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

# **discovery_discover_sensitives**
> DiscoveredSensitives discovery_discover_sensitives(automatic=automatic, seeded_discoverable_sensitives=seeded_discoverable_sensitives)

/discovery/discover/sensitives [POST]

This endpoint will accept an array of text values, and attampt to extract sensitive data out of it.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.discovered_sensitives import DiscoveredSensitives
from openapi_client.models.seeded_discoverable_sensitives import SeededDiscoverableSensitives
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
    api_instance = openapi_client.DiscoveryApi(api_client)
    automatic = True # bool | For most cases set to true. If this is set to true we will handle the behavior automically or else we will not proactively handle specific behavior but we will let the developer decide the behavior. (optional) (default to True)
    seeded_discoverable_sensitives = openapi_client.SeededDiscoverableSensitives() # SeededDiscoverableSensitives |  (optional)

    try:
        # /discovery/discover/sensitives [POST]
        api_response = api_instance.discovery_discover_sensitives(automatic=automatic, seeded_discoverable_sensitives=seeded_discoverable_sensitives)
        print("The response of DiscoveryApi->discovery_discover_sensitives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->discovery_discover_sensitives: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automatic** | **bool**| For most cases set to true. If this is set to true we will handle the behavior automically or else we will not proactively handle specific behavior but we will let the developer decide the behavior. | [optional] [default to True]
 **seeded_discoverable_sensitives** | [**SeededDiscoverableSensitives**](SeededDiscoverableSensitives.md)|  | [optional] 

### Return type

[**DiscoveredSensitives**](DiscoveredSensitives.md)

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

# **discovery_discover_tags_related**
> DiscoveredRelatedTags discovery_discover_tags_related(automatic=automatic, seeded_discoverable_related_tags=seeded_discoverable_related_tags)

/discovery/discover/tags/related [POST]

This will take in a tag or multiple tags and return all the tags that are related to the tag or tag provide in the body.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.discovered_related_tags import DiscoveredRelatedTags
from openapi_client.models.seeded_discoverable_related_tags import SeededDiscoverableRelatedTags
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
    api_instance = openapi_client.DiscoveryApi(api_client)
    automatic = True # bool | For most cases set to true. If this is set to true we will handle the behavior automically or else we will not proactively handle specific behavior but we will let the developer decide the behavior. (optional) (default to True)
    seeded_discoverable_related_tags = openapi_client.SeededDiscoverableRelatedTags() # SeededDiscoverableRelatedTags |  (optional)

    try:
        # /discovery/discover/tags/related [POST]
        api_response = api_instance.discovery_discover_tags_related(automatic=automatic, seeded_discoverable_related_tags=seeded_discoverable_related_tags)
        print("The response of DiscoveryApi->discovery_discover_tags_related:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryApi->discovery_discover_tags_related: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automatic** | **bool**| For most cases set to true. If this is set to true we will handle the behavior automically or else we will not proactively handle specific behavior but we will let the developer decide the behavior. | [optional] [default to True]
 **seeded_discoverable_related_tags** | [**SeededDiscoverableRelatedTags**](SeededDiscoverableRelatedTags.md)|  | [optional] 

### Return type

[**DiscoveredRelatedTags**](DiscoveredRelatedTags.md)

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

