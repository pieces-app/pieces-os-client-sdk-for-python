# FlattenedEntities

This is a DAG-Safe collection of Entity references.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the key is an entity id. | [optional] 
**iterable** | [**List[ReferencedEntity]**](ReferencedEntity.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_entities import FlattenedEntities

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedEntities from a JSON string
flattened_entities_instance = FlattenedEntities.from_json(json)
# print the JSON string representation of the object
print(FlattenedEntities.to_json())

# convert the object into a dict
flattened_entities_dict = flattened_entities_instance.to_dict()
# create an instance of FlattenedEntities from a dict
flattened_entities_from_dict = FlattenedEntities.from_dict(flattened_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


