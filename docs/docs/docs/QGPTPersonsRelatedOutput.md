# QGPTPersonsRelatedOutput

This model is used for the output of the /qgpt/related/persons endpoint.  Explanations here is a custom object with key value pairs, when the key is the personUUId and the value is an explanation as to why this person was reccommended.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**persons** | [**Persons**](Persons.md) |  | 
**explanations** | **Dict[str, str]** | This is a Map&lt;String, String&gt; where the the key is a person id. and the value is the explanation. | [optional] 

## Example

```python
from openapi_client.models.qgpt_persons_related_output import QGPTPersonsRelatedOutput

# TODO update the JSON string below
json = "{}"
# create an instance of QGPTPersonsRelatedOutput from a JSON string
qgpt_persons_related_output_instance = QGPTPersonsRelatedOutput.from_json(json)
# print the JSON string representation of the object
print QGPTPersonsRelatedOutput.to_json()

# convert the object into a dict
qgpt_persons_related_output_dict = qgpt_persons_related_output_instance.to_dict()
# create an instance of QGPTPersonsRelatedOutput from a dict
qgpt_persons_related_output_form_dict = qgpt_persons_related_output.from_dict(qgpt_persons_related_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


