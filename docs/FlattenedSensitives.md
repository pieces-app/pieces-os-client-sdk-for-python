# FlattenedSensitives

This is a flattened representation of multiple sensitive pieces of data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[ReferencedSensitive]**](ReferencedSensitive.md) |  | 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_sensitives import FlattenedSensitives

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedSensitives from a JSON string
flattened_sensitives_instance = FlattenedSensitives.from_json(json)
# print the JSON string representation of the object
print FlattenedSensitives.to_json()

# convert the object into a dict
flattened_sensitives_dict = flattened_sensitives_instance.to_dict()
# create an instance of FlattenedSensitives from a dict
flattened_sensitives_from_dict = FlattenedSensitives.from_dict(flattened_sensitives_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


