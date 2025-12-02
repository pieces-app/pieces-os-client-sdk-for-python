# InteractedAssets

A model which contains a list of InteractedAssets with potentially additional properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[InteractedAsset]**](InteractedAsset.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.interacted_assets import InteractedAssets

# TODO update the JSON string below
json = "{}"
# create an instance of InteractedAssets from a JSON string
interacted_assets_instance = InteractedAssets.from_json(json)
# print the JSON string representation of the object
print(InteractedAssets.to_json())

# convert the object into a dict
interacted_assets_dict = interacted_assets_instance.to_dict()
# create an instance of InteractedAssets from a dict
interacted_assets_from_dict = InteractedAssets.from_dict(interacted_assets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


