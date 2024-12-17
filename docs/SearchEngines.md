# SearchEngines

This is a model for plural Engine. This means that you can run multiple searches, this follow similar behavior to the Asset Filtering.where you can create you own complex operations: IE search a query in FTS, and filter all that have the create from here to here.  note: each Engine will only represent 1 search operation, however you many pass in operations to create further nesting. IE  Engine: [FTS + w/ operations: [created filter, updated filer, ncs Search] w/ a type of OR:::: This can be as nested as you want however will just increase the time till it returns results.]  note: type: default behavior for the type is an AND operation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[SearchEngine]**](SearchEngine.md) |  | 
**type** | [**FilterOperationTypeEnum**](FilterOperationTypeEnum.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.search_engines import SearchEngines

# TODO update the JSON string below
json = "{}"
# create an instance of SearchEngines from a JSON string
search_engines_instance = SearchEngines.from_json(json)
# print the JSON string representation of the object
print SearchEngines.to_json()

# convert the object into a dict
search_engines_dict = search_engines_instance.to_dict()
# create an instance of SearchEngines from a dict
search_engines_from_dict = SearchEngines.from_dict(search_engines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


