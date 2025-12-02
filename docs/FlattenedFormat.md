# FlattenedFormat

A representation of Data for a particular Form Factor of an Asset.[DAG Compatible - Directed Acyclic Graph Data Structure]  FlattenedFormats prevent Cycles in Reference because all outbound references are strings as opposed to crosspollinated objects.  i.e. FlattenedFormat.asset is Type String  fragment or file will always be defined. Even thought they are both optional.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | [**FlattenedActivities**](FlattenedActivities.md) |  | [optional] 
**analysis** | [**FlattenedAnalysis**](FlattenedAnalysis.md) |  | [optional] 
**application** | [**Application**](Application.md) |  | 
**asset** | **str** | A uuid model. 36 Characters (4 Dashes, 32 Numbers/Letters)  | 
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
from pieces_os_client.models.flattened_format import FlattenedFormat

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedFormat from a JSON string
flattened_format_instance = FlattenedFormat.from_json(json)
# print the JSON string representation of the object
print(FlattenedFormat.to_json())

# convert the object into a dict
flattened_format_dict = flattened_format_instance.to_dict()
# create an instance of FlattenedFormat from a dict
flattened_format_from_dict = FlattenedFormat.from_dict(flattened_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


