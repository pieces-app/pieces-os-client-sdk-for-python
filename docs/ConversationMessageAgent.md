# ConversationMessageAgent

Structured agent object for message context, providing information about the agent that generated or processed a specific message within multi-agent workflows.  This object is used to enhance visibility of model's multi-agent workflows and is particularly useful for the DEEP_STUDY feature, allowing for better UI representation and grouping of agent activities.  NOTE: think about this for future usage         status: (but use an enum)   type: string   description: Current status of the agent's activity.   enum:     - initialized     - in_progress     - completed     - failed     - timed_out

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | A unique identifier to group all agent messages for a specific user session or a particular response generation turn. This is crucial for UI grouping. | 
**instance_id** | **str** | Unique identifier for a specific agent instance (e.g., C-1, C-2, C-3). Optional, can be null. | [optional] 
**readable_description** | **str** | A brief, human-readable description of what this specific agent/task does. (this is for future support.) | [optional] 
**readable_name** | **str** | Human-readable name for UI display. This would typically be derived from &#39;role&#39; and &#39;task&#39;. (this is for future usage) | [optional] 
**role** | **str** | The broad category or role of the agent (e.g., \&quot;Orchestrator\&quot;, \&quot;Thinking\&quot;, \&quot;GraphGeneration\&quot;, \&quot;DraftGeneration\&quot;). | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**task** | **str** | The specific phase or task the agent is performing (e.g., \&quot;Phase1\&quot;, \&quot;GraphNoising\&quot;, \&quot;GraphQuestionGeneration\&quot;, \&quot;Initialized\&quot;). | [optional] 

## Example

```python
from pieces_os_client.models.conversation_message_agent import ConversationMessageAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageAgent from a JSON string
conversation_message_agent_instance = ConversationMessageAgent.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageAgent.to_json())

# convert the object into a dict
conversation_message_agent_dict = conversation_message_agent_instance.to_dict()
# create an instance of ConversationMessageAgent from a dict
conversation_message_agent_from_dict = ConversationMessageAgent.from_dict(conversation_message_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


