# Distributions

This is the plural Model of a Distribution.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[Distribution]**](Distribution.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.distributions import Distributions

# TODO update the JSON string below
json = "{}"
# create an instance of Distributions from a JSON string
distributions_instance = Distributions.from_json(json)
# print the JSON string representation of the object
print Distributions.to_json()

# convert the object into a dict
distributions_dict = distributions_instance.to_dict()
# create an instance of Distributions from a dict
distributions_form_dict = distributions.from_dict(distributions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


