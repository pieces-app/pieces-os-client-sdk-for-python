# FlattenedUsers

A DAG-Safe collection of User references.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the key is a user id. | [optional] 
**iterable** | [**List[ReferencedUser]**](ReferencedUser.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_users import FlattenedUsers

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedUsers from a JSON string
flattened_users_instance = FlattenedUsers.from_json(json)
# print the JSON string representation of the object
print(FlattenedUsers.to_json())

# convert the object into a dict
flattened_users_dict = flattened_users_instance.to_dict()
# create an instance of FlattenedUsers from a dict
flattened_users_from_dict = FlattenedUsers.from_dict(flattened_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


