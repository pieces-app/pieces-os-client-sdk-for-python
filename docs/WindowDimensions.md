# WindowDimensions

note: this is modeled off of the browsers bounding box DOMRect https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bottom** | **float** |  | 
**height** | **float** |  | 
**left** | **float** |  | 
**right** | **float** |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**top** | **float** |  | 
**width** | **float** |  | 
**x** | **float** |  | 
**y** | **float** |  | 

## Example

```python
from pieces_os_client.models.window_dimensions import WindowDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of WindowDimensions from a JSON string
window_dimensions_instance = WindowDimensions.from_json(json)
# print the JSON string representation of the object
print(WindowDimensions.to_json())

# convert the object into a dict
window_dimensions_dict = window_dimensions_instance.to_dict()
# create an instance of WindowDimensions from a dict
window_dimensions_from_dict = WindowDimensions.from_dict(window_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


