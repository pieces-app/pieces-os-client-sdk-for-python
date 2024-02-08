# ReferencedPerson

[DAG Safe] version of a Person Model. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | 
**reference** | [**FlattenedPerson**](FlattenedPerson.md) |  | [optional] 

## Example

```python
from openapi_client.models.referenced_person import ReferencedPerson

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedPerson from a JSON string
referenced_person_instance = ReferencedPerson.from_json(json)
# print the JSON string representation of the object
print ReferencedPerson.to_json()

# convert the object into a dict
referenced_person_dict = referenced_person_instance.to_dict()
# create an instance of ReferencedPerson from a dict
referenced_person_form_dict = referenced_person.from_dict(referenced_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


