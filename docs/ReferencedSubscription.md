# ReferencedSubscription

A minimal reference to a Subscription, with just an id and an optional reference to the FlattenedSubscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**reference** | [**FlattenedSubscription**](FlattenedSubscription.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.referenced_subscription import ReferencedSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedSubscription from a JSON string
referenced_subscription_instance = ReferencedSubscription.from_json(json)
# print the JSON string representation of the object
print(ReferencedSubscription.to_json())

# convert the object into a dict
referenced_subscription_dict = referenced_subscription_instance.to_dict()
# create an instance of ReferencedSubscription from a dict
referenced_subscription_from_dict = ReferencedSubscription.from_dict(referenced_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


