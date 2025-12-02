# SeededEntity

This is the minimum information required to create a new entity. You must specify the type (ORGANIZATION or TEAM) and provide a name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**InstanceConfiguration**](InstanceConfiguration.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**domains** | **List[str]** | Optional list of associated domains for this entity | [optional] 
**name** | **str** | Display name of the entity | 
**org_identifier** | **str** | this is the id that represents the org in the user-team service | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**team_identifier** | **str** | this is the id that represents the team in the user-team service | [optional] 
**type** | [**EntityTypeEnum**](EntityTypeEnum.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_entity import SeededEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SeededEntity from a JSON string
seeded_entity_instance = SeededEntity.from_json(json)
# print the JSON string representation of the object
print(SeededEntity.to_json())

# convert the object into a dict
seeded_entity_dict = seeded_entity_instance.to_dict()
# create an instance of SeededEntity from a dict
seeded_entity_from_dict = SeededEntity.from_dict(seeded_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


