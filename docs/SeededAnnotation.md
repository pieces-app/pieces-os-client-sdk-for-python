# SeededAnnotation

This is the percursor to a fully referenced Annotation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | **str** |  | [optional] 
**anchors** | [**FlattenedAnchors**](FlattenedAnchors.md) |  | [optional] 
**asset** | **str** |  | [optional] 
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**conversation** | **str** |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**favorited** | **bool** |  | [optional] 
**mechanism** | [**MechanismEnum**](MechanismEnum.md) |  | [optional] 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**model** | **str** |  | [optional] 
**person** | **str** |  | [optional] 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**pseudo** | **bool** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**tags** | [**FlattenedTags**](FlattenedTags.md) |  | [optional] 
**text** | **str** | This is the text of the annotation. | 
**type** | [**AnnotationTypeEnum**](AnnotationTypeEnum.md) |  | 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 
**workstream_events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 
**workstream_summary** | **str** |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_annotation import SeededAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of SeededAnnotation from a JSON string
seeded_annotation_instance = SeededAnnotation.from_json(json)
# print the JSON string representation of the object
print(SeededAnnotation.to_json())

# convert the object into a dict
seeded_annotation_dict = seeded_annotation_instance.to_dict()
# create an instance of SeededAnnotation from a dict
seeded_annotation_from_dict = SeededAnnotation.from_dict(seeded_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


