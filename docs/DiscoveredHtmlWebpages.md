# DiscoveredHtmlWebpages

Assumption: The iterable will be in the exact same order as it was passed in within the seededDiscoveredHtmlWebpages

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** |  | 
**iterable** | [**List[DiscoveredHtmlWebpage]**](DiscoveredHtmlWebpage.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.discovered_html_webpages import DiscoveredHtmlWebpages

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveredHtmlWebpages from a JSON string
discovered_html_webpages_instance = DiscoveredHtmlWebpages.from_json(json)
# print the JSON string representation of the object
print DiscoveredHtmlWebpages.to_json()

# convert the object into a dict
discovered_html_webpages_dict = discovered_html_webpages_instance.to_dict()
# create an instance of DiscoveredHtmlWebpages from a dict
discovered_html_webpages_from_dict = DiscoveredHtmlWebpages.from_dict(discovered_html_webpages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


