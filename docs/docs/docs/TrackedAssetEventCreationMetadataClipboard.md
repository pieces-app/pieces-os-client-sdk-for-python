# TrackedAssetEventCreationMetadataClipboard

If an asset was created from a clipboard event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**keyboard** | **bool** | Whether the clipboard was utilized via the keyboard | [optional] 
**interaction** | **bool** | Whether the clipboard was extracted through a button click | [optional] 

## Example

```python
from openapi_client.models.tracked_asset_event_creation_metadata_clipboard import TrackedAssetEventCreationMetadataClipboard

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedAssetEventCreationMetadataClipboard from a JSON string
tracked_asset_event_creation_metadata_clipboard_instance = TrackedAssetEventCreationMetadataClipboard.from_json(json)
# print the JSON string representation of the object
print TrackedAssetEventCreationMetadataClipboard.to_json()

# convert the object into a dict
tracked_asset_event_creation_metadata_clipboard_dict = tracked_asset_event_creation_metadata_clipboard_instance.to_dict()
# create an instance of TrackedAssetEventCreationMetadataClipboard from a dict
tracked_asset_event_creation_metadata_clipboard_form_dict = tracked_asset_event_creation_metadata_clipboard.from_dict(tracked_asset_event_creation_metadata_clipboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


