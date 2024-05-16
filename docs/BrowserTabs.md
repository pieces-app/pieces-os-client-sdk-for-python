# BrowserTabs

This is a plural representation of the BrowserTab

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[BrowserTab]**](BrowserTab.md) |  | 

## Example

```python
from pieces_os_client.models.browser_tabs import BrowserTabs

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserTabs from a JSON string
browser_tabs_instance = BrowserTabs.from_json(json)
# print the JSON string representation of the object
print BrowserTabs.to_json()

# convert the object into a dict
browser_tabs_dict = browser_tabs_instance.to_dict()
# create an instance of BrowserTabs from a dict
browser_tabs_form_dict = browser_tabs.from_dict(browser_tabs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


