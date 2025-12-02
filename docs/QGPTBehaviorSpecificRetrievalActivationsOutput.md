# QGPTBehaviorSpecificRetrievalActivationsOutput

This will provide a running count of the number of deep study activations for the user.  activations: this is a list of currently active behaviorSpecificRetrievals 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activations** | [**List[BehaviorSpecificRetrievalActivation]**](BehaviorSpecificRetrievalActivation.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.qgpt_behavior_specific_retrieval_activations_output import QGPTBehaviorSpecificRetrievalActivationsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTBehaviorSpecificRetrievalActivationsOutput from a JSON string
qgpt_behavior_specific_retrieval_activations_output_instance = QGPTBehaviorSpecificRetrievalActivationsOutput.from_json(json)
# print the JSON string representation of the object
print(QGPTBehaviorSpecificRetrievalActivationsOutput.to_json())

# convert the object into a dict
qgpt_behavior_specific_retrieval_activations_output_dict = qgpt_behavior_specific_retrieval_activations_output_instance.to_dict()
# create an instance of QGPTBehaviorSpecificRetrievalActivationsOutput from a dict
qgpt_behavior_specific_retrieval_activations_output_from_dict = QGPTBehaviorSpecificRetrievalActivationsOutput.from_dict(qgpt_behavior_specific_retrieval_activations_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


