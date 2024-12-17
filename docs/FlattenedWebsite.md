# FlattenedWebsite

This is a specific model for related websites to an asset.[DAG SAFE]

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**id** | **str** | this is aspecific uuid that represents | 
**interactions** | **int** | This is an optional value that will keep track of the number of times this has been interacted with. | [optional] 
**mechanisms** | [**Dict[str, MechanismEnum]**](MechanismEnum.md) | This is a Map&lt;String, MechanismEnum&gt; where the the key is an asset id. | [optional] 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**name** | **str** | A customizable name. | 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**url** | **str** | The true url or the website. | 

## Example

```python
from pieces_os_client.models.flattened_website import FlattenedWebsite

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedWebsite from a JSON string
flattened_website_instance = FlattenedWebsite.from_json(json)
# print the JSON string representation of the object
print FlattenedWebsite.to_json()

# convert the object into a dict
flattened_website_dict = flattened_website_instance.to_dict()
# create an instance of FlattenedWebsite from a dict
flattened_website_from_dict = FlattenedWebsite.from_dict(flattened_website_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


