# SegmentInstanceConfiguration

Configuration for the Segment analytics feature  note: this model can scale to use API key and headers in the future

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.segment_instance_configuration import SegmentInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentInstanceConfiguration from a JSON string
segment_instance_configuration_instance = SegmentInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(SegmentInstanceConfiguration.to_json())

# convert the object into a dict
segment_instance_configuration_dict = segment_instance_configuration_instance.to_dict()
# create an instance of SegmentInstanceConfiguration from a dict
segment_instance_configuration_from_dict = SegmentInstanceConfiguration.from_dict(segment_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


