# Formats

A base class for a collection of formats and some additional meta properties.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[Format]**](Format.md) |  | 

## Example

```python
from openapi_client.models.formats import Formats

# TODO update the JSON string below
json = "{}"
# create an instance of Formats from a JSON string
formats_instance = Formats.from_json(json)
# print the JSON string representation of the object
print Formats.to_json()

# convert the object into a dict
formats_dict = formats_instance.to_dict()
# create an instance of Formats from a dict
formats_form_dict = formats.from_dict(formats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


