# SeededTag

This is the minimum information needed when creating a Tag.  Default we will attach manual to a tag unless otherwise specified for mechanism.  you can optionally add an asset, format, or person uuid to attach this tag directly to it  TODO consider updating these asset,format to referenced Models

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | this is a uuid that references an asset. | [optional] 
**category** | [**TagCategoryEnum**](TagCategoryEnum.md) |  | [optional] 
**mechanism** | [**MechanismEnum**](MechanismEnum.md) |  | [optional] 
**person** | **str** | uuid of the person, you want to add this tag too | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**tags_vector** | **List[float]** | This is the embedding for the format.(NEEDs to collection.vector) and specific here because we can only index on a single name NOTE: this is the vector index that corresponds to the couchbase lite index. | [optional] 
**text** | **str** | This is the description of the tag. | 

## Example

```python
from pieces_os_client.models.seeded_tag import SeededTag

# TODO update the JSON string below
json = "{}"
# create an instance of SeededTag from a JSON string
seeded_tag_instance = SeededTag.from_json(json)
# print the JSON string representation of the object
print(SeededTag.to_json())

# convert the object into a dict
seeded_tag_dict = seeded_tag_instance.to_dict()
# create an instance of SeededTag from a dict
seeded_tag_from_dict = SeededTag.from_dict(seeded_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


