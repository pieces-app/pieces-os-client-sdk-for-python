# Classifications

This is a plural representation of a Classification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[Classification]**](Classification.md) |  | 

## Example

```python
from pieces_os_client.models.classifications import Classifications

# TODO update the JSON string below
json = "{}"
# create an instance of Classifications from a JSON string
classifications_instance = Classifications.from_json(json)
# print the JSON string representation of the object
print Classifications.to_json()

# convert the object into a dict
classifications_dict = classifications_instance.to_dict()
# create an instance of Classifications from a dict
classifications_form_dict = classifications.from_dict(classifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


