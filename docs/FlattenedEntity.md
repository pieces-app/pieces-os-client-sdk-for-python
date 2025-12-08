# FlattenedEntity

This is a DAG-Safe minimal representation of an Entity to prevent circular dependencies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**InstanceConfiguration**](InstanceConfiguration.md) |  | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**org_identifier** | **str** | this is the id that represents the org in the user-team service | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**subscriptions** | [**FlattenedSubscriptions**](FlattenedSubscriptions.md) |  | [optional] 
**team_identifier** | **str** | this is the id that represents the team in the user-team service | [optional] 
**type** | [**EntityTypeEnum**](EntityTypeEnum.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**users** | [**FlattenedUsers**](FlattenedUsers.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_entity import FlattenedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedEntity from a JSON string
flattened_entity_instance = FlattenedEntity.from_json(json)
# print the JSON string representation of the object
print(FlattenedEntity.to_json())

# convert the object into a dict
flattened_entity_dict = flattened_entity_instance.to_dict()
# create an instance of FlattenedEntity from a dict
flattened_entity_from_dict = FlattenedEntity.from_dict(flattened_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


