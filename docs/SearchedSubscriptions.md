# SearchedSubscriptions

This is the searched subscriptions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[SearchedSubscription]**](SearchedSubscription.md) | This is the iterable of the searched subscriptions | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.searched_subscriptions import SearchedSubscriptions

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedSubscriptions from a JSON string
searched_subscriptions_instance = SearchedSubscriptions.from_json(json)
# print the JSON string representation of the object
print(SearchedSubscriptions.to_json())

# convert the object into a dict
searched_subscriptions_dict = searched_subscriptions_instance.to_dict()
# create an instance of SearchedSubscriptions from a dict
searched_subscriptions_from_dict = SearchedSubscriptions.from_dict(searched_subscriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


