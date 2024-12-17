# Seeds

This is a plural model for multiple Seed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterable** | [**List[Seed]**](Seed.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeds import Seeds

# TODO update the JSON string below
json = "{}"
# create an instance of Seeds from a JSON string
seeds_instance = Seeds.from_json(json)
# print the JSON string representation of the object
print Seeds.to_json()

# convert the object into a dict
seeds_dict = seeds_instance.to_dict()
# create an instance of Seeds from a dict
seeds_from_dict = Seeds.from_dict(seeds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


