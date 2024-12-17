# ProjectModules

This is a plural representation of the ProjectModule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[ProjectModule]**](ProjectModule.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.project_modules import ProjectModules

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectModules from a JSON string
project_modules_instance = ProjectModules.from_json(json)
# print the JSON string representation of the object
print ProjectModules.to_json()

# convert the object into a dict
project_modules_dict = project_modules_instance.to_dict()
# create an instance of ProjectModules from a dict
project_modules_from_dict = ProjectModules.from_dict(project_modules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


