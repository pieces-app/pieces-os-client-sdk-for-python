# Assets

A base class for a collection of assets and some additional meta properties. Fully Populated with Formats internally (not just uuid's).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[Asset]**](Asset.md) |  | 
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an asset id. | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from openapi_client.models.assets import Assets

# TODO update the JSON string below
json = "{}"
# create an instance of Assets from a JSON string
assets_instance = Assets.from_json(json)
# print the JSON string representation of the object
print Assets.to_json()

# convert the object into a dict
assets_dict = assets_instance.to_dict()
# create an instance of Assets from a dict
assets_form_dict = assets.from_dict(assets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


