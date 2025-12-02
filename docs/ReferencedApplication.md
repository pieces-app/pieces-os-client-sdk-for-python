# ReferencedApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**reference** | [**FlattenedApplication**](FlattenedApplication.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.referenced_application import ReferencedApplication

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedApplication from a JSON string
referenced_application_instance = ReferencedApplication.from_json(json)
# print the JSON string representation of the object
print(ReferencedApplication.to_json())

# convert the object into a dict
referenced_application_dict = referenced_application_instance.to_dict()
# create an instance of ReferencedApplication from a dict
referenced_application_from_dict = ReferencedApplication.from_dict(referenced_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


