# BrowserSelection

This is a given bit of text/code that is selected in the browser, this can be a copy/paste/selection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | [**Classification**](Classification.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**value** | [**TransferableString**](TransferableString.md) |  | 

## Example

```python
from pieces_os_client.models.browser_selection import BrowserSelection

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserSelection from a JSON string
browser_selection_instance = BrowserSelection.from_json(json)
# print the JSON string representation of the object
print BrowserSelection.to_json()

# convert the object into a dict
browser_selection_dict = browser_selection_instance.to_dict()
# create an instance of BrowserSelection from a dict
browser_selection_from_dict = BrowserSelection.from_dict(browser_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


