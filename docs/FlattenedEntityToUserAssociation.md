# FlattenedEntityToUserAssociation

This is a DAG-Safe minimal representation of an entity-to-user association.  note: this is done with light weight properties at the top level for fast queries  entity,user: light weight string references

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**entity** | **str** | Entity UUID | 
**id** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**user** | **str** | User UUID | 

## Example

```python
from pieces_os_client.models.flattened_entity_to_user_association import FlattenedEntityToUserAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedEntityToUserAssociation from a JSON string
flattened_entity_to_user_association_instance = FlattenedEntityToUserAssociation.from_json(json)
# print the JSON string representation of the object
print(FlattenedEntityToUserAssociation.to_json())

# convert the object into a dict
flattened_entity_to_user_association_dict = flattened_entity_to_user_association_instance.to_dict()
# create an instance of FlattenedEntityToUserAssociation from a dict
flattened_entity_to_user_association_from_dict = FlattenedEntityToUserAssociation.from_dict(flattened_entity_to_user_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


