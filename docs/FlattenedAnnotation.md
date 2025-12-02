# FlattenedAnnotation

This is the flattened Version of the annotation, IMPORTANT: when referencing these, ONLY Take the UUID, do NOT polinate(ie w/ asset/person/model) the FlattenedAnnotation as it can create an infinite loop.  UPDATE: the singular fields on here(asset, person, anchor, conversation, and summary) are all now deprecated... an annotation will now have a many to many relationship with all of it materials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | [**ReferencedAnchor**](ReferencedAnchor.md) |  | [optional] 
**anchors** | [**FlattenedAnchors**](FlattenedAnchors.md) |  | [optional] 
**asset** | [**ReferencedAsset**](ReferencedAsset.md) |  | [optional] 
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**conversation** | [**ReferencedConversation**](ReferencedConversation.md) |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**favorited** | **bool** |  | [optional] 
**id** | **str** |  | 
**mechanism** | [**MechanismEnum**](MechanismEnum.md) |  | [optional] 
**messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**model** | [**ReferencedModel**](ReferencedModel.md) |  | [optional] 
**person** | [**ReferencedPerson**](ReferencedPerson.md) |  | [optional] 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**pseudo** | **bool** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**summary** | [**ReferencedWorkstreamSummary**](ReferencedWorkstreamSummary.md) |  | [optional] 
**tags** | [**FlattenedTags**](FlattenedTags.md) |  | [optional] 
**text** | **str** | This is the text of the annotation. | 
**type** | [**AnnotationTypeEnum**](AnnotationTypeEnum.md) |  | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 
**workstream_events** | [**FlattenedWorkstreamEvents**](FlattenedWorkstreamEvents.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_annotation import FlattenedAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedAnnotation from a JSON string
flattened_annotation_instance = FlattenedAnnotation.from_json(json)
# print the JSON string representation of the object
print(FlattenedAnnotation.to_json())

# convert the object into a dict
flattened_annotation_dict = flattened_annotation_instance.to_dict()
# create an instance of FlattenedAnnotation from a dict
flattened_annotation_from_dict = FlattenedAnnotation.from_dict(flattened_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


