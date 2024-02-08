# FlattenedAnnotations

This is a flattened plural of Annotation, typically this will just be a list of uuids.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[ReferencedAnnotation]**](ReferencedAnnotation.md) |  | 
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an annotation id. | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from openapi_client.models.flattened_annotations import FlattenedAnnotations

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedAnnotations from a JSON string
flattened_annotations_instance = FlattenedAnnotations.from_json(json)
# print the JSON string representation of the object
print FlattenedAnnotations.to_json()

# convert the object into a dict
flattened_annotations_dict = flattened_annotations_instance.to_dict()
# create an instance of FlattenedAnnotations from a dict
flattened_annotations_form_dict = flattened_annotations.from_dict(flattened_annotations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


