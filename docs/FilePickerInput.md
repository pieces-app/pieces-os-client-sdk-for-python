# FilePickerInput

This is the input model for the FilePicker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**allowed_extensions** | **List[str]** |  | [optional] 
**allow_multiple** | **bool** | default behavior is set to true | [optional] 

## Example

```python
from pieces_os_client.models.file_picker_input import FilePickerInput

# TODO update the JSON string below
json = "{}"
# create an instance of FilePickerInput from a JSON string
file_picker_input_instance = FilePickerInput.from_json(json)
# print the JSON string representation of the object
print FilePickerInput.to_json()

# convert the object into a dict
file_picker_input_dict = file_picker_input_instance.to_dict()
# create an instance of FilePickerInput from a dict
file_picker_input_from_dict = FilePickerInput.from_dict(file_picker_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


