# SeededAnchor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**List[SeededAnnotation]**](SeededAnnotation.md) |  | [optional] 
**asset** | **str** | You may associate a SeededAnchor with an asset | [optional] 
**conversation** | **str** |  | [optional] 
**fullpath** | **str** |  | 
**name** | **str** |  | [optional] 
**persons** | [**FlattenedPersons**](FlattenedPersons.md) |  | [optional] 
**platform** | [**PlatformEnum**](PlatformEnum.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**type** | [**AnchorTypeEnum**](AnchorTypeEnum.md) |  | 
**watch** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.seeded_anchor import SeededAnchor

# TODO update the JSON string below
json = "{}"
# create an instance of SeededAnchor from a JSON string
seeded_anchor_instance = SeededAnchor.from_json(json)
# print the JSON string representation of the object
print(SeededAnchor.to_json())

# convert the object into a dict
seeded_anchor_dict = seeded_anchor_instance.to_dict()
# create an instance of SeededAnchor from a dict
seeded_anchor_from_dict = SeededAnchor.from_dict(seeded_anchor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


