# TrackedAssetEventIdentifierDescriptionPairs

These are all of the available event types that are permitted in an object pair notation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**asset_created** | **str** | The key value pair for an asset being created. | [optional] [default to 'UNKNOWN']
**asset_viewed** | **str** | An asset was viewed | [optional] [default to 'UNKNOWN']
**asset_format_copied** | **str** | An asset&#39;s format was copied | [optional] [default to 'UNKNOWN']
**asset_format_downloaded** | **str** | An asset&#39;s format was downloaded | [optional] [default to 'UNKNOWN']
**asset_deleted** | **str** | An asset was deleted or not | [optional] [default to 'UNKNOWN']
**asset_description_updated** | **str** | An asset was redescribed by the user | [optional] [default to 'UNKNOWN']
**asset_name_updated** | **str** | An asset was renamed by the user | [optional] [default to 'UNKNOWN']
**asset_format_generic_classification_updated** | **str** | A generic classification was changed on a format within an asset | [optional] [default to 'UNKNOWN']
**asset_format_specific_classification_updated** | **str** | A specific classification was changed on a format within an asset | [optional] [default to 'UNKNOWN']
**asset_creation_failed** | **str** |  | [optional] [default to 'UNKNOWN']
**asset_tag_added** | **str** |  | [optional] [default to 'UNKNOWN']
**asset_link_added** | **str** |  | [optional] [default to 'UNKNOWN']
**asset_link_generated** | **str** | user generated a link for the asset | [optional] [default to 'UNKNOWN']
**asset_link_deleted** | **str** |  | [optional] [default to 'UNKNOWN']
**asset_tag_deleted** | **str** |  | [optional] [default to 'UNKNOWN']
**asset_updated** | **str** | This is just a generic string for an asset was updated. | [optional] [default to 'UNKNOWN']
**asset_format_value_edited** | **str** | This is a side effect event for a format value getting edited that exists on an asset. | [optional] [default to 'UNKNOWN']
**asset_format_updated** | **str** | This is a generic activity event for an asset getting updated because our format was updated for some reason. | [optional] [default to 'UNKNOWN']
**asset_link_revoked** | **str** | This means that a shareable link was revoked. | [optional] [default to 'UNKNOWN']
**asset_person_added** | **str** | This just means that a person was added via the user. | [optional] [default to 'UNKNOWN']
**asset_person_deleted** | **str** | This just means that a person was deleted via the user. | [optional] [default to 'UNKNOWN']
**asset_sensitive_added** | **str** | This just means that a sensitive was added via the user. | [optional] [default to 'UNKNOWN']
**asset_sensitive_deleted** | **str** | This just means that a sensitive was deleted via the user. | [optional] [default to 'UNKNOWN']
**suggested_asset_referenced** | **str** | This means that an asset was view/used while the user was looking at the suggestion view. | [optional] [default to 'UNKNOWN']
**searched_asset_referenced** | **str** | This means that an asset was view/used while the user was looking at the searching view. | [optional] [default to 'UNKNOWN']
**asset_referenced** | **str** | This means that an asset was view/used while the user was looking at the default view. | [optional] [default to 'UNKNOWN']
**activity_asset_referenced** | **str** | This means that a user referenced an asset by first clicking on an asset within an activity event.(ie from the activity view) | [optional] [default to 'UNKNOWN']
**asset_annotation_added** | **str** |  | [optional] [default to 'UNKNOWN']
**asset_annotation_deleted** | **str** |  | [optional] [default to 'UNKNOWN']
**asset_annotation_updated** | **str** |  | [optional] [default to 'UNKNOWN']
**asset_hint_added** | **str** |  | [optional] [default to 'UNKNOWN']
**asset_hint_deleted** | **str** |  | [optional] [default to 'UNKNOWN']
**asset_hint_updated** | **str** |  | [optional] [default to 'UNKNOWN']
**asset_anchor_added** | **str** |  | [optional] [default to 'UNKNOWN']
**asset_anchor_deleted** | **str** |  | [optional] [default to 'UNKNOWN']
**asset_anchor_updated** | **str** |  | [optional] [default to 'UNKNOWN']

## Example

```python
from pieces_os_client.models.tracked_asset_event_identifier_description_pairs import TrackedAssetEventIdentifierDescriptionPairs

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedAssetEventIdentifierDescriptionPairs from a JSON string
tracked_asset_event_identifier_description_pairs_instance = TrackedAssetEventIdentifierDescriptionPairs.from_json(json)
# print the JSON string representation of the object
print TrackedAssetEventIdentifierDescriptionPairs.to_json()

# convert the object into a dict
tracked_asset_event_identifier_description_pairs_dict = tracked_asset_event_identifier_description_pairs_instance.to_dict()
# create an instance of TrackedAssetEventIdentifierDescriptionPairs from a dict
tracked_asset_event_identifier_description_pairs_from_dict = TrackedAssetEventIdentifierDescriptionPairs.from_dict(tracked_asset_event_identifier_description_pairs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


