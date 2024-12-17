# TemporalSearchOptions

created: will return the materials based on if the range is satisfied w/ this created timestamp ** same goes for updated

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**created** | [**AnonymousTemporalRange**](AnonymousTemporalRange.md) |  | [optional] 
**updated** | [**AnonymousTemporalRange**](AnonymousTemporalRange.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.temporal_search_options import TemporalSearchOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TemporalSearchOptions from a JSON string
temporal_search_options_instance = TemporalSearchOptions.from_json(json)
# print the JSON string representation of the object
print TemporalSearchOptions.to_json()

# convert the object into a dict
temporal_search_options_dict = temporal_search_options_instance.to_dict()
# create an instance of TemporalSearchOptions from a dict
temporal_search_options_from_dict = TemporalSearchOptions.from_dict(temporal_search_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


