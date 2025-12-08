# FlattenedHints

This is the flattened Version of plural hints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an hint id. | [optional] 
**iterable** | [**List[ReferencedHint]**](ReferencedHint.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_hints import FlattenedHints

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedHints from a JSON string
flattened_hints_instance = FlattenedHints.from_json(json)
# print the JSON string representation of the object
print(FlattenedHints.to_json())

# convert the object into a dict
flattened_hints_dict = flattened_hints_instance.to_dict()
# create an instance of FlattenedHints from a dict
flattened_hints_from_dict = FlattenedHints.from_dict(flattened_hints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


