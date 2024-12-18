# ModelCapabilities

This will let us know what capabilities the model is aloud to be used for.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**temporal** | **bool** | True if model is able to support live context and any other temporally powered RAG Capabilities i.e. \&quot;What did I do yesterday?\&quot; | [optional] 
**images** | **bool** | True if the model can leverage images and graphical material files in it&#39;s context window | [optional] 
**videos** | **bool** | True if the model can leverage videos files in it&#39;s context window | [optional] 
**documents** | **bool** | True if the model can leverage code/text/other files in it&#39;s context window | [optional] 
**codebases** | **bool** | True if the model can leverage entire code bases/snippetized code bases in its context window | [optional] 
**assets** | **bool** | True if the model can leverage saved assets &amp; their metadata in its context window. | [optional] 
**websites** | **bool** | True if the model can leverage websites in its context window. | [optional] 

## Example

```python
from pieces_os_client.models.model_capabilities import ModelCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCapabilities from a JSON string
model_capabilities_instance = ModelCapabilities.from_json(json)
# print the JSON string representation of the object
print ModelCapabilities.to_json()

# convert the object into a dict
model_capabilities_dict = model_capabilities_instance.to_dict()
# create an instance of ModelCapabilities from a dict
model_capabilities_from_dict = ModelCapabilities.from_dict(model_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


