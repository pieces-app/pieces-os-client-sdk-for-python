# IDESelection

This is a given bit of text/code that is selected in the IDE, this can be a copy/paste/selection  location: this is the given location provided by the LSP(might need to be a different object we will see)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | [**Classification**](Classification.md) |  | [optional] 
**location** | [**LanguageServerProtocolLocation**](LanguageServerProtocolLocation.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**value** | [**TransferableString**](TransferableString.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.ide_selection import IDESelection

# TODO update the JSON string below
json = "{}"
# create an instance of IDESelection from a JSON string
ide_selection_instance = IDESelection.from_json(json)
# print the JSON string representation of the object
print(IDESelection.to_json())

# convert the object into a dict
ide_selection_dict = ide_selection_instance.to_dict()
# create an instance of IDESelection from a dict
ide_selection_from_dict = IDESelection.from_dict(ide_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


