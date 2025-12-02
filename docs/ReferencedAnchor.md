# ReferencedAnchor

This is the referenced version of a Anchor, main used for the uuid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**reference** | [**FlattenedAnchor**](FlattenedAnchor.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.referenced_anchor import ReferencedAnchor

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedAnchor from a JSON string
referenced_anchor_instance = ReferencedAnchor.from_json(json)
# print the JSON string representation of the object
print(ReferencedAnchor.to_json())

# convert the object into a dict
referenced_anchor_dict = referenced_anchor_instance.to_dict()
# create an instance of ReferencedAnchor from a dict
referenced_anchor_from_dict = ReferencedAnchor.from_dict(referenced_anchor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


