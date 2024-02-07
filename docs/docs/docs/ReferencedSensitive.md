# ReferencedSensitive

A reference to a sensitive which at minimum must have the Sensitive id. But in the case of a hydrated client API it may have a populated reference of type Sensitive.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**id** | **str** |  | 
**reference** | [**FlattenedSensitive**](FlattenedSensitive.md) |  | [optional] 

## Example

```python
from openapi_client.models.referenced_sensitive import ReferencedSensitive

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedSensitive from a JSON string
referenced_sensitive_instance = ReferencedSensitive.from_json(json)
# print the JSON string representation of the object
print ReferencedSensitive.to_json()

# convert the object into a dict
referenced_sensitive_dict = referenced_sensitive_instance.to_dict()
# create an instance of ReferencedSensitive from a dict
referenced_sensitive_form_dict = referenced_sensitive.from_dict(referenced_sensitive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


