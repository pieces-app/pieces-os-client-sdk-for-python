# FlattenedActivity

Note: - if mechanism == internal we will not display to the user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**Application**](Application.md) |  | 
**asset** | [**ReferencedAsset**](ReferencedAsset.md) |  | [optional] 
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**event** | [**SeededConnectorTracking**](SeededConnectorTracking.md) |  | 
**format** | [**ReferencedFormat**](ReferencedFormat.md) |  | [optional] 
**id** | **str** |  | 
**mechanism** | [**MechanismEnum**](MechanismEnum.md) |  | 
**rank** | **int** |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**user** | [**FlattenedUserProfile**](FlattenedUserProfile.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.flattened_activity import FlattenedActivity

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedActivity from a JSON string
flattened_activity_instance = FlattenedActivity.from_json(json)
# print the JSON string representation of the object
print FlattenedActivity.to_json()

# convert the object into a dict
flattened_activity_dict = flattened_activity_instance.to_dict()
# create an instance of FlattenedActivity from a dict
flattened_activity_from_dict = FlattenedActivity.from_dict(flattened_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


