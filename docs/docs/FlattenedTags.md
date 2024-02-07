# FlattenedTags

This is multiple ReferencedTags(which includes an optional FlattenedTag Model within the reference model).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[ReferencedTag]**](ReferencedTag.md) |  | 
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an tag id. | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from openapi_client.models.flattened_tags import FlattenedTags

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedTags from a JSON string
flattened_tags_instance = FlattenedTags.from_json(json)
# print the JSON string representation of the object
print FlattenedTags.to_json()

# convert the object into a dict
flattened_tags_dict = flattened_tags_instance.to_dict()
# create an instance of FlattenedTags from a dict
flattened_tags_form_dict = flattened_tags.from_dict(flattened_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


