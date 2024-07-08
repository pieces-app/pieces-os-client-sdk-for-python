# AnonymousTemporalRange

if you want a range between you can use from && to.  if you want anything before, use to and NO from.  if you want anything after, use from and NO to.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**var_from** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**to** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**between** | **bool** |  | [optional] 
**continuous** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.anonymous_temporal_range import AnonymousTemporalRange

# TODO update the JSON string below
json = "{}"
# create an instance of AnonymousTemporalRange from a JSON string
anonymous_temporal_range_instance = AnonymousTemporalRange.from_json(json)
# print the JSON string representation of the object
print AnonymousTemporalRange.to_json()

# convert the object into a dict
anonymous_temporal_range_dict = anonymous_temporal_range_instance.to_dict()
# create an instance of AnonymousTemporalRange from a dict
anonymous_temporal_range_from_dict = AnonymousTemporalRange.from_dict(anonymous_temporal_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


