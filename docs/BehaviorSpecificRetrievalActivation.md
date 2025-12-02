# BehaviorSpecificRetrievalActivation

This will provide a running count of the number of deep study activations for the user.  thinking_message_group: this is a group id for the thinking messages of this current activation.  conversation: this is a referencedConversation will jsut include an id  type: is the type of activation this is. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**ReferencedConversation**](ReferencedConversation.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**thinking_message_group** | **str** |  | [optional] 
**type** | [**WorkstreamSummaryBehaviorEnum**](WorkstreamSummaryBehaviorEnum.md) |  | 

## Example

```python
from pieces_os_client.models.behavior_specific_retrieval_activation import BehaviorSpecificRetrievalActivation

# TODO update the JSON string below
json = "{}"
# create an instance of BehaviorSpecificRetrievalActivation from a JSON string
behavior_specific_retrieval_activation_instance = BehaviorSpecificRetrievalActivation.from_json(json)
# print the JSON string representation of the object
print(BehaviorSpecificRetrievalActivation.to_json())

# convert the object into a dict
behavior_specific_retrieval_activation_dict = behavior_specific_retrieval_activation_instance.to_dict()
# create an instance of BehaviorSpecificRetrievalActivation from a dict
behavior_specific_retrieval_activation_from_dict = BehaviorSpecificRetrievalActivation.from_dict(behavior_specific_retrieval_activation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


