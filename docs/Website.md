# Website

This is a specific model for related websites to an asset.  NOTE: website <> source window displays a many to many relationship, however is a 1 to 1 relationship with logic built in to ensure that this remains a 1 to one relationship. Please take a look at the the workstreamEvent creation(specifically when creating a website <> source window relationship), as well as the associate for a website <> a source window, This will ensure that we only ever have a single website, this will update the website if the time stamp if we are seeing the website again and as well update the source windows name as well if this is different so that is is only ever possible to have a website<>sourceWindow where a website can only ever have 1 source window.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | 
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**url** | **str** | this is the actual website url. | 
**name** | **str** | This is a name that is customized. | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**mechanisms** | [**Dict[str, MechanismEnum]**](MechanismEnum.md) | This is a Map&lt;String, MechanismEnum&gt; where the the key is an asset id. | [optional] 
**interactions** | **int** | This is an optional value that will keep track of the number of times this has been interacted with. | [optional] 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**annotations** | [**FlattenedAnnotations**](FlattenedAnnotations.md) |  | [optional] 
**workstream_events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 
**sources** | [**FlattenedIdentifiedWorkstreamPatternEngineSources**](FlattenedIdentifiedWorkstreamPatternEngineSources.md) |  | [optional] 
**source_windows** | [**FlattenedWorkstreamPatternEngineSourceWindows**](FlattenedWorkstreamPatternEngineSourceWindows.md) |  | [optional] 
**tags** | [**FlattenedTags**](FlattenedTags.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.website import Website

# TODO update the JSON string below
json = "{}"
# create an instance of Website from a JSON string
website_instance = Website.from_json(json)
# print the JSON string representation of the object
print Website.to_json()

# convert the object into a dict
website_dict = website_instance.to_dict()
# create an instance of Website from a dict
website_from_dict = Website.from_dict(website_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


