# Format

A representation of Data for a particular Form Factor of an Asset.  Below asset HAS to be Flattened because it is a leaf node and must prevent cycles agressively.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | [**Activities**](Activities.md) |  | [optional] 
**analysis** | [**Analysis**](Analysis.md) |  | [optional] 
**application** | [**Application**](Application.md) |  | 
**asset** | [**FlattenedAsset**](FlattenedAsset.md) |  | 
**bytes** | [**ByteDescriptor**](ByteDescriptor.md) |  | 
**classification** | [**Classification**](Classification.md) |  | 
**cloud** | **str** | This is a path used to determine what path this format lives at within the cloud. | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**creator** | **str** |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**file** | [**FileFormat**](FileFormat.md) |  | [optional] 
**fragment** | [**FragmentFormat**](FragmentFormat.md) |  | [optional] 
**icon** | **str** |  | [optional] 
**id** | **str** |  | 
**relationship** | [**Relationship**](Relationship.md) |  | [optional] 
**role** | [**Role**](Role.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**synced** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 

## Example

```python
from pieces_os_client.models.format import Format

# TODO update the JSON string below
json = "{}"
# create an instance of Format from a JSON string
format_instance = Format.from_json(json)
# print the JSON string representation of the object
print Format.to_json()

# convert the object into a dict
format_dict = format_instance.to_dict()
# create an instance of Format from a dict
format_from_dict = Format.from_dict(format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


