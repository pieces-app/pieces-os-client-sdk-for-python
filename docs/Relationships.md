# Relationships


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[Relationship]**](Relationship.md) |  | 

## Example

```python
from pieces_os_client.models.relationships import Relationships

# TODO update the JSON string below
json = "{}"
# create an instance of Relationships from a JSON string
relationships_instance = Relationships.from_json(json)
# print the JSON string representation of the object
print Relationships.to_json()

# convert the object into a dict
relationships_dict = relationships_instance.to_dict()
# create an instance of Relationships from a dict
relationships_from_dict = Relationships.from_dict(relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


