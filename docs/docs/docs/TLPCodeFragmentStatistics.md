# TLPCodeFragmentStatistics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**descriptive** | [**TLPCodeFragmentDescriptiveStatistics**](TLPCodeFragmentDescriptiveStatistics.md) |  | [optional] 

## Example

```python
from openapi_client.models.tlp_code_fragment_statistics import TLPCodeFragmentStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of TLPCodeFragmentStatistics from a JSON string
tlp_code_fragment_statistics_instance = TLPCodeFragmentStatistics.from_json(json)
# print the JSON string representation of the object
print TLPCodeFragmentStatistics.to_json()

# convert the object into a dict
tlp_code_fragment_statistics_dict = tlp_code_fragment_statistics_instance.to_dict()
# create an instance of TLPCodeFragmentStatistics from a dict
tlp_code_fragment_statistics_form_dict = tlp_code_fragment_statistics.from_dict(tlp_code_fragment_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


