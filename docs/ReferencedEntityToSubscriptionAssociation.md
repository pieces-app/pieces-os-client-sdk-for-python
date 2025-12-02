# ReferencedEntityToSubscriptionAssociation

A minimal reference to an EntityToSubscriptionAssociation with optional flattened data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The UUID of the association | 
**reference** | [**FlattenedEntityToSubscriptionAssociation**](FlattenedEntityToSubscriptionAssociation.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.referenced_entity_to_subscription_association import ReferencedEntityToSubscriptionAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedEntityToSubscriptionAssociation from a JSON string
referenced_entity_to_subscription_association_instance = ReferencedEntityToSubscriptionAssociation.from_json(json)
# print the JSON string representation of the object
print(ReferencedEntityToSubscriptionAssociation.to_json())

# convert the object into a dict
referenced_entity_to_subscription_association_dict = referenced_entity_to_subscription_association_instance.to_dict()
# create an instance of ReferencedEntityToSubscriptionAssociation from a dict
referenced_entity_to_subscription_association_from_dict = ReferencedEntityToSubscriptionAssociation.from_dict(referenced_entity_to_subscription_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


