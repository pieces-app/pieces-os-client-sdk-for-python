# QGPTPersonsRelatedInput

This is used for /qgpt/persons/related.  will accept a seed, or conversation all optionally. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | optional application id | [optional] 
**conversation** | [**QGPTConversation**](QGPTConversation.md) |  | [optional] 
**model** | **str** | optional model id | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**seed** | [**Seed**](Seed.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.qgpt_persons_related_input import QGPTPersonsRelatedInput

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTPersonsRelatedInput from a JSON string
qgpt_persons_related_input_instance = QGPTPersonsRelatedInput.from_json(json)
# print the JSON string representation of the object
print(QGPTPersonsRelatedInput.to_json())

# convert the object into a dict
qgpt_persons_related_input_dict = qgpt_persons_related_input_instance.to_dict()
# create an instance of QGPTPersonsRelatedInput from a dict
qgpt_persons_related_input_from_dict = QGPTPersonsRelatedInput.from_dict(qgpt_persons_related_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


