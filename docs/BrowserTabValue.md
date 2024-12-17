# BrowserTabValue

snippet: these are extracted code blocks selection: here is a copy/paste/selection  note: recommended that you pass in the md version of the webpage  note: please dont pass in all three html,md,text, just pass in 1.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | [**TransferableString**](TransferableString.md) |  | [optional] 
**md** | [**TransferableString**](TransferableString.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**selection** | [**BrowserSelection**](BrowserSelection.md) |  | [optional] 
**snippet** | [**BrowserSelection**](BrowserSelection.md) |  | [optional] 
**text** | [**TransferableString**](TransferableString.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.browser_tab_value import BrowserTabValue

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserTabValue from a JSON string
browser_tab_value_instance = BrowserTabValue.from_json(json)
# print the JSON string representation of the object
print BrowserTabValue.to_json()

# convert the object into a dict
browser_tab_value_dict = browser_tab_value_instance.to_dict()
# create an instance of BrowserTabValue from a dict
browser_tab_value_from_dict = BrowserTabValue.from_dict(browser_tab_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


