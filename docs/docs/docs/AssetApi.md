# openapi_client.AssetApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_associate_tag**](AssetApi.md#asset_associate_tag) | **POST** /asset/{asset}/tags/associate/{tag} | /asset/{asset}/tags/associate/{tag} [POST]
[**asset_associate_website**](AssetApi.md#asset_associate_website) | **POST** /asset/{asset}/websites/associate/{website} | /asset/{asset}/websites/associate/{website} [POST]
[**asset_disassociate_tag**](AssetApi.md#asset_disassociate_tag) | **POST** /asset/{asset}/tags/disassociate/{tag} | /asset/{asset}/tags/disassociate/{tag} [POST]
[**asset_disassociate_website**](AssetApi.md#asset_disassociate_website) | **POST** /asset/{asset}/websites/disassociate/{website} | /asset/{asset}/websites/disassociate/{website} [POST]
[**asset_formats**](AssetApi.md#asset_formats) | **GET** /asset/{asset}/formats | /asset/{asset}/formats [GET] Scoped To Asset
[**asset_reclassify**](AssetApi.md#asset_reclassify) | **POST** /asset/reclassify | /asset/reclassify [POST]
[**asset_scores_increment**](AssetApi.md#asset_scores_increment) | **POST** /asset/{asset}/scores/increment | &#39;/asset/{asset}/scores/increment&#39; [POST]
[**asset_snapshot**](AssetApi.md#asset_snapshot) | **GET** /asset/{asset} | /asset/{asset} [GET] Scoped To Asset
[**asset_snapshot_post**](AssetApi.md#asset_snapshot_post) | **POST** /asset/{asset} | /asset/{asset} [POST] Scoped to an Asset
[**asset_specific_asset_activities**](AssetApi.md#asset_specific_asset_activities) | **GET** /asset/{asset}/activities | /asset/{asset}/activities [GET]
[**asset_specific_asset_conversations**](AssetApi.md#asset_specific_asset_conversations) | **GET** /asset/{asset}/conversations | /asset/{asset}/conversations [GET]
[**asset_specific_asset_export**](AssetApi.md#asset_specific_asset_export) | **GET** /asset/{asset}/export | [GET] /asset/{asset}/export
[**asset_update**](AssetApi.md#asset_update) | **POST** /asset/update | /asset/update [POST] Scoped to Asset


# **asset_associate_tag**
> asset_associate_tag(asset, tag)

/asset/{asset}/tags/associate/{tag} [POST]

This will associate a tag with a asset. This will do the same thing as the tag equivilant.

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
    api_instance = openapi_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    tag = 'tag_example' # str | tag id

    try:
        # /asset/{asset}/tags/associate/{tag} [POST]
        api_instance.asset_associate_tag(asset, tag)
    except Exception as e:
        print("Exception when calling AssetApi->asset_associate_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **tag** | **str**| tag id | 

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

# **asset_associate_website**
> asset_associate_website(asset, website)

/asset/{asset}/websites/associate/{website} [POST]

This will associate a website with a asset. This will do the same thing as the website equivilant.

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
    api_instance = openapi_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    website = 'website_example' # str | website id

    try:
        # /asset/{asset}/websites/associate/{website} [POST]
        api_instance.asset_associate_website(asset, website)
    except Exception as e:
        print("Exception when calling AssetApi->asset_associate_website: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **website** | **str**| website id | 

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

# **asset_disassociate_tag**
> asset_disassociate_tag(tag, asset)

/asset/{asset}/tags/disassociate/{tag} [POST]

This will enable us to dissassociate a tag from a asset. This will do the same thing as the tag equivilant.

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
    api_instance = openapi_client.AssetApi(api_client)
    tag = 'tag_example' # str | tag id
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /asset/{asset}/tags/disassociate/{tag} [POST]
        api_instance.asset_disassociate_tag(tag, asset)
    except Exception as e:
        print("Exception when calling AssetApi->asset_disassociate_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| tag id | 
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 

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

# **asset_disassociate_website**
> asset_disassociate_website(website, asset)

/asset/{asset}/websites/disassociate/{website} [POST]

This will enable us to dissassociate a website from a asset. This will do the same thing as the website equivilant.

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
    api_instance = openapi_client.AssetApi(api_client)
    website = 'website_example' # str | website id
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /asset/{asset}/websites/disassociate/{website} [POST]
        api_instance.asset_disassociate_website(website, asset)
    except Exception as e:
        print("Exception when calling AssetApi->asset_disassociate_website: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website** | **str**| website id | 
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 

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

# **asset_formats**
> Formats asset_formats(asset, transferables=transferables)

/asset/{asset}/formats [GET] Scoped To Asset

Get the formats for a given asset.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.formats import Formats
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
    api_instance = openapi_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /asset/{asset}/formats [GET] Scoped To Asset
        api_response = api_instance.asset_formats(asset, transferables=transferables)
        print("The response of AssetApi->asset_formats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_formats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Formats**](Formats.md)

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

# **asset_reclassify**
> Asset asset_reclassify(transferables=transferables, asset_reclassification=asset_reclassification)

/asset/reclassify [POST]

This will update the classification of this asset to the proper classification.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.asset import Asset
from openapi_client.models.asset_reclassification import AssetReclassification
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
    api_instance = openapi_client.AssetApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    asset_reclassification = openapi_client.AssetReclassification() # AssetReclassification | This will accept a Reclassification that includeds and assetand a language that this assets needs to be reclassified to. We will just return an Asset that has been reclassified. (optional)

    try:
        # /asset/reclassify [POST]
        api_response = api_instance.asset_reclassify(transferables=transferables, asset_reclassification=asset_reclassification)
        print("The response of AssetApi->asset_reclassify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_reclassify: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **asset_reclassification** | [**AssetReclassification**](AssetReclassification.md)| This will accept a Reclassification that includeds and assetand a language that this assets needs to be reclassified to. We will just return an Asset that has been reclassified. | [optional] 

### Return type

[**Asset**](Asset.md)

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

# **asset_scores_increment**
> asset_scores_increment(asset, seeded_score_increment=seeded_score_increment)

'/asset/{asset}/scores/increment' [POST]

This will take in a SeededScoreIncrement and will increment the material relative to the incoming body.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.seeded_score_increment import SeededScoreIncrement
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
    api_instance = openapi_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    seeded_score_increment = openapi_client.SeededScoreIncrement() # SeededScoreIncrement |  (optional)

    try:
        # '/asset/{asset}/scores/increment' [POST]
        api_instance.asset_scores_increment(asset, seeded_score_increment=seeded_score_increment)
    except Exception as e:
        print("Exception when calling AssetApi->asset_scores_increment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **seeded_score_increment** | [**SeededScoreIncrement**](SeededScoreIncrement.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_snapshot**
> Asset asset_snapshot(asset, transferables=transferables)

/asset/{asset} [GET] Scoped To Asset

Get the snapshot of a specific asset.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.asset import Asset
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
    api_instance = openapi_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /asset/{asset} [GET] Scoped To Asset
        api_response = api_instance.asset_snapshot(asset, transferables=transferables)
        print("The response of AssetApi->asset_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**410** | Asset no longer exists and is Gone. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_snapshot_post**
> Asset asset_snapshot_post(asset, transferables=transferables, seeded_accessor=seeded_accessor)

/asset/{asset} [POST] Scoped to an Asset

Get the snapshot of a specific asset. by passing over as well the user who is getting the snapshot.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.asset import Asset
from openapi_client.models.seeded_accessor import SeededAccessor
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
    api_instance = openapi_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    seeded_accessor = openapi_client.SeededAccessor() # SeededAccessor |  (optional)

    try:
        # /asset/{asset} [POST] Scoped to an Asset
        api_response = api_instance.asset_snapshot_post(asset, transferables=transferables, seeded_accessor=seeded_accessor)
        print("The response of AssetApi->asset_snapshot_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_snapshot_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **seeded_accessor** | [**SeededAccessor**](SeededAccessor.md)|  | [optional] 

### Return type

[**Asset**](Asset.md)

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

# **asset_specific_asset_activities**
> Activities asset_specific_asset_activities(asset, transferables=transferables)

/asset/{asset}/activities [GET]

This will get a specific asset's activity events

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.activities import Activities
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
    api_instance = openapi_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /asset/{asset}/activities [GET]
        api_response = api_instance.asset_specific_asset_activities(asset, transferables=transferables)
        print("The response of AssetApi->asset_specific_asset_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_specific_asset_activities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Activities**](Activities.md)

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

# **asset_specific_asset_conversations**
> Conversations asset_specific_asset_conversations(asset, transferables=transferables)

/asset/{asset}/conversations [GET]

This will get a specific asset's conversations

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.conversations import Conversations
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
    api_instance = openapi_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)

    try:
        # /asset/{asset}/conversations [GET]
        api_response = api_instance.asset_specific_asset_conversations(asset, transferables=transferables)
        print("The response of AssetApi->asset_specific_asset_conversations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_specific_asset_conversations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 

### Return type

[**Conversations**](Conversations.md)

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

# **asset_specific_asset_export**
> ExportedAsset asset_specific_asset_export(asset, export_type)

[GET] /asset/{asset}/export

This will return a export version of your asset.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.exported_asset import ExportedAsset
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
    api_instance = openapi_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    export_type = 'export_type_example' # str | This specifies the type of export the user wants.

    try:
        # [GET] /asset/{asset}/export
        api_response = api_instance.asset_specific_asset_export(asset, export_type)
        print("The response of AssetApi->asset_specific_asset_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_specific_asset_export: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| The id (uuid) of the asset that you are trying to access. | 
 **export_type** | **str**| This specifies the type of export the user wants. | 

### Return type

[**ExportedAsset**](ExportedAsset.md)

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

# **asset_update**
> Asset asset_update(transferables=transferables, asset=asset)

/asset/update [POST] Scoped to Asset

This endpoint will accept an Asset that the user wants to update, and will return the a full Asset that was updated!

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.asset import Asset
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
    api_instance = openapi_client.AssetApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    asset = openapi_client.Asset() # Asset | This is the updated Asset that needs to be updated in our db. (optional)

    try:
        # /asset/update [POST] Scoped to Asset
        api_response = api_instance.asset_update(transferables=transferables, asset=asset)
        print("The response of AssetApi->asset_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferables** | **bool**| This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) | [optional] 
 **asset** | [**Asset**](Asset.md)| This is the updated Asset that needs to be updated in our db. | [optional] 

### Return type

[**Asset**](Asset.md)

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

