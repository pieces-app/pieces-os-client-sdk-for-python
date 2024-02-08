# Hints

This is the plural of a Hint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[Hint]**](Hint.md) |  | 
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an hint id. | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from openapi_client.models.hints import Hints

# TODO update the JSON string below
json = "{}"
# create an instance of Hints from a JSON string
hints_instance = Hints.from_json(json)
# print the JSON string representation of the object
print Hints.to_json()

# convert the object into a dict
hints_dict = hints_instance.to_dict()
# create an instance of Hints from a dict
hints_form_dict = hints.from_dict(hints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


