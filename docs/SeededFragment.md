# SeededFragment

This will be either a TransferableString or TransferableBytes that represent your fragment. ONLY Pass one or the other DONT pass both or neither.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes** | [**TransferableBytes**](TransferableBytes.md) |  | [optional] 
**metadata** | [**FragmentMetadata**](FragmentMetadata.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**string** | [**TransferableString**](TransferableString.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_fragment import SeededFragment

# TODO update the JSON string below
json = "{}"
# create an instance of SeededFragment from a JSON string
seeded_fragment_instance = SeededFragment.from_json(json)
# print the JSON string representation of the object
print SeededFragment.to_json()

# convert the object into a dict
seeded_fragment_dict = seeded_fragment_instance.to_dict()
# create an instance of SeededFragment from a dict
seeded_fragment_from_dict = SeededFragment.from_dict(seeded_fragment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


