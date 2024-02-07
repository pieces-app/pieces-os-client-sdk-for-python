# Sensitives

This is a model that represents many individual sensitive pieces of data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[Sensitive]**](Sensitive.md) |  | 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from openapi_client.models.sensitives import Sensitives

# TODO update the JSON string below
json = "{}"
# create an instance of Sensitives from a JSON string
sensitives_instance = Sensitives.from_json(json)
# print the JSON string representation of the object
print Sensitives.to_json()

# convert the object into a dict
sensitives_dict = sensitives_instance.to_dict()
# create an instance of Sensitives from a dict
sensitives_form_dict = sensitives.from_dict(sensitives_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


