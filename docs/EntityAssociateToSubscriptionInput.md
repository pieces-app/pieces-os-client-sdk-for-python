# EntityAssociateToSubscriptionInput

NOTE: this is an optional body provided within the endpoint. This is the input model for associating an Entity with a Subscription.  This body is currently empty but can be extended in the future with additional metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.entity_associate_to_subscription_input import EntityAssociateToSubscriptionInput

# TODO update the JSON string below
json = "{}"
# create an instance of EntityAssociateToSubscriptionInput from a JSON string
entity_associate_to_subscription_input_instance = EntityAssociateToSubscriptionInput.from_json(json)
# print the JSON string representation of the object
print(EntityAssociateToSubscriptionInput.to_json())

# convert the object into a dict
entity_associate_to_subscription_input_dict = entity_associate_to_subscription_input_instance.to_dict()
# create an instance of EntityAssociateToSubscriptionInput from a dict
entity_associate_to_subscription_input_from_dict = EntityAssociateToSubscriptionInput.from_dict(entity_associate_to_subscription_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


