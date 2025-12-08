# ReferencedEntity

A minimal reference to an Entity with optional flattened data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The UUID of the entity | 
**reference** | [**FlattenedEntity**](FlattenedEntity.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.referenced_entity import ReferencedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedEntity from a JSON string
referenced_entity_instance = ReferencedEntity.from_json(json)
# print the JSON string representation of the object
print(ReferencedEntity.to_json())

# convert the object into a dict
referenced_entity_dict = referenced_entity_instance.to_dict()
# create an instance of ReferencedEntity from a dict
referenced_entity_from_dict = ReferencedEntity.from_dict(referenced_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


