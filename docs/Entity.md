# Entity

An Entity represents either an Organization or a Team.   NOTE: org/team identifier will be present if it is a org vs a team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**InstanceConfiguration**](InstanceConfiguration.md) |  | 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**domains** | **List[str]** | List of associated domains for this entity | [optional] 
**id** | **str** | This will be a uuid | 
**name** | **str** | Display name of the entity | 
**org_identifier** | **str** | this is the id that represents the org in the user-team service | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**subscriptions** | [**FlattenedSubscriptions**](FlattenedSubscriptions.md) |  | [optional] 
**team_identifier** | **str** | this is the id that represents the org in the user-team service | [optional] 
**type** | [**EntityTypeEnum**](EntityTypeEnum.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**users** | [**FlattenedUsers**](FlattenedUsers.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.entity import Entity

# TODO update the JSON string below
json = "{}"
# create an instance of Entity from a JSON string
entity_instance = Entity.from_json(json)
# print the JSON string representation of the object
print(Entity.to_json())

# convert the object into a dict
entity_dict = entity_instance.to_dict()
# create an instance of Entity from a dict
entity_from_dict = Entity.from_dict(entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


