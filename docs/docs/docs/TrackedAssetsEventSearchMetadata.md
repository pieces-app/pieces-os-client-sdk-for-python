# TrackedAssetsEventSearchMetadata

Metadata attached to a search event on an Asset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**query** | **str** | The search query itself | [optional] 
**results** | [**TrackedAssetsEventSearchMetadataResults**](TrackedAssetsEventSearchMetadataResults.md) |  | [optional] 

## Example

```python
from openapi_client.models.tracked_assets_event_search_metadata import TrackedAssetsEventSearchMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedAssetsEventSearchMetadata from a JSON string
tracked_assets_event_search_metadata_instance = TrackedAssetsEventSearchMetadata.from_json(json)
# print the JSON string representation of the object
print TrackedAssetsEventSearchMetadata.to_json()

# convert the object into a dict
tracked_assets_event_search_metadata_dict = tracked_assets_event_search_metadata_instance.to_dict()
# create an instance of TrackedAssetsEventSearchMetadata from a dict
tracked_assets_event_search_metadata_form_dict = tracked_assets_event_search_metadata.from_dict(tracked_assets_event_search_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


