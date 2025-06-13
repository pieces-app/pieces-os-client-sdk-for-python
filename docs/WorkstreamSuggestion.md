# WorkstreamSuggestion

This is an individual material that is apart of the workstream feed. might want to also consider plural uuids ie top websites/tags/and others..  related: this is an optional field that will only be calculated for first degree relationships.          ie. an anchor may have related.iterable.first.persons that are not associated but related.          via the workstream patturn engine.  current: if current is defined then this is the current viewed object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**summary** | [**ReferencedWorkstreamSummary**](ReferencedWorkstreamSummary.md) |  | [optional] 
**asset** | [**ReferencedAsset**](ReferencedAsset.md) |  | [optional] 
**tag** | [**ReferencedTag**](ReferencedTag.md) |  | [optional] 
**website** | [**ReferencedWebsite**](ReferencedWebsite.md) |  | [optional] 
**anchor** | [**ReferencedAnchor**](ReferencedAnchor.md) |  | [optional] 
**conversation** | [**ReferencedConversation**](ReferencedConversation.md) |  | [optional] 
**person** | [**ReferencedPerson**](ReferencedPerson.md) |  | [optional] 
**seed** | [**Seed**](Seed.md) |  | [optional] 
**seeds** | [**Seeds**](Seeds.md) |  | [optional] 
**summaries** | [**FlattenedWorkstreamSummaries**](FlattenedWorkstreamSummaries.md) |  | [optional] 
**assets** | [**FlattenedAssets**](FlattenedAssets.md) |  | [optional] 
**tags** | [**FlattenedTags**](FlattenedTags.md) |  | [optional] 
**websites** | [**FlattenedWebsites**](FlattenedWebsites.md) |  | [optional] 
**anchors** | [**FlattenedAnchors**](FlattenedAnchors.md) |  | [optional] 
**conversations** | [**FlattenedConversations**](FlattenedConversations.md) |  | [optional] 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**related** | [**WorkstreamSuggestions**](WorkstreamSuggestions.md) |  | [optional] 
**current** | [**WorkstreamSuggestion**](WorkstreamSuggestion.md) |  | [optional] 
**annotation** | [**ReferencedAnnotation**](ReferencedAnnotation.md) |  | [optional] 
**annotations** | [**FlattenedAnnotations**](FlattenedAnnotations.md) |  | [optional] 
**conversation_message** | [**ReferencedConversationMessage**](ReferencedConversationMessage.md) |  | [optional] 
**conversation_messages** | [**FlattenedConversationMessages**](FlattenedConversationMessages.md) |  | [optional] 
**hint** | [**ReferencedHint**](ReferencedHint.md) |  | [optional] 
**hints** | [**FlattenedHints**](FlattenedHints.md) |  | [optional] 
**sensitive** | [**ReferencedSensitive**](ReferencedSensitive.md) |  | [optional] 
**sensitives** | [**FlattenedSensitives**](FlattenedSensitives.md) |  | [optional] 
**source** | [**ReferencedIdentifiedWorkstreamPatternEngineSource**](ReferencedIdentifiedWorkstreamPatternEngineSource.md) |  | [optional] 
**sources** | [**FlattenedIdentifiedWorkstreamPatternEngineSources**](FlattenedIdentifiedWorkstreamPatternEngineSources.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.workstream_suggestion import WorkstreamSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of WorkstreamSuggestion from a JSON string
workstream_suggestion_instance = WorkstreamSuggestion.from_json(json)
# print the JSON string representation of the object
print WorkstreamSuggestion.to_json()

# convert the object into a dict
workstream_suggestion_dict = workstream_suggestion_instance.to_dict()
# create an instance of WorkstreamSuggestion from a dict
workstream_suggestion_from_dict = WorkstreamSuggestion.from_dict(workstream_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


