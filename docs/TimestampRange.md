# TimestampRange

if you want a range between you can use from && to.  if you want anything before, use to and NO from.  if you want anything after, use from and NO to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**var_from** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**to** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**between** | **bool** |  | [optional] 

## Example

```python
from pieces_os_client.models.timestamp_range import TimestampRange

# TODO update the JSON string below
json = "{}"
# create an instance of TimestampRange from a JSON string
timestamp_range_instance = TimestampRange.from_json(json)
# print the JSON string representation of the object
print TimestampRange.to_json()

# convert the object into a dict
timestamp_range_dict = timestamp_range_instance.to_dict()
# create an instance of TimestampRange from a dict
timestamp_range_form_dict = timestamp_range.from_dict(timestamp_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


