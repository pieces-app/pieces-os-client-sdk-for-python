# SearchedSubscription

TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**subscription** | [**Subscription**](Subscription.md) |  | [optional] 
**exact** | **bool** |  | 
**similarity** | **float** |  | 
**temporal** | **bool** |  | [optional] 
**identifier** | **str** | This is the uuid of the source. | 

## Example

```python
from pieces_os_client.models.searched_subscription import SearchedSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedSubscription from a JSON string
searched_subscription_instance = SearchedSubscription.from_json(json)
# print the JSON string representation of the object
print SearchedSubscription.to_json()

# convert the object into a dict
searched_subscription_dict = searched_subscription_instance.to_dict()
# create an instance of SearchedSubscription from a dict
searched_subscription_from_dict = SearchedSubscription.from_dict(searched_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


