# FlattenedEntityToSubscriptionAssociation

This is a DAG-Safe minimal representation of an entity-to-subscription association.  note: this is done with light weight properties at the top level for fast queries  entity,subscription: light weight string references

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**entity** | **str** | Entity UUID | 
**id** | **str** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**subscription** | **str** | Subscription UUID | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 

## Example

```python
from pieces_os_client.models.flattened_entity_to_subscription_association import FlattenedEntityToSubscriptionAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedEntityToSubscriptionAssociation from a JSON string
flattened_entity_to_subscription_association_instance = FlattenedEntityToSubscriptionAssociation.from_json(json)
# print the JSON string representation of the object
print(FlattenedEntityToSubscriptionAssociation.to_json())

# convert the object into a dict
flattened_entity_to_subscription_association_dict = flattened_entity_to_subscription_association_instance.to_dict()
# create an instance of FlattenedEntityToSubscriptionAssociation from a dict
flattened_entity_to_subscription_association_from_dict = FlattenedEntityToSubscriptionAssociation.from_dict(flattened_entity_to_subscription_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


