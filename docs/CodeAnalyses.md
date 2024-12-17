# CodeAnalyses


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[CodeAnalysis]**](CodeAnalysis.md) |  | 

## Example

```python
from pieces_os_client.models.code_analyses import CodeAnalyses

# TODO update the JSON string below
json = "{}"
# create an instance of CodeAnalyses from a JSON string
code_analyses_instance = CodeAnalyses.from_json(json)
# print the JSON string representation of the object
print CodeAnalyses.to_json()

# convert the object into a dict
code_analyses_dict = code_analyses_instance.to_dict()
# create an instance of CodeAnalyses from a dict
code_analyses_from_dict = CodeAnalyses.from_dict(code_analyses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


