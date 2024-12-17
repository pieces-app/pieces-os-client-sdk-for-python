# SeededRangeConversationAssociation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**reference** | [**ReferencedConversation**](ReferencedConversation.md) |  | 
**grounding** | [**SeededRangeConversationGroundingAssociation**](SeededRangeConversationGroundingAssociation.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_range_conversation_association import SeededRangeConversationAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of SeededRangeConversationAssociation from a JSON string
seeded_range_conversation_association_instance = SeededRangeConversationAssociation.from_json(json)
# print the JSON string representation of the object
print SeededRangeConversationAssociation.to_json()

# convert the object into a dict
seeded_range_conversation_association_dict = seeded_range_conversation_association_instance.to_dict()
# create an instance of SeededRangeConversationAssociation from a dict
seeded_range_conversation_association_from_dict = SeededRangeConversationAssociation.from_dict(seeded_range_conversation_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


