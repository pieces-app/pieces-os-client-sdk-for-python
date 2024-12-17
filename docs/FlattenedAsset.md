# FlattenedAsset

An Asset Model representing data extracted from an Application connecting a group of data containing one or more Formats. [DAG Compatible - Directed Acyclic Graph Data Structure]  FlattenedAsset prevent Cycles in Reference because all outbound references are strings as opposed to crosspollinated objects.  i.e. FlattenedFormat.preview is Type String, and FlattenedFormat.original is Type String

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | [**FlattenedActivities**](FlattenedActivities.md) |  | [optional] 
**anchors** | [**FlattenedAnchors**](FlattenedAnchors.md) |  | [optional] 
**annotations** | [**FlattenedAnnotations**](FlattenedAnnotations.md) |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**creator** | **str** |  | 
**curated** | **bool** | This is an optional boolean that will flag that this asset came from a currated collection. | [optional] 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**demo** | **bool** | This will let us know if this asset was generated as a &#39;demo&#39; snippet | [optional] 
**discovered** | **bool** |  | [optional] 
**favorited** | **bool** |  | [optional] 
**formats** | [**FlattenedFormats**](FlattenedFormats.md) |  | 
**hints** | [**FlattenedHints**](FlattenedHints.md) |  | [optional] 
**id** | **str** | The globally available UID representing the asset in the Database, both locally and in the cloud. | 
**interacted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**mechanism** | [**MechanismEnum**](MechanismEnum.md) |  | 
**name** | **str** |  | [optional] 
**original** | **str** | An identifier of the format that is a reference to the original. | 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**preview** | [**FlattenedPreview**](FlattenedPreview.md) |  | 
**pseudo** | **bool** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**sensitives** | [**FlattenedSensitives**](FlattenedSensitives.md) |  | [optional] 
**shares** | [**FlattenedShares**](FlattenedShares.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**synced** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**tags** | [**FlattenedTags**](FlattenedTags.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_asset import FlattenedAsset

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedAsset from a JSON string
flattened_asset_instance = FlattenedAsset.from_json(json)
# print the JSON string representation of the object
print FlattenedAsset.to_json()

# convert the object into a dict
flattened_asset_dict = flattened_asset_instance.to_dict()
# create an instance of FlattenedAsset from a dict
flattened_asset_from_dict = FlattenedAsset.from_dict(flattened_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


