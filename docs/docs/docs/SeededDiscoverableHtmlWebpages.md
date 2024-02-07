# SeededDiscoverableHtmlWebpages


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[SeededDiscoverableHtmlWebpage]**](SeededDiscoverableHtmlWebpage.md) |  | 
**application** | **str** | This is the applicaiton Id used to connect to Pieces OS. | 

## Example

```python
from openapi_client.models.seeded_discoverable_html_webpages import SeededDiscoverableHtmlWebpages

# TODO update the JSON string below
json = "{}"
# create an instance of SeededDiscoverableHtmlWebpages from a JSON string
seeded_discoverable_html_webpages_instance = SeededDiscoverableHtmlWebpages.from_json(json)
# print the JSON string representation of the object
print SeededDiscoverableHtmlWebpages.to_json()

# convert the object into a dict
seeded_discoverable_html_webpages_dict = seeded_discoverable_html_webpages_instance.to_dict()
# create an instance of SeededDiscoverableHtmlWebpages from a dict
seeded_discoverable_html_webpages_form_dict = seeded_discoverable_html_webpages.from_dict(seeded_discoverable_html_webpages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


