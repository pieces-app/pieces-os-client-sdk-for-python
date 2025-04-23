# StreamedIdentifier

This is currently only used within /assets/steam/identifiers && /conversations/steam/identifiers && annotations but can be used with other as well, if we want to expand this class.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**ReferencedAsset**](ReferencedAsset.md) |  | [optional] 
**conversation** | [**ReferencedConversation**](ReferencedConversation.md) |  | [optional] 
**annotation** | [**ReferencedAnnotation**](ReferencedAnnotation.md) |  | [optional] 
**activity** | [**ReferencedActivity**](ReferencedActivity.md) |  | [optional] 
**anchor** | [**ReferencedAnchor**](ReferencedAnchor.md) |  | [optional] 
**anchor_point** | [**ReferencedAnchorPoint**](ReferencedAnchorPoint.md) |  | [optional] 
**hint** | [**ReferencedHint**](ReferencedHint.md) |  | [optional] 
**conversation_message** | [**ReferencedConversationMessage**](ReferencedConversationMessage.md) |  | [optional] 
**format** | [**ReferencedFormat**](ReferencedFormat.md) |  | [optional] 
**person** | [**ReferencedPerson**](ReferencedPerson.md) |  | [optional] 
**range** | [**ReferencedRange**](ReferencedRange.md) |  | [optional] 
**sensitive** | [**ReferencedSensitive**](ReferencedSensitive.md) |  | [optional] 
**tag** | [**ReferencedTag**](ReferencedTag.md) |  | [optional] 
**website** | [**ReferencedWebsite**](ReferencedWebsite.md) |  | [optional] 
**application** | [**ReferencedApplication**](ReferencedApplication.md) |  | [optional] 
**model** | [**ReferencedModel**](ReferencedModel.md) |  | [optional] 
**workstream_summary** | [**ReferencedWorkstreamSummary**](ReferencedWorkstreamSummary.md) |  | [optional] 
**workstream_pattern_engine_source** | [**ReferencedIdentifiedWorkstreamPatternEngineSource**](ReferencedIdentifiedWorkstreamPatternEngineSource.md) |  | [optional] 
**deleted** | **bool** | This is a specific bool that will let us know if we deleted an Identifierfrom the db. | [optional] 

## Example

```python
from pieces_os_client.models.streamed_identifier import StreamedIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of StreamedIdentifier from a JSON string
streamed_identifier_instance = StreamedIdentifier.from_json(json)
# print the JSON string representation of the object
print StreamedIdentifier.to_json()

# convert the object into a dict
streamed_identifier_dict = streamed_identifier_instance.to_dict()
# create an instance of StreamedIdentifier from a dict
streamed_identifier_from_dict = StreamedIdentifier.from_dict(streamed_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


