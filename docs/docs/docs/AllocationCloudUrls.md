# AllocationCloudUrls

you will have at minimum 2 urls,  base: is the default url of your cloud.  id: is the branded url, uuid.pieces.cloud.  (optional) vanity: is the custom branded url, mark.pieces.cloud

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**base** | [**AllocationCloudUrl**](AllocationCloudUrl.md) |  | 
**id** | [**AllocationCloudUrl**](AllocationCloudUrl.md) |  | 
**vanity** | [**AllocationCloudUrl**](AllocationCloudUrl.md) |  | [optional] 

## Example

```python
from openapi_client.models.allocation_cloud_urls import AllocationCloudUrls

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationCloudUrls from a JSON string
allocation_cloud_urls_instance = AllocationCloudUrls.from_json(json)
# print the JSON string representation of the object
print AllocationCloudUrls.to_json()

# convert the object into a dict
allocation_cloud_urls_dict = allocation_cloud_urls_instance.to_dict()
# create an instance of AllocationCloudUrls from a dict
allocation_cloud_urls_form_dict = allocation_cloud_urls.from_dict(allocation_cloud_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


