# BigQueryInstanceConfiguration

Configuration for the BigQuery analytics feature  note: this model can scale to use dataset and table in the future

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.big_query_instance_configuration import BigQueryInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of BigQueryInstanceConfiguration from a JSON string
big_query_instance_configuration_instance = BigQueryInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(BigQueryInstanceConfiguration.to_json())

# convert the object into a dict
big_query_instance_configuration_dict = big_query_instance_configuration_instance.to_dict()
# create an instance of BigQueryInstanceConfiguration from a dict
big_query_instance_configuration_from_dict = BigQueryInstanceConfiguration.from_dict(big_query_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


