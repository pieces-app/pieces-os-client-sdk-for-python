# ProjectModule

This is a representation of a Module or a Project  anchor: is the folder path of this repo/module  contributors: is a nice to have is all the contributors of this repo/module  range: is the amount of time this user has been working on this repo  classifications: if all the languages that are used within this repo/module

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**anchor** | [**SeededAnchor**](SeededAnchor.md) |  | 
**range** | [**AnonymousTemporalRange**](AnonymousTemporalRange.md) |  | [optional] 
**contributors** | [**DocumentContributors**](DocumentContributors.md) |  | [optional] 
**classifications** | [**Classifications**](Classifications.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.project_module import ProjectModule

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectModule from a JSON string
project_module_instance = ProjectModule.from_json(json)
# print the JSON string representation of the object
print ProjectModule.to_json()

# convert the object into a dict
project_module_dict = project_module_instance.to_dict()
# create an instance of ProjectModule from a dict
project_module_form_dict = project_module.from_dict(project_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


