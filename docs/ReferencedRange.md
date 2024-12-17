# ReferencedRange

This is a minimal version of a Range, with mainly an Id.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**reference** | [**FlattenedRange**](FlattenedRange.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.referenced_range import ReferencedRange

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedRange from a JSON string
referenced_range_instance = ReferencedRange.from_json(json)
# print the JSON string representation of the object
print ReferencedRange.to_json()

# convert the object into a dict
referenced_range_dict = referenced_range_instance.to_dict()
# create an instance of ReferencedRange from a dict
referenced_range_from_dict = ReferencedRange.from_dict(referenced_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


