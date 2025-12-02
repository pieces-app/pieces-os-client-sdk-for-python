# FlattenedAssets

A collection of Assets specific to the authenticated user. [DAG Compatible - Directed Acyclic Graph Data Structure]  FlattenedAssets prevent Cycles in Reference because all outbound references are strings as opposed to crosspollinated objects.  i.e. Asset asset = FlattenedAssets.iterable[0] => Format format = asset.preview => String id = format.asset => String id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **Dict[str, int]** | This is a Map&lt;String, int&gt; where the the key is an asset id. | [optional] 
**iterable** | [**List[ReferencedAsset]**](ReferencedAsset.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_assets import FlattenedAssets

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedAssets from a JSON string
flattened_assets_instance = FlattenedAssets.from_json(json)
# print the JSON string representation of the object
print(FlattenedAssets.to_json())

# convert the object into a dict
flattened_assets_dict = flattened_assets_instance.to_dict()
# create an instance of FlattenedAssets from a dict
flattened_assets_from_dict = FlattenedAssets.from_dict(flattened_assets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


