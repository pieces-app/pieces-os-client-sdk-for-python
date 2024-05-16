# IDETab

This is a representation of an IDE Tab  value: is the value of the entire file(that being said we do not recomment passing this over as we can read this file on PieceOS side of things) classification: this is the classifcation of this file  selection: this is a represention of a copy/paste/selection of a bit of code  anchor: this is the file path  range: this is the duration that this user has been on this Tab  current: is a boolean that will let us know if this is the current active tab  contributors: is the people that are extracted via git  lsp: this is the languageserverprotocol this is used for may things such as error,stackstrces, mainly information extracted from the lang server

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**value** | [**TransferableString**](TransferableString.md) |  | [optional] 
**classification** | [**Classification**](Classification.md) |  | [optional] 
**selections** | [**IDESelections**](IDESelections.md) |  | [optional] 
**anchor** | [**SeededAnchor**](SeededAnchor.md) |  | 
**range** | [**AnonymousTemporalRange**](AnonymousTemporalRange.md) |  | [optional] 
**current** | **bool** |  | [optional] 
**contributors** | [**DocumentContributors**](DocumentContributors.md) |  | [optional] 
**lsp** | [**LanguageServerProtocol**](LanguageServerProtocol.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.ide_tab import IDETab

# TODO update the JSON string below
json = "{}"
# create an instance of IDETab from a JSON string
ide_tab_instance = IDETab.from_json(json)
# print the JSON string representation of the object
print IDETab.to_json()

# convert the object into a dict
ide_tab_dict = ide_tab_instance.to_dict()
# create an instance of IDETab from a dict
ide_tab_form_dict = ide_tab.from_dict(ide_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


