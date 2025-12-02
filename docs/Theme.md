# Theme

This will describe the theme that belongs to a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dark** | **bool** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.theme import Theme

# TODO update the JSON string below
json = "{}"
# create an instance of Theme from a JSON string
theme_instance = Theme.from_json(json)
# print the JSON string representation of the object
print(Theme.to_json())

# convert the object into a dict
theme_dict = theme_instance.to_dict()
# create an instance of Theme from a dict
theme_from_dict = Theme.from_dict(theme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


