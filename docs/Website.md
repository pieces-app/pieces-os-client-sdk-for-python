# Website

This is a specific model for related websites to an asset.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**id** | **str** |  | 
**interactions** | **int** | This is an optional value that will keep track of the number of times this has been interacted with. | [optional] 
**mechanisms** | [**Dict[str, MechanismEnum]**](MechanismEnum.md) | This is a Map&lt;String, MechanismEnum&gt; where the the key is an asset id. | [optional] 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**name** | **str** | This is a name that is customized. | 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**url** | **str** | this is the actual website url. | 

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


