# SeededUser



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**emails** | **List[str]** |  | 

## Example

```python
from openapi_client.models.seeded_user import SeededUser

# TODO update the JSON string below
json = "{}"
# create an instance of SeededUser from a JSON string
seeded_user_instance = SeededUser.from_json(json)
# print the JSON string representation of the object
print SeededUser.to_json()

# convert the object into a dict
seeded_user_dict = seeded_user_instance.to_dict()
# create an instance of SeededUser from a dict
seeded_user_form_dict = seeded_user.from_dict(seeded_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


