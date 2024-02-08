# FlattenedWebsites

This is a specific model for related websites to an asset.[DAG SAFE]

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[ReferencedWebsite]**](ReferencedWebsite.md) |  | 
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an website id. | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from openapi_client.models.flattened_websites import FlattenedWebsites

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedWebsites from a JSON string
flattened_websites_instance = FlattenedWebsites.from_json(json)
# print the JSON string representation of the object
print FlattenedWebsites.to_json()

# convert the object into a dict
flattened_websites_dict = flattened_websites_instance.to_dict()
# create an instance of FlattenedWebsites from a dict
flattened_websites_form_dict = flattened_websites.from_dict(flattened_websites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


