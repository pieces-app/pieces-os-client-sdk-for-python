# Accessors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[Accessor]**](Accessor.md) |  | 

## Example

```python
from openapi_client.models.accessors import Accessors

# TODO update the JSON string below
json = "{}"
# create an instance of Accessors from a JSON string
accessors_instance = Accessors.from_json(json)
# print the JSON string representation of the object
print Accessors.to_json()

# convert the object into a dict
accessors_dict = accessors_instance.to_dict()
# create an instance of Accessors from a dict
accessors_form_dict = accessors.from_dict(accessors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


