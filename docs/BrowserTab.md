# BrowserTab

a tab can have many values because you might want to pass in a value that represents the code_blocks(snippets) or a md represenet note: please only pass 1 representation, I will clean on POS side tho (txt || md || html)  anchor: can be defined in the browser if view a local file  website: this is the given url of the tab  range: this is the amount of time this user is current on this given tab  current: means that this is the current tab that is open  contributors: these are all the extracted people from this given tab

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | [**SeededAnchor**](SeededAnchor.md) |  | [optional] 
**contributors** | [**DocumentContributors**](DocumentContributors.md) |  | [optional] 
**current** | **bool** |  | [optional] 
**range** | [**AnonymousTemporalRange**](AnonymousTemporalRange.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**values** | [**BrowserTabValues**](BrowserTabValues.md) |  | [optional] 
**website** | [**SeededWebsite**](SeededWebsite.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.browser_tab import BrowserTab

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserTab from a JSON string
browser_tab_instance = BrowserTab.from_json(json)
# print the JSON string representation of the object
print(BrowserTab.to_json())

# convert the object into a dict
browser_tab_dict = browser_tab_instance.to_dict()
# create an instance of BrowserTab from a dict
browser_tab_from_dict = BrowserTab.from_dict(browser_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


