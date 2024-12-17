# CodeAnalysis

This is the ML Analysis object Specific to code.  prediction and similarity are custom types. ** please dont not modify **

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | **str** | this is just a reference to the analysis parent object. | 
**id** | **str** |  | 
**language** | **str** |  | [optional] 
**model** | [**Model**](Model.md) |  | 
**prediction** | **Dict[str, float]** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**similarity** | **Dict[str, float]** |  | [optional] 
**tokenized** | **List[str]** |  | [optional] 
**top5_colors** | **List[int]** |  | [optional] 
**top5_sorted** | **List[str]** |  | [optional] 
**type** | [**ClassificationGenericEnum**](ClassificationGenericEnum.md) |  | 

## Example

```python
from pieces_os_client.models.code_analysis import CodeAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of CodeAnalysis from a JSON string
code_analysis_instance = CodeAnalysis.from_json(json)
# print the JSON string representation of the object
print CodeAnalysis.to_json()

# convert the object into a dict
code_analysis_dict = code_analysis_instance.to_dict()
# create an instance of CodeAnalysis from a dict
code_analysis_from_dict = CodeAnalysis.from_dict(code_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


