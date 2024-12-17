# Websites

This is a specific model for related websites to an asset.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an website id. | [optional] 
**iterable** | [**List[Website]**](Website.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.websites import Websites

# TODO update the JSON string below
json = "{}"
# create an instance of Websites from a JSON string
websites_instance = Websites.from_json(json)
# print the JSON string representation of the object
print Websites.to_json()

# convert the object into a dict
websites_dict = websites_instance.to_dict()
# create an instance of Websites from a dict
websites_from_dict = Websites.from_dict(websites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


