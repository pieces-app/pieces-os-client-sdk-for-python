# QGPTConversationMessageRoleEnum

This is the role enum used for a QGPT conversation  SYSTEM_THINKING is a special role that is used to indicate that the message is a system thinking message. This is used to indicate that the message is a system thinking message. 'search for relevant files'... xyz 'searching google for xyz'...  USER: is the user message SYSTEM: is the system message(ie the message from the LLM)  NOTE: can expand in the future to anything that doesn't fit into a \"SYSTEM_THINKING\" bucket  i.e. \"SYSTEM_ACTION\" or \"SYSTEM_QUESTION\" where the system waits on a response from a user or even a  \"SYSTEM_CHECKIN\" where it's like should I keep going or something 

## Enum

* `UNKNOWN` (value: `'UNKNOWN'`)

* `USER` (value: `'USER'`)

* `SYSTEM` (value: `'SYSTEM'`)

* `ASSISTANT` (value: `'ASSISTANT'`)

* `SYSTEM_THINKING` (value: `'SYSTEM_THINKING'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


