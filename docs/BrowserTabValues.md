# BrowserTabValues

Plural model that represent many tabs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[BrowserTabValue]**](BrowserTabValue.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.browser_tab_values import BrowserTabValues

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserTabValues from a JSON string
browser_tab_values_instance = BrowserTabValues.from_json(json)
# print the JSON string representation of the object
print BrowserTabValues.to_json()

# convert the object into a dict
browser_tab_values_dict = browser_tab_values_instance.to_dict()
# create an instance of BrowserTabValues from a dict
browser_tab_values_from_dict = BrowserTabValues.from_dict(browser_tab_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


