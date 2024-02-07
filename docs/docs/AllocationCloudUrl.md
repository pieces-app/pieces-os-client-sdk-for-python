# AllocationCloudUrl

This is one of the 3 possible urls that will route to your cloud :).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**status** | [**AllocationStatusEnum**](AllocationStatusEnum.md) |  | 
**url** | **str** | this is the base url that is used to communicat with your vpc. | 

## Example

```python
from openapi_client.models.allocation_cloud_url import AllocationCloudUrl

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationCloudUrl from a JSON string
allocation_cloud_url_instance = AllocationCloudUrl.from_json(json)
# print the JSON string representation of the object
print AllocationCloudUrl.to_json()

# convert the object into a dict
allocation_cloud_url_dict = allocation_cloud_url_instance.to_dict()
# create an instance of AllocationCloudUrl from a dict
allocation_cloud_url_form_dict = allocation_cloud_url.from_dict(allocation_cloud_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


