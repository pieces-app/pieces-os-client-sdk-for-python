# FlattenedSubscriptions

This is the referenced subscriptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an subscription. | [optional] 
**iterable** | [**List[ReferencedSubscription]**](ReferencedSubscription.md) | This is the iterable of the referenced subscriptions | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_subscriptions import FlattenedSubscriptions

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedSubscriptions from a JSON string
flattened_subscriptions_instance = FlattenedSubscriptions.from_json(json)
# print the JSON string representation of the object
print(FlattenedSubscriptions.to_json())

# convert the object into a dict
flattened_subscriptions_dict = flattened_subscriptions_instance.to_dict()
# create an instance of FlattenedSubscriptions from a dict
flattened_subscriptions_from_dict = FlattenedSubscriptions.from_dict(flattened_subscriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


