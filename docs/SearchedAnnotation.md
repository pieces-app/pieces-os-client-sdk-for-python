# SearchedAnnotation

This is used for the Annotation searching endpoint  annotation here is only provided if transferables are set to true.  temporal: if this is provided this means that their material matched the input via a timestamp.  TODO will want to consider returning related materials to this material potentially both associated/ and not associated materials ie suggestion: WorkstreamSuggestions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**annotation** | [**Annotation**](Annotation.md) |  | [optional] 
**exact** | **bool** |  | 
**similarity** | **float** |  | 
**temporal** | **bool** |  | [optional] 
**identifier** | **str** | This is the uuid of the annotation. | 

## Example

```python
from pieces_os_client.models.searched_annotation import SearchedAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of SearchedAnnotation from a JSON string
searched_annotation_instance = SearchedAnnotation.from_json(json)
# print the JSON string representation of the object
print SearchedAnnotation.to_json()

# convert the object into a dict
searched_annotation_dict = searched_annotation_instance.to_dict()
# create an instance of SearchedAnnotation from a dict
searched_annotation_from_dict = SearchedAnnotation.from_dict(searched_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


