# FlattenedDistribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 
**deleted** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | [optional] 
**github** | [**GitHubDistribution**](GitHubDistribution.md) |  | [optional] 
**id** | **str** |  | 
**mailgun** | [**MailgunDistribution**](MailgunDistribution.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**share** | **str** | This is the UUId of the share. | 
**updated** | [**GroupedTimestamp**](GroupedTimestamp.md) |  | 

## Example

```python
from pieces_os_client.models.flattened_distribution import FlattenedDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of FlattenedDistribution from a JSON string
flattened_distribution_instance = FlattenedDistribution.from_json(json)
# print the JSON string representation of the object
print(FlattenedDistribution.to_json())

# convert the object into a dict
flattened_distribution_dict = flattened_distribution_instance.to_dict()
# create an instance of FlattenedDistribution from a dict
flattened_distribution_from_dict = FlattenedDistribution.from_dict(flattened_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


