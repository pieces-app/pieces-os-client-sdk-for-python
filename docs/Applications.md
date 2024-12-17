# Applications

A list of all the applications

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[Application]**](Application.md) |  | 

## Example

```python
from pieces_os_client.models.applications import Applications

# TODO update the JSON string below
json = "{}"
# create an instance of Applications from a JSON string
applications_instance = Applications.from_json(json)
# print the JSON string representation of the object
print Applications.to_json()

# convert the object into a dict
applications_dict = applications_instance.to_dict()
# create an instance of Applications from a dict
applications_from_dict = Applications.from_dict(applications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


