# Asset

An Asset Model representing data extracted from an Application connecting a group of data containing one or more Formats.  Below formats, preview, and original CAN to be pollinated (DAG Unsafe) because it is a root node and it's child leaf nodes will prevent cycles agressively.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | [**Activities**](Activities.md) |  | [optional] 
**anchors** | [**Anchors**](Anchors.md) |  | [optional] 
**annotations** | [**Annotations**](Annotations.md) |  | [optional] 
**conversations** | [**Conversations**](Conversations.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**creator** | **str** |  | 
**curated** | **bool** | This is an optional boolean that will flag that this asset came from a currated collection. | [optional] 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**demo** | **bool** | This will let us know if this asset was generated as a &#39;demo&#39; snippet | [optional] 
**discovered** | **bool** |  | [optional] 
**favorited** | **bool** |  | [optional] 
**formats** | [**Formats**](Formats.md) |  | 
**hints** | [**Hints**](Hints.md) |  | [optional] 
**id** | **str** | The globally available UID representing the asset in the Database, both locally and in the cloud. | 
**interacted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**mechanism** | [**MechanismEnum**](MechanismEnum.md) |  | 
**name** | **str** |  | [optional] 
**original** | [**ReferencedFormat**](ReferencedFormat.md) |  | 
**persons** | [**Persons**](Persons.md) |  | [optional] 
**preview** | [**Preview**](Preview.md) |  | 
**pseudo** | **bool** | This will determine if this is a asset that the user did not explicitly save. | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**sensitives** | [**Sensitives**](Sensitives.md) |  | [optional] 
**shares** | [**Shares**](Shares.md) |  | [optional] 
**summaries** | [**WorkstreamSummaries**](WorkstreamSummaries.md) |  | [optional] 
**synced** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**websites** | [**Websites**](Websites.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.asset import Asset

# TODO update the JSON string below
json = "{}"
# create an instance of Asset from a JSON string
asset_instance = Asset.from_json(json)
# print the JSON string representation of the object
print Asset.to_json()

# convert the object into a dict
asset_dict = asset_instance.to_dict()
# create an instance of Asset from a dict
asset_from_dict = Asset.from_dict(asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


