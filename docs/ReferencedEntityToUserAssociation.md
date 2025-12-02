# ReferencedEntityToUserAssociation

A minimal reference to an EntityToUserAssociation with optional flattened data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The UUID of the association | 
**reference** | [**FlattenedEntityToUserAssociation**](FlattenedEntityToUserAssociation.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.referenced_entity_to_user_association import ReferencedEntityToUserAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedEntityToUserAssociation from a JSON string
referenced_entity_to_user_association_instance = ReferencedEntityToUserAssociation.from_json(json)
# print the JSON string representation of the object
print(ReferencedEntityToUserAssociation.to_json())

# convert the object into a dict
referenced_entity_to_user_association_dict = referenced_entity_to_user_association_instance.to_dict()
# create an instance of ReferencedEntityToUserAssociation from a dict
referenced_entity_to_user_association_from_dict = ReferencedEntityToUserAssociation.from_dict(referenced_entity_to_user_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


