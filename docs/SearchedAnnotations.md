# SearchedAnnotations

This is the plural Model used to return many SearchedAnnotation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[SearchedAnnotation]**](SearchedAnnotation.md) |  | 

## Example

```python
from pieces_os_client.models.searched_annotations import SearchedAnnotations

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedAnnotations from a JSON string
searched_annotations_instance = SearchedAnnotations.from_json(json)
# print the JSON string representation of the object
print SearchedAnnotations.to_json()

# convert the object into a dict
searched_annotations_dict = searched_annotations_instance.to_dict()
# create an instance of SearchedAnnotations from a dict
searched_annotations_from_dict = SearchedAnnotations.from_dict(searched_annotations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


