# Seed

A seed Model used to wrap a format or asset  Note: we will expand this now to support additional paramerters.  Note: however if create an asset, only pass in the asset, not passing in an asset in this case will cause the endpoint to fail.  TODO: for a breaking change update the type enum here to add support for the additional materials or remove it entirely.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**asset** | [**SeededAsset**](SeededAsset.md) |  | [optional] 
**person** | [**SeededPerson**](SeededPerson.md) |  | [optional] 
**anchor** | [**SeededAnchor**](SeededAnchor.md) |  | [optional] 
**website** | [**SeededWebsite**](SeededWebsite.md) |  | [optional] 
**type** | [**SeedTypeEnum**](SeedTypeEnum.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seed import Seed

# TODO update the JSON string below
json = "{}"
# create an instance of Seed from a JSON string
seed_instance = Seed.from_json(json)
# print the JSON string representation of the object
print Seed.to_json()

# convert the object into a dict
seed_dict = seed_instance.to_dict()
# create an instance of Seed from a dict
seed_from_dict = Seed.from_dict(seed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


